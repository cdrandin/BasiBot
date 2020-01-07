async def d_exec(client, message):
    try:
        r = exec(str(message.content).split("!exec")[1])
        await client.send(message.channel, "Success")
        return
    except Exception as e:
        await client.send(message.channel, "Error: %s" % e)
    return
