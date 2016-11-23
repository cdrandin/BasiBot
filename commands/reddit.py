from utils.get_image import get_image_url

async def hentai(client, message):
    await client.send_message(message.channel, get_image_url("hentai"))
    return


async def reddit_random(client, message):
    subreddit = message.content.split("!random ")[1]
    await client.send_message(message.channel, "Result For: {0} \n".format(subreddit) + get_image_url(subreddit))
    return

