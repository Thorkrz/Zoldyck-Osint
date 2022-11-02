import requests 
from urllib.parse import urlparse,urljoin 
from bs4 import BeautifulSoup as bs 
import colorama 
from rich.console import Console

console = Console()
colorama.init()

GREEN = colorama.Fore.GREEN
GRAY = colorama.Fore.LIGHTBLACK_EX
YELLOW = colorama.Fore.YELLOW 


interal_urls = set()
external_urls = set()


def is_valid(url):

    parsed = urlparse(url)

    return bool(parsed.netloc) and bool(parsed.scheme) 



def get_all_urls(url): 


    urls = set()
    domian_name = urlparse(url).netloc 
    soup = bs(requests.get(url).content,"html.parser")

    for a_tag in soup.find_all("a"):

        href = a_tag.attrs.get("href")

        if href == "" and href is None:

            continue 

        href = urljoin(url,href)
        parsed_href = urlparse(href)
        parsed_href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        
        if not is_valid(href):

            continue 

        if href in interal_urls:
            continue 


        if domian_name not in href:

            if href not in external_urls:

                print(f"{GRAY}[*] External Url: {href}")
                external_urls.add(href)

        
        print(f"{GREEN}[+] Internal Url: {href}")
        urls.add(href)
        interal_urls.add(href)
    
    return urls 

total_urls_visited = 0

def crawl(url,max_urls=30):

     
    global total_urls_visited 
    total_urls_visited += 1 
    print(f"{YELLOW}[*] Crawling: {url}")
    links = get_all_urls(url)

    for link in links:

        if total_urls_visited > max_urls:
            break 
        
        crawl(link,max_urls=max_urls)
    
    
def total():
    console.print("[white]=[/white]"*35)
    console.print(f"    [red]INFORMAÇÕES ADICIONAIS[/red]")
    console.print("[white]=[/white]"*35)
    console.print(f"[green][+] Total de Internal Urls:[/green] [white]{len(interal_urls)}[/white] ")
    console.print(f"[green][+] Total de External Urls:[/green] [white]{len(external_urls)}[/white] ")
    console.print(f"[green][+] Total Urls:[/green] [white]{len(external_urls) + len(interal_urls)}[/white] ")
    console.print("[white]=[/white]"*35)

