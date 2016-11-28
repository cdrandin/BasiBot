async def ytho(client, message):
    print("Upload Received")
    try:
        await client.send_file(message.channel, "images/ytho.jpg")
    except Exception as e:
        await client.send_message(message.channel, "ERROR: %s" % e)
    return
