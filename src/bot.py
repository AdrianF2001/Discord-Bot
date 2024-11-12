import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from utils.command_loader import load_commands
from utils.event_loader import register_events

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Test Server
TEST_GUILD_ID  = 1304441601711542343

# Main Server
MAIN_GUILD_ID  = 1304556112984412252

GUILD_IDS = [TEST_GUILD_ID, MAIN_GUILD_ID]

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    for guild_id in GUILD_IDS:
        load_commands(client, tree, guild_id)
        register_events(client, tree, guild_id)
        await tree.sync(guild=discord.Object(id=guild_id))
    print(f'We have logged in as {client.user}')


client.run(TOKEN)