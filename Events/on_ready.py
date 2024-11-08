import discord

async def on_ready_event(client, tree, guild_id):
    print(f'We have logged in as {client.user}')
    await tree.sync(guild=discord.Object(id=guild_id))