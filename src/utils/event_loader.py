from discord import Client

from events.on_message import on_message_event
from events.on_member_online import on_member_update_event

def register_events(client: Client, tree, guild_id):

    @client.event
    async def on_message(message):
        await on_message_event(client, message)

    @client.event
    async def on_member_update(before, after):
        await on_member_update_event(before, after)