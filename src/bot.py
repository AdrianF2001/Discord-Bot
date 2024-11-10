import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from utils.command_loader import load_commands
from utils.event_loader import register_events

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Test Server
GUILD_ID = 1304441601711542343

# Main Server
# GUILD_ID = 1304556112984412252

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# Events und Befehle importieren und anwenden
register_events(client, tree, GUILD_ID)

# Slash-Commands laden
load_commands(client, tree, GUILD_ID)

client.run(TOKEN)