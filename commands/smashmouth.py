import asyncio


async def smashmouth(client, message):
    for x in range(0, 5):
        await message.channel.send("and they don't stop coming")
        await asyncio.sleep(1)
    return
