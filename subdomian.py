import requests 
from rich.console import Console 


console = Console()


def scanner(domian_name):


    with open("subdomínios.txt","r") as file:


        arquivo = file.read()
        sub_dom = arquivo.splitlines()

        for subdomian in sub_dom: 
            url = f"https://{subdomian}.{domian_name}"
            try:
                requests.get(url)
                console.print(f"[green][+] {url}[/green]")

            except requests.ConnectionError: 
                pass
        
    