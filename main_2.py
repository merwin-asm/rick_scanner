import discord
import requests
import re
import os


TOKEN = os.environ['Token']


def req(link):
    x = requests.get(link)
    return x.text

def scan(link):
    file = req(link).lower()
    pattern = "rick"
    if re.search(pattern,file):
        return True
    else:
        return False

def get_link(msg):
    msg = str(msg)
    try:
        msg = msg.split("http")[1]
        link = "http"+msg
        try:
            link_ = link.split(" ")[0]
        except:
            link_ = link
        return link_
    except:
        return False

cli = discord.Client()

@cli.event
async def on_message(message):
    if message.author != cli.user:
        msg = str(message.content)
        link = get_link(msg)
        if link != False:
            if scan(link):
                await message.channel.send("")
cli.run(TOKEN)
