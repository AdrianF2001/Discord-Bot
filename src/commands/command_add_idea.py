import discord
from google_api import append_text_to_doc

DOCUMENT_ID = '1SMmN9cAT1JkTojYBjVOVxG-Cje4obCFvJUZChb3x3aA'

async def submit_idea(interaction, idea_text):
    try:
        append_text_to_doc(DOCUMENT_ID, idea_text)
        await interaction.response.send_message("Deine Idee wurde erfolgreich gesendet!")
    except Exception as e:
        await interaction.response.send_message(f"Fehler beim Senden deiner Idee: {str(e)}")

def add_command(client, tree, guild_id):
    @tree.command(
        name="submit_idea",
        description="Sende eine Idee an das Google Docs-Dokument",
        guild=discord.Object(id=guild_id)
    )
    async def _submit_idea(interaction, idea: str):
        await submit_idea(interaction, idea)
