import requests 
import json 
from rich.console import Console 

console = Console()



def get_ip(ip): 

   try:
        req = requests.get(f"http://ip-api.com/json/{ip}")
        json_data = req.json()
        json_status = json_data["status"]
        json_country = json_data["country"]
        json_countryCode = json_data["countryCode"]
        json_regionName = json_data["regionName"]
        json_city = json_data["city"]
        json_lat = json_data["lat"]
        json_lon = json_data["lon"]
        json_timezone = json_data["timezone"]
        json_isp = json_data["isp"]
        json_as = json_data["as"]
        print("="*35)
        console.print(f"   [red]INFORMAÇÕES DO IP {ip}[/red]")
        print("="*35)
        console.print(f"[green][+] Status:[/green] [white]{json_status}[/white]\n[green][+] Country:[/green] [white]{json_country}[/white]\n[green][+] Country Name:[/green] [white]{json_countryCode}[white]\n[green][+] Região:[/green] [white]{json_regionName}[/white]\n[green][+] Cidade:[/green] [white]{json_city}[/white]\n[green][+] Latitude:[/green] [blue]{json_lat}[/blue]\n[green][+] Longitude:[/green] [blue]{json_lon}[/blue]\n[green][+] TimeZone:[/green] [white]{json_timezone}[/white]\n[green][+] ISP:[/green] [white]{json_isp}[/white]\n[green][+] AS:[/green] [white]{json_as}[/white]")
        print("="*35)
   except:
       console.print("[red][*] ERRO IP NÂO ENCONTRADO[/red]")




