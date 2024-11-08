import discord
from Events import on_ready, on_message

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Events aus den Event-Dateien registrieren
on_ready.register_event(client)
on_message.register_event(client)

client.run('MTMwNDQ0MDY0MTgxMTY0ODU2Mg.GWCPEC.aXJPgOe9-n53OFg7L-ymOFYkpd1zKMTnXM2HHg')