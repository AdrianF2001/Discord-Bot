import os
from gradio_client import Client
from discord import app_commands, File
import discord
import asyncio

async def text_to_image(interaction, pos_prompt, neg_prompt=None):
    await interaction.response.defer()
    client = Client("Schlendriano/TextToImage")
    try:
        # Ausführen des blockierenden API-Aufrufs in einem separaten Thread
        result = await asyncio.to_thread(client.predict,
                                         prompt=pos_prompt,
                                         negative_prompt=neg_prompt,
                                         seed=0,
                                         randomize_seed=True,
                                         width=1024,
                                         height=1024,
                                         guidance_scale=0,
                                         num_inference_steps=2,
                                         api_name="/infer"
        )

        if isinstance(result, tuple) and os.path.exists(result[0]):
            image_path = result[0]
            # Senden des Bildes als Datei an Discord
            with open(image_path, 'rb') as image_file:
                await interaction.followup.send(file=File(image_file, filename="generated_image.webp"))
            os.remove(image_path)
        else:
            await interaction.followup.send("Es gab ein Problem beim Abrufen des Bildes.")
    except Exception as e:
        print(f"Fehler: {e}")
        await interaction.followup.send("Es gab ein Problem bei der Antwortgenerierung. Bitte versuche es später erneut.")

def add_command(client, tree, guild_id):
    @tree.command(
        name="generate_picture",
        description="Erzeuge ein Bild",
        guild=discord.Object(id=guild_id)
    )
    @app_commands.describe(
        pos_prompt="Inhalt des Bildes",
        neg_prompt="Optional"
    )
    async def _chat_command(interaction: discord.Interaction, pos_prompt: str, neg_prompt: str = None):
        await text_to_image(interaction, pos_prompt, neg_prompt)
