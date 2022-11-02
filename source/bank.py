import requests 
import json 
from rich.console import Console 

console = Console()



def get_bank(code): 

   try:
        req = requests.get(f"https://brasilapi.com.br/api/banks/v1/{code}")
        json_data = req.json()
        json_ispb = json_data["ispb"]
        json_name = json_data["name"]
        json_code = json_data["code"]
        json_fullname = json_data["fullName"]

        print("="*35)
        console.print(f"     [red]INFORMAÇÕES DO BANCO[/red]")
        print("="*35)
        console.print(f"[green][+] Ispb:[/green] [white]{json_ispb}[/white]\n[green][+] Name:[/green] [white]{json_name}[/white]\n[green][+] Code:[/green] [white]{json_code}[/white]\n[green][+] Full Name:[/green] [white]{json_fullname}[/white]")
        print("="*35)
    
   except:
        console.print("[red][*] Código bancário não encontrado[/red]")


