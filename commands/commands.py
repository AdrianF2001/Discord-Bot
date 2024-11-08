import discord

async def first_command(interaction):
    await interaction.response.send_message("https://github.com/AdrianF2001/Discord-Bot")

def add_command(client, tree, guild_id):
    @tree.command(
        name="version",
        description="Version des Bots",
        guild=discord.Object(id=guild_id)
    )
    async def _first_command(interaction):
        await first_command(interaction)