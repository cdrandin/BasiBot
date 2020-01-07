import discord


async def speaker(client, message):
    print("Upload Received")
    try:
        await message.channel.send(file=discord.File('images/speaker.png'))
    except Exception as e:
        await message.channel.send("ERROR: %s" % e)
    return
