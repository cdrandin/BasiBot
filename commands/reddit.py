from utils.get_image import get_image_url


async def hentai(client, message):
    await message.channel.send(get_image_url("hentai"))
    return


async def reddit_random(client, message):
    _ = message.content.split("!random ")

    if len(_) > 1:
        subreddit = _[1]
        await message.channel.send("Result For: {0} \n".format(subreddit) + get_image_url(subreddit))
    else:
        await message.channel.send("Invalid. Usage: `!random <subreddit>`")
    return
