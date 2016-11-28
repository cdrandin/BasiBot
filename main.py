import discord
import json

# Commands #
from commands.insult import insult
from commands.smashmouth import smashmouth
from commands.reddit import hentai, reddit_random
from commands.speaker import speaker
from commands.ytho import ytho
from commands.wclogs_rankings import wclogs_rankings


config = json.loads(open('config.json').read())  # Load Configs
client = discord.Client()


def is_admin(author):
    """
    Is this user a bot admin?
    :param author: message.author
    :return: bool
    """
    if str(author).lower() in config["admins"]:
        return True
    return False


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if "www.warcraftlogs.com/" in message.content and "view=rankings" in message.content:
        print(str(message.author))
        await wclogs_rankings(client, message)

    if message.content.startswith('!insult'):
        print(str(message.author))
        await insult(client, message)

    # if message.content.startswith('!smashmouth'):
    #     print(str(message.author))
    #     await smashmouth(client, message)

    if message.content.startswith('!hentai'):
        print(str(message.author))
        await hentai(client, message)

    if message.content.startswith('!random'):
        print(str(message.author))
        await reddit_random(client, message)

    if message.content.startswith('!speaker'):
        print(str(message.author))
        await speaker(client, message)
    if message.content.startswith('!ytho'):
        print(str(message.author))
        await ytho(client, message)

    if message.content.startswith('!admin'):
        print(str(message.author))
        if is_admin(message.author):
            await client.send_message(message.channel, "You Are An Admin")
        else:
            await client.send_message(message.channel, "You Are Not An Admin")

client.run(config["token"])
