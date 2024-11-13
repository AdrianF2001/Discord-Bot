import discord

async def roadmap(interaction):
    await interaction.response.send_message("https://trello.com/b/eucpZkMP/discord-bot-roadmap", ephemeral=True)

def add_command(client, tree, guild_id):
    @tree.command(
        name="roadmap",
        description="Roadmap für den Bot (To-Do, In Arbeit, Fertig implementiert)",
        guild=discord.Object(id=guild_id)
    )
    async def _roadmap(interaction):
        await roadmap(interaction)