import requests 
from time import sleep 

import threading
from rich.console import Console
user_num = 0 
user_working = 0 
user_results = []
headers = {"User-Agent":"Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.334; U; id) Presto/2.5.25 Version/10.54"}
console = Console()




def send_req(url,username): 

    try:
        req = requests.get(url.format(username),headers=headers)
    except requests.exceptions.Timeout:
        pass
    except requests.exceptions.TooManyRedirects:
        pass
    except requests.exceptions.ConnectionError:
        pass 

    try:
        global user_num,user_results,user_working 
        
        user_num += 1

        if req.status_code == 200: 
            user_working += 1 
           

        elif req.status_code == 404:
            pass 

        else:
            pass

        user_results.append(f"{req.status_code} {user_num}/88 {url.format(username)}")

    except:
        pass
 
 
 

def userrecon(username):
    global user_results,user_num,user_working
    
    console.print("[green][+] Procurando Informações do Username...[/green]")
    sleep(0.13)
    urllist = [
        "https://facebook.com/{}",
        "https://instagram.com/{}",
        "https://twitter.com/{}",
        "https://www.youtube.com/results?search_query={}",
        "https://vimeo.com/{}",
        "https://github.com/{}",
        "https://plus.google.com/{}",
        "https://pinterest.com/{}",
        "https://flickr.com/people/{}",
        "https://vk.com/{}",
        "https://about.me/{}",
        "https://disqus.com/{}",
        "https://bitbucket.org/{}",
        "https://flipboard.com/@{}",
        "https://medium.com/@{}",
        "https://hackerone.com/{}",
        "https://keybase.io/{}",
        "https://buzzfeed.com/{}",
        "https://slideshare.net/{}",
        "https://mixcloud.com/{}",
        "https://soundcloud.com/{}",
        "https://badoo.com/en/{}",
        "https://imgur.com/user/{}",
        "https://open.spotify.com/user/{}",
        "https://pastebin.com/u/{}",
        "https://wattpad.com/user/{}",
        "https://canva.com/{}",
        "https://codecademy.com/{}",
        "https://last.fm/user/{}",
        "https://blip.fm/{}",
        "https://dribbble.com/{}",
        "https://en.gravatar.com/{}",
        "https://foursquare.com/{}",
        "https://creativemarket.com/{}",
        "https://ello.co/{}",
        "https://cash.me/{}",
        "https://angel.co/{}",
        "https://500px.com/{}",
        "https://houzz.com/user/{}",
        "https://tripadvisor.com/members/{}",
        "https://kongregate.com/accounts/{}",
        "https://{}.blogspot.com/",
        "https://{}.tumblr.com/",
        "https://{}.wordpress.com/",
        "https://{}.devianart.com/",
        "https://{}.slack.com/",
        "https://{}.livejournal.com/",
        "https://{}.newgrounds.com/",
        "https://{}.hubpages.com",
        "https://{}.contently.com",
        "https://steamcommunity.com/id/{}",
        "https://www.wikipedia.org/wiki/User:{}",
        "https://www.freelancer.com/u/{}",
        "https://www.dailymotion.com/{}",
        "https://www.etsy.com/shop/{}",
        "https://www.scribd.com/{}",
        "https://www.patreon.com/{}",
        "https://www.behance.net/{}",
        "https://www.goodreads.com/{}",
        "https://www.gumroad.com/{}",
        "https://www.instructables.com/member/{}",
        "https://www.codementor.io/{}",
        "https://www.reverbnation.com/{}",
        "https://www.designspiration.net/{}",
        "https://www.bandcamp.com/{}",
        "https://www.colourlovers.com/love/{}",
        "https://www.ifttt.com/p/{}",
        "https://www.trakt.tv/users/{}",
        "https://www.okcupid.com/profile/{}",
        "https://www.trip.skyscanner.com/user/{}",
        "http://www.zone-h.org/archive/notifier={}",
        "https://www.anime-planet.com/users/{}",
        "https://www.duolingo.com/2017-06-30/users?username={}&_=1628308619574",
        "https://ebay.com/usr/{}",
        "https://onlyfans.com/{}",
        "https://psnprofiles.com/{}",
        "https://www.pornhub.com/users/{}",
        "https://reddit.com/user/{}",
        "https://roblox.com/user.aspx?username={}",
        "https://rumble.com/user/{}",
        "https://feelinsonice.appspot.com/web/deeplink/snapcode?username={}&size=400&type=SVG",
        "https://t.me/{}",
        "https://tiktok.com/@{}",
        "https://tinder.com/@{}",
        "https://twitch.tv/{}",
        "https://www.xvideos.com/profiles/{}",
        "https://profiles.wordpress.org/{}/",
        "https://www.xboxgamertag.com/search/{}"
    ]
     
    for url in urllist:
        threading.Thread(target=send_req,args=(url,username)).start()
    while True:

      if user_num == len(urllist):
        break 
    print()
    print("="*40)
    console.print(f"[red]    REDES SOCIAIS DE {username}   [/red]")
    print("="*40)
    for user in user_results: 
        
        print(user)
    console.print("[red]=[/red]"*45)
