import requests

banned_names = ["brandon", "brand0n", "b-randon", "br-andon", "bra-ndon", "bran-don", "brand-on", "brando-n",
                "br@nd0n", "br@andon", "basimot", "102645145815490560", "reznok", "monnstermash"]

def get_insult():
    r = requests.get("http://www.insultgenerator.org")
    return r.text.split("<div class=\"wrap\">")[1].split("<br><br>")[1].split('</div>')[0]\
        .replace('&nbsp', ' ').replace("&#44", "").replace(";", '')

async def insult(client, message):
    print(message.content)
    target = message.content.split("!insult ")[1]

    try:
        if any(name for name in ["basibot", "250739365771214848"] if name in target.lower()):
            await client.send_message(message.channel, "{0} {1}".format(target, "Damn, you are one sexy bot."))
            return

        elif any(name for name in banned_names
                 if name in target.lower()):
            await client.send_message(message.channel, "I would never insult my master.")
            return

        elif any(name for name in ["185167277702774794", "speaker"] if name in target.lower()):
            await client.send_message(message.channel, "{0} {1} {2}".format(target, get_insult(), "Also, your DPS is terrible."))
            return

        else:
            await client.send_message(message.channel, "{0} {1}".format(target, get_insult()))
            return

    except Exception as e:
        await client.send_message(message.channel, "ERROR: %s" % e)
        return
