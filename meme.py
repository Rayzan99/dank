
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix = ">")

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('>help'):
        msg = '''Hello {0.author.mention} yes you need help'''.format(message)
        await client.send_message(message.channel, msg)
        return

    if message.content == ">join":
        await client.send_message(message.channel, "I wont lmao")
        return
    
    if message.content == ">play":
        await client.send_message(message.channel, "Bruhhh internet is runing at like Bytes xD cant do that shit rn.")
        return
    
    if message.content == ">stop":
        await client.send_message(message.channel, "Cant stop wont stop.")
        return
    
    if message.content == "xD":
        await client.send_message(message.channel, "xDDDDDDDD")
        return
    
    if message.content == "lol":
        await client.send_message(message.channel, "blmao")
        return
    
    if message.content == "blmao":
        await client.send_message(message.channel, "BIG LMAO")
        return
    
    if message.content == "lmao"":
        await client.send_message(message.channel, "LOLOLOLOLOL")
        return
    
    if message.content == "lul":
        await client.send_message(message.channel, "OMEGALUL")
        return
    
    if message.content == "thot":
        await client.send_message(message.channel, "NO U!")
        return
    
    if message.content == "fak":
        await client.send_message(message.channel, "Yu")
    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(os.getenv('TOKEN'))
