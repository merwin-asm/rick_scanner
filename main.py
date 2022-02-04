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

cli = discord.Client()

@cli.event
async def on_message(message):
    if message.author != cli.user:
        msg = str(message.content)
        if msg.startswith("$rickscan"):
            link = msg.split("$rickscan")[1]
            res = scan(link)
            if res:
                text = "There are chances u get rick rolled..."
            else:
                text = "Its safe..."
            await message.channel.send(text)
cli.run(TOKEN)
