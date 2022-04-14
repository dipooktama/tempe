import discord
import os
from dotenv import load_dotenv
import json
import random

load_dotenv()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(os.getenv('DISCORD_TOKEN'))
#client.run('OTY0MTgwODQ0MTQ1MTcyNTEx.Ylg5Yg.LTure-kgNxHLskZWgTwX_Hkal_4')