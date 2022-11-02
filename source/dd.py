import requests
import json 
from rich.console import Console 


console = Console()


def get_dd(dd): 

  try:
        req = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{dd}")
        json_data = req.json()
        json_state = json_data["state"]
        json_city = json_data["cities"][0]
        json_city2 = json_data["cities"][1]
        json_city3 = json_data["cities"][2]
        json_city4 = json_data["cities"][3]
        json_city5 = json_data["cities"][4]
        json_city6 = json_data["cities"][5]
        json_city7 = json_data["cities"][6]
        json_city8 = json_data["cities"][7]
        json_city9 = json_data["cities"][8]
        json_city10 = json_data["cities"][9]
        json_city11 = json_data["cities"][10]
        json_city12 = json_data["cities"][11]
        json_city13 = json_data["cities"][12]
        json_city14 = json_data["cities"][13]
        json_city15 = json_data["cities"][14]
        json_city16 = json_data["cities"][15]
        json_city17 = json_data["cities"][16]
        json_city18 = json_data["cities"][17]
        json_city19 = json_data["cities"][18]
        json_city20 = json_data["cities"][19]
        json_city21 = json_data["cities"][20]
        json_city22 = json_data["cities"][21]
    
        
        print("="*34)
        console.print(f"      [red]CIDADES DO DD {dd}[/red]")
        print("="*34)
        console.print(f"[green][+] Estado:[/green] [white]{json_state}[/white]\n[green][+] Cidade 1:[/green] [white]{json_city}[/white]\n[green][+] Cidade 2:[/green] [white]{json_city2}[/white]\n[green][+] Cidade 3:[/green] [white]{json_city3}[/white]\n[green][+] Cidade 4:[/green] [white]{json_city4}[/white]\n[green][+] Cidade 5:[/green] [white]{json_city5}[/white]\n[green][+] Cidade 6:[/green] [white]{json_city7}[/white]\n[green][+] Cidade 7:[/green] [white]{json_city7}[/white]\n[green][+] Cidade 8:[/green] [white]{json_city8}[/white]\n[green][+] Cidade 9:[/green] [white]{json_city9}[/white]\n[green][+] Cidade 10:[/green] [white]{json_city10}[/white]\n[green][+] Cidade 11:[/green] [white]{json_city11}[/white]\n[green][+] Cidade 12:[/green] [white]{json_city12}[/white]\n[green][+] Cidade 13:[/green] [white]{json_city13}[/white]\n[green][+] Cidade 14:[/green] [white]{json_city14}[/white]\n[green][+] Cidade 15:[/green] [white]{json_city15}[/white]\n[green][+] Cidade 16:[/green] [white]{json_city16}[/white]\n[green][+] Cidade 17:[/green] [white]{json_city17}[/white]\n[green][+] Cidade 18:[/green] [white]{json_city18}[/white]\n[green][+] Cidade 19:[/green] [white]{json_city19}[/white]\n[green][+] Cidade 20:[/green] [white]{json_city20}[/white]\n[green][+] Cidade 21:[/green] [white]{json_city21}[/white]\n[green][+] Cidade 22:[/green] [white]{json_city22}[/white]")
        print("="*34)
  except:
         
        console.print("[red][*] ERROR DD NÂO ENCONTRADO[/red]")
         


