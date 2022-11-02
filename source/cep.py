
import requests 
import json 
from rich.console import Console 


console = Console()



def get_cep(cep):

    req = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}") 
    json_data = req.json()
    json_cep = json_data["cep"]
    json_state = json_data["state"]
    json_city = json_data["city"]
    json_neighborhood = json_data["neighborhood"]
    json_street = json_data["street"] 
    json_longi = json_data["location"]["coordinates"]["longitude"] 
    json_lati = json_data["location"]["coordinates"]["latitude"] 
    print("="*35)
    console.print(f"    [red]INFORMAÇÕES DO CEP {cep}[/red]")
    print("="*35)
    console.print(f"[green][+] Cep:[/green] [red]{json_cep}[/red]\n[green][+] Estado: [white]{json_state}[/white]\n[green][+] Cidade:[/green] [white]{json_city}[/white]\n[green][+] Bairro:[/green] [white]{json_neighborhood}[/white]\n[green][+] Rua:[/green] [white]{json_street}[/white]\n[green][+] Latitude:[/green] [blue]{json_lati}[/blue]\n[green][+] Longitude:[/green] [blue]{json_longi}[/blue]")
    print("="*35)
