import colorama
import os
import json
import requests
import uuid
from colorama import Fore, Style
colorama.init()
os.system("cls")
def get_hwid():
    hwid = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return hwid
def check():
    site = requests.get('example.com') # your website
    hwid = get_hwid()
    try:
        if hwid in site.text:
            # Find the line containing the HWID
            for line in site.text.split('\n'):
                if hwid in line:
                    # Split the line by colon to extract details
                    parts = line.split(':')
                    name = parts[1] if len(parts) > 1 else 'Unknown'# if name does not exist set as Unknown
                    details = parts[2:] if len(parts) > 2 else [] # set as none
                    print(f"        {Fore.LIGHTYELLOW_EX}> {Fore.GREEN}You logged as {Fore.LIGHTRED_EX}{name}")
                    
                    print(Fore.LIGHTCYAN_EX + f"""|                   HWID                  |        Name        |        Details      |     
| {hwid} |   {name}   | {details}""")
                    break
        else:
            print('[ERROR] HWID NOT in database')
            print('[HWID: ' + hwid + ']')
    except Exception as e:
        print('[ERROR] FAILED to connect to database')
        print(hwid)
        print(f"Exception: {e}")
banner = f"""
{Fore.LIGHTGREEN_EX}
        ██╗  ██╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ███╗   ██╗
        ██║ ██╔╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗████╗  ██║
        █████╔╝ ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██╔██╗ ██║
        ██╔═██╗ ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║
        ██║  ██╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║ ╚████║
        ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝
                                              {Fore.LIGHTBLACK_EX}- {Fore.LIGHTBLUE_EX}github.com/iAlperenS
"""
def log(text, d):
    if d == "i":
        input(Fore.LIGHTBLACK_EX + "> " + Fore.MAGENTA + text)
    elif d == "p":
        print(Fore.LIGHTBLACK_EX + "> " + Fore.MAGENTA + text)
print(banner)
check()
data = input(Fore.LIGHTYELLOW_EX + "      > " + Fore.GREEN + "Start Client " + Fore.LIGHTYELLOW_EX)
def update_hwid_status():
    url = 'http://localhost:5000/set_hwid_status' # your server - i am using localhost (my pc)
    response = requests.post(url)
    print(response.json())
update_hwid_status()
input("You can close this tab but dont close Server...")
