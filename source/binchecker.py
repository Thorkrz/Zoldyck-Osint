from webbrowser import get
import requests 
import json 
from rich.console import Console

console = Console()



def get_bin(bin): 
  
  try:
        req = requests.get(f"https://bin-check-dr4g.herokuapp.com/api/{bin}") 
        json_data = req.json()
        json_result = json_data["result"]
        json_message = json_data["message"]
        json_bin = json_data["data"]["bin"]
        json_vendor = json_data["data"]["vendor"]
        json_type = json_data["data"]["type"]
        json_level = json_data["data"]["level"]
        json_bank = json_data["data"]["bank"]
        json_country = json_data["data"]["country"]
        json_countryinfo = json_data["data"]["countryInfo"]["name"]
        json_code = json_data["data"]["countryInfo"]["code"]
        json_dialCode = json_data["data"]["countryInfo"]["dialCode"]

        print("="*35)
        console.print(f"     [red]INFORMAÇÕES DO CARTÃO[/red]")
        print("="*35)
        console.print(f"[green][+] Result:[/green] {json_result}\n[green][+] MESSAGE:[/green] {json_message}\n[green][+] Bin:[/green] [blue]{json_bin}[/blue]\n[green][+] Vendor:[/green] {json_vendor}\n[green][+] Type Card:[/green] {json_type}\n[green][+] Level:[/green] {json_level}\n[green][+] Bank:[/green] {json_bank}\n[green][+] Country:[/green] {json_country}\n[green][+] Name:[/green] {json_countryinfo}\n[green][+] Code:[/green] {json_code}\n[green][+] DD:[/green] [blue]{json_dialCode}[/blue]")
        print("="*35)
  except:
        console.print("[red][*] ERROR BIN INVÁLIDO[/red]")
  


