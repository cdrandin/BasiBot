import discord
import json

### Commands ###
from commands.insult import insult
from commands.smashmouth import smashmouth
from commands.reddit import hentai, reddit_random
from commands.speaker import speaker


config = json.loads(open('config.json').read())  # Load Configs, primarily token
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!insult'):
        await insult(client, message)

    if message.content.startswith('!smashmouth'):
        await smashmouth(client, message)

    if message.content.startswith('!hentai'):
        await hentai(client, message)

    if message.content.startswith('!random'):
        await reddit_random(client, message)

    if message.content.startswith('!speaker'):
        await speaker(client, message)

client.run(config["token"])
