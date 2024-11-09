async def on_message_event(client, message):
    if message.author == client.user:
        return

    if 'beeil' in message.content or 'mach hinne' in message.content:
        await message.channel.send('Schnauze!')