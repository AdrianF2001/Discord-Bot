async def on_message_event(client, message):
    if message.author == client.user:
        return

    #if message.content.startswith(('beeil', 'mach hinne')):
    if 'beeil' or 'mach hinne' in message.content:
        await message.channel.send('Schnauze!')