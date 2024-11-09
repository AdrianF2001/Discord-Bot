import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from events.on_message import on_message_event
from events.on_ready import on_ready_event
from commands import load_commands

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Test Server
# GUILD_ID = 1304441601711542343

# Main Server
GUILD_ID = 1304556112984412252

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Events und Befehle importieren und anwenden
@client.event
async def on_ready():
    await on_ready_event(client, tree, GUILD_ID)

@client.event
async def on_message(message):
    await on_message_event(client, message)

# Slash-Commands laden
load_commands(client, tree, GUILD_ID)

client.run(TOKEN)