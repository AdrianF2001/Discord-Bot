import discord

async def on_ready():
    print(f'We have logged in as {discord.Client.user}')

def register_event(client):
    client.event(on_ready)  # Event direkt registrieren
