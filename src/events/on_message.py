from utils.agnai_chat import chat_with_agnai

async def on_message_event(client, message):
    if message.author == client.user:
        return

    if 'beeil' in message.content or 'mach hinne' in message.content:
        await message.channel.send('Schnauze!')

    if message.channel.id == 1305918307282714656 or message.channel.id == 1305921951717392497:
        async with message.channel.typing():
            response_text = await chat_with_agnai(message.author.id, message.content)

        await message.channel.send(response_text)

