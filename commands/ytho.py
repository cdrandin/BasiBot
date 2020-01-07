import discord


async def ytho(client, message):
    print("Upload Received")
    try:
        await message.channel.send(file=discord.File('images/ytho.jpg'))
    except Exception as e:
        await message.channel.send("ERROR: %s" % e)
    return
