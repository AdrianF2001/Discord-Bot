import discord

async def bot_version(interaction):
    await interaction.response.send_message("https://github.com/AdrianF2001/Discord-Bot")

def add_command(client, tree, guild_id):
    @tree.command(
        name="version",
        description="Version des Bots",
        guild=discord.Object(id=guild_id)
    )
    async def _bot_version(interaction):
        await bot_version(interaction)