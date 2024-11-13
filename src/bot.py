import discord
from discord import app_commands
from utils.command_loader import load_commands
from utils.event_loader import register_events
from utils.dotenv_loader import get_env_var


TOKEN = get_env_var("DISCORD_TOKEN")

# Test Server
TEST_GUILD_ID  = get_env_var("DISCORD_TEST_GUILD_ID")

# Main Server
MAIN_GUILD_ID  = get_env_var("DISCORD_MAIN_GUILD_ID")

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