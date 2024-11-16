import importlib

def load_commands(client, tree, guild_id):
    commands_list = ['command_roadmap', 'command_kacken', 'command_text_to_image', 'command_initiate_agnai_chat']
    for command in commands_list:
        module = importlib.import_module(f'commands.{command}')
        module.add_command(client, tree, guild_id)
