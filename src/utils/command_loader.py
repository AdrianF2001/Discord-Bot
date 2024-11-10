from commands.command_bot_version import add_command as add_version_command
from commands.command_add_idea import add_command as add_submit_idea_command
from commands.command_kacken import add_command as add_kacken_command
from commands.command_ai_chat import add_command as add_chat_command

def load_commands(client, tree, guild_id):
    add_version_command(client, tree, guild_id)
    add_submit_idea_command(client, tree, guild_id)
    add_kacken_command(client, tree, guild_id)
    add_chat_command(client, tree, guild_id)
    
