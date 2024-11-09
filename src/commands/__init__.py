from pathlib import Path

def load_commands(client, tree, guild_id):
    # Durchsuche das commands-Verzeichnis nach Python-Dateien
    command_files = Path(__file__).parent.glob("*.py")

    for file in command_files:
        # Nur Python-Dateien ohne "__init__.py"
        if file.name != "__init__.py":
            module_name = file.stem
            module = __import__(f"commands.{module_name}", fromlist=[module_name])

            # Prüfe, ob die Funktion für den Command vorhanden ist
            if hasattr(module, 'add_command'):
                # Füge den Command zur CommandTree hinzu
                module.add_command(client, tree, guild_id)
