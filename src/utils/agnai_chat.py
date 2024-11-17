import aiohttp
from utils.dotenv_loader import get_env_var


api_url = "https://api.agnai.chat/v1/chat/completions"
api_key = get_env_var("AGNAI_KEY")
conversation_contexts = {}

async def chat_with_agnai(user_id, prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
    }

    if user_id not in conversation_contexts:
        return "Chat nicht initialisiert. Bitte initialisiere zuerst den Chat."

    conversation_contexts[user_id].append({"role": "user", "content": prompt})

    data = {
        "messages": conversation_contexts[user_id],
        "max_tokens": 400
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(api_url, headers=headers, json=data) as response:
            if response.status == 200:
                result = await response.json()
                assistant_reply = f"<@{user_id}> {result['choices'][0]['text'].strip()}"
                conversation_contexts[user_id].append({"role": "assistant", "content": assistant_reply})
                return assistant_reply
            else:
                error_text = await response.text()
                return f"Fehler bei der Anfrage. Statuscode: {response.status}, Antwort: {error_text}"