import requests
from bs4 import BeautifulSoup
banned_names = ["brandon", "brand0n", "b-randon", "br-andon", "bra-ndon", "bran-don", "brand-on", "brando-n",
                "br@nd0n", "br@andon", "basimot", "102645145815490560", "reznok", "monnstermash"]


def get_insult():
    r = requests.get("http://www.robietherobot.com/insult-generator.htm")
    soup = BeautifulSoup(r.text)
    return ' '.join(soup.form.table.h1.text.strip().split())


async def insult(client, message):
    print(message.content)
    _ = message.content.split("!insult ")

    if len(_) <= 1:
        await message.channel.send("Invalid. Usage: `!insult @<username>`")
        return

    target = _[1]

    try:
        if any(name for name in ["basibot", "250739365771214848"] if name in target.lower()):
            await message.channel.send("{0} {1}".format(target, "Damn, you are one sexy bot."))
            return

        elif any(name for name in banned_names
                 if name in target.lower()):
            await message.channel.send("I would never insult my master.")
            return

        elif any(name for name in ["185167277702774794", "speaker"] if name in target.lower()):
            await message.channel.send("{0} {1} {2}".format(target, get_insult(), "Also, your DPS is terrible."))
            return
        else:
            await message.channel.send("{0} {1}".format(target, get_insult()))
            return

    except Exception as e:
        await message.channel.send("ERROR: %s" % e)
        return
