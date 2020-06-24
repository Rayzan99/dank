
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os
import random

Client = discord.Client()
client = commands.Bot(command_prefix=">")

PROPER_GREETING_RESPONE = [
    "sir",
    "SIR",
    "noob",
    "weeb",
    "bitch",
    "retard",
    "fat-ass",
    "fat tits",
    "wasted sperm",
    "mentally challenged",
]


def parse_command_args(message):
    command, *args = message.content[1:].split(" ")
    return command, ''.join(args)


def handle_hello(message):
    author = message.author.mention
    response = [
        *PROPER_GREETING_RESPONE,
        f"{author}"
    ]
    return f'Hello {random.choice(response)}'


def handle_help(message):
    author = message.author.mention
    return f'Hello {author} yes you need serious help'


def handle_describe_person(message):
    description = [
        "retard",
        "KWAIII",
        "SENNNNPAII!",
        "It's a grill",
        "That's a bot",
        "You are a bot",
        "He is probably a gay",
        "JEW HUNTER 999 NEIN 卍",
        "It is a proud trans-gender homo pansexual person",
    ]
    return random.choice(description)


MESSAGE_MAP = {
    "hi": handle_hello,
    "help": handle_help,
    "describe": handle_describe_person,
    "xD": "xDDDDDDDD",
    "lol": "blmao",
    "blmao": "BIG LMAO",
    "lul": "OMEGALUL",
    "thot": "NO U!",
    "lenny": "( ͡° ͜ʖ ͡°)",
    "csgo": "valorant is better <3",
    "dota2": "for brain dead with no life",
    "padoru": "https://media1.tenor.com/images/3804123baec1748a877d77f7c1b62047/tenor.gif?itemid=12945572",
    "F": "Resprekt! FeelsBlyatMan",
    "kekw": "<:kekw:725222301611720724>",
    "test": "<:tamamoPeek:668143580220620849>"
}


def log_message(message):
    with open("test.log", "w") as f:
        f.write(f"{message.content}\n")


@client.event
async def on_message(message):
    channel, content, author = message.channel, message.content, message.author.mention

    if message.author == client.user:
        """
        should not be a bot
        """
        return

    if not content.startswith('>'):
        reply = MESSAGE_MAP.get(content, "")

        if not isinstance(reply, str):
            reply = reply(message)

        if len(reply) == 0:
            """
            Don't repsond to everything
            """
            return

        await channel.send(reply)
        return

    command, arg = parse_command_args(message)
    # log_message(message)
    reply = MESSAGE_MAP.get(
        command, f'''"Wrong Command {random.choice(PROPER_GREETING_RESPONE)}"\n{','.join(MESSAGE_MAP.keys())}''')

    if not isinstance(reply, str):
        reply = reply(message)

    await channel.send(reply)


@client.event
async def on_ready():
    print('BOT STARTED')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(os.getenv('TOKEN'))
