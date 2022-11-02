import requests 
import json
from rich.console import Console
from time import sleep
console = Console()

def git_dumpp(user):

    try:
      req = requests.get(f"https://api.github.com/users/{user}")
    except KeyError:
        pass
    
    try:
        json_data = req.json()
        login_json = json_data["login"]
        bio_json = json_data["bio"]
        email_json = json_data["email"]
        twitter_json = json_data["twitter_username"]

        loc_json = json_data["location"]
        followers = json_data["followers"]
        following_url = json_data["following"]
        
        console.log("[green][+] Procurando Username...[/green]")
        sleep(1.0)
        print("="*40)
        console.print(f"[red]      GITHUB DE {user}   [/red]")
        print("="*40)  
        console.print(f"[green][+]Login:[/green] {login_json}\n[green][+]Bio:[/green] {bio_json}\n[green][+]Email:[/green] {email_json}\n[green][+]Twitter:[/green] {twitter_json}\n[green][+]Location:[/green] {loc_json}\n[green][+]Seguidores:[/green] {followers}\n[green][+]Seguindo:[/green] {following_url}" )
        print("="*40) 
    except:
        
        console.print("[red][*] Username não encontrado.[/red]")
 

