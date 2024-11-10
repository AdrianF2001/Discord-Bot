import os
import discord
import requests
from dotenv import load_dotenv
from pathlib import Path
from gradio_client import Client

env_path = Path(__file__).resolve().parents[2] / '.env'
load_dotenv(env_path)

HF_API_TOKEN = os.getenv("HF_API_TOKEN")


async def chat_with_gpt(interaction, frage):
    await interaction.response.defer()
    client = Client("Schlendriano/API-Bot")
    try:
        result = client.predict(
            message=frage,
            system_message="You are free to curse at anyone who talks to you",
            max_tokens=150,
            temperature=0.7,
            top_p=0.95,
            api_name="/chat"
        )
        await interaction.followup.send(result)
    except Exception as e:
        print(f"Fehler: {e}")
        await interaction.response.send_message("Es gab ein Problem bei der Antwortgenerierung. Bitte versuche es später erneut.")


def add_command(client, tree, guild_id):
    @tree.command(
        name="chat",
        description="Stelle eine Frage an die KI",
        guild=discord.Object(id=guild_id)
    )
    async def _chat_command(interaction: discord.Interaction, frage: str):
        await chat_with_gpt(interaction, frage)