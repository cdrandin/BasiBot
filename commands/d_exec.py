async def d_exec(client, message):
    try:
        r = exec(str(message.content).split("!exec")[1])
        await client.send_message(message.channel, "Success")
        return
    except Exception as e:
        await client.send_message(message.channel, "Error: %s" % e)
    return
