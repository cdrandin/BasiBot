import json
# Commands #
from commands.insult import insult
from commands.reddit import hentai, reddit_random
from commands.smashmouth import smashmouth
from commands.speaker import speaker
from commands.ytho import ytho

import discord

# from commands.wclogs_rankings import wclogs_rankings
# from commands.d_exec import d_exec
# from commands.pug import pug


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
    # if "www.warcraftlogs.com/" in message.content and "view=rankings" in message.content:
    #     print(str(message.author))
    #     await wclogs_rankings(client, message)

    elif message.content.startswith('!insult'):
        print(str(message.author))
        await insult(client, message)

    elif message.content.startswith('!smashmouth'):
        print(str(message.author))
        await smashmouth(client, message)

    elif message.content.startswith('!hentai'):
        print(str(message.author))
        await hentai(client, message)

    elif message.content.startswith('!random'):
        print(str(message.author))
        await reddit_random(client, message)

    elif message.content.startswith('!speaker'):
        print(str(message.author))
        await speaker(client, message)

    elif message.content.startswith('!ytho'):
        print(str(message.author))
        await ytho(client, message)

    # elif message.content.startswith('!pug'):
    #     print(str(message.author))
    #     await pug(client, message)

    # elif message.content.startswith('!exec') and is_admin(message.author):
    #     print(str(message.author))
    # elif    await d_exec(client, message)

    elif message.content.startswith('!admin'):
        print(str(message.author))
        if is_admin(message.author):
            await client.send(message.channel, "You Are An Admin")
        else:
            await client.send(message.channel, "You Are Not An Admin")

client.run(config["token"])
