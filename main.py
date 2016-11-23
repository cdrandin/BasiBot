from discord.ext import commands
import requests
from get_image import get_image_url


bot = commands.Bot(command_prefix='!', description="Basimot's BasiBot!")


def get_insult():
    r = requests.get("http://www.insultgenerator.org")
    return r.text.split("<div class=\"wrap\">")[1].split("<br><br>")[1].split('</div>')[0]\
        .replace('&nbsp', ' ').replace("&#44", "").replace(";", '')


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
        if any(name for name in ["basibot", "250739365771214848"] if name in user.lower()):
            await bot.say("{0} {1}".format(user, "Damn, you are one sexy bot."))
        elif any(name for name in ["brandon", "basimot", "102645145815490560", "reznok", "monnstermash"]
                 if name in user.lower()):
            await bot.say("I would never insult my master.")
        elif any(name for name in ["185167277702774794", "speaker"] if name in user.lower()):
            await bot.say("{0} {1} {2}".format(user, get_insult(), "Also, your DPS is terrible."))
        else:
            await bot.say("{0} {1}".format(user, get_insult()))

    except Exception as e:
        await bot.say("ERROR: %s" % e)
        return

bot.run('')
