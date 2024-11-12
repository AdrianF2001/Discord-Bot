import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()


api_url = "https://api.agnai.chat/v1/chat/completions"
api_key = os.getenv("AGNAI_KEY")

conversation_contexts = {}

async def chat_with_agnai(user_id, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    if user_id not in conversation_contexts:
        conversation_contexts[user_id] = [{"role": "system", "content": "You're a friendly human, always willing to help"}]

    conversation_contexts[user_id].append({"role": "user", "content": prompt})

    data = {
        "messages": conversation_contexts[user_id],
        "max_tokens": 400
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                assistant_reply = result['choices'][0]['text'].strip()

                conversation_contexts[user_id].append({"role": "assistant", "content": assistant_reply})

                return assistant_reply
            else:
                error_text = await response.text()
                return f"Fehler bei der Anfrage. Statuscode: {response.status}, Antwort: {error_text}"
