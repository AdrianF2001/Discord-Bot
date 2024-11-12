import importlib

def load_commands(client, tree, guild_id):
    commands_list = ['command_bot_version', 'command_add_idea', 'command_kacken', 'command_ai_chat', 'command_text_to_image']
    for command in commands_list:
        module = importlib.import_module(f'commands.{command}')
        module.add_command(client, tree, guild_id)
