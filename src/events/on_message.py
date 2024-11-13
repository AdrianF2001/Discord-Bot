from utils.agnai_chat import chat_with_agnai
from commands.command_initiate_agnai_chat import initialized_users
from utils.dotenv_loader import get_env_var

CHANNEL_ID_MAIN = get_env_var("DISCORD_CHANNEL_ID_MAIN")
CHANNEL_ID_TEST = get_env_var("DISCORD_CHANNEL_ID_TEST")

async def on_message_event(client, message):
    if message.author == client.user:
        return

    if 'beeil' in message.content or 'mach hinne' in message.content:
        await message.channel.send('Schnauze!')

    if message.channel.id == CHANNEL_ID_MAIN or message.channel.id == CHANNEL_ID_TEST:
        if message.author.id not in initialized_users:
            await message.channel.send("Bitte initialisiere zuerst den Chat mit `/initiate_agnai_chat`.")
            return
        async with message.channel.typing():
            response_text = await chat_with_agnai(message.author.id, message.content)

        await message.channel.send(response_text)

