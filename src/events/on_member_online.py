import discord

async def on_member_update_event(before: discord.Member, after: discord.Member):
    if before.status != discord.Status.online and after.status == discord.Status.online:
        channel = after.guild.system_channel
        if channel:
            await channel.send(f'{after.mention} ist jetzt online')