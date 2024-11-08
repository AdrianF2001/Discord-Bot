import discord

async def on_message(message):
    if message.author == discord.Client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    

def register_event(client):
    client.event(on_message)  # Event direkt registrieren
