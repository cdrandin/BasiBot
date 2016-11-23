from discord.ext import commands
import requests
from get_image import get_image_url


bot = commands.Bot(command_prefix='!', description="Basimot's BasiBot!")


def get_insult():
    r = requests.get("http://www.insultgenerator.org")
    return r.text.split("<div class=\"wrap\">")[1].split("<br><br>")[1].split('</div>')[0].replace('&nbsp', ' ').replace("&#44", "")


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def speaker():
    print("Upload Received")
    try:
        await bot.upload('bad_dps.png')
    except Exception as e:
        await bot.say("ERROR: %s" % e)


@bot.command()
async def hentai():
    await bot.say(get_image_url("hentai"))


@bot.command()
async def smashmouth():
    for x in range(0, 5):
        await bot.say("and they don't stop coming")


@bot.command()
async def random(subreddit: str):
    await bot.say("Result For: {0} \n".format(subreddit) + get_image_url(subreddit))


@bot.command()
async def insult(user: str):
    try:
        print(user)
        if "basibot" in user.lower() or "250739365771214848" in user.lower():
            await bot.say("{0} {1}".format(user, "Damn, you are one sexy bot."))
        elif "brandon" in user.lower() or "basimot" in user.lower() or "102645145815490560" in user.lower() or "reznok" in user.lower() or "monnstermash" in user.lower():
            await bot.say("I would never insult my master.")
        elif "185167277702774794" in user.lower() or "speaker" in user.lower():
            await bot.say("{0} {1} {2}".format(user, get_insult(), "Also, your DPS is terrible."))
        else:
            await bot.say("{0} {1}".format(user, get_insult()))

    except Exception as e:
        await bot.say("ERROR: %s" % e)
        return

bot.run('')