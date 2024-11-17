import os
from dotenv import load_dotenv

load_dotenv(override=True)

def get_env_var(var_name, default=None):
    """
    Lädt eine Umgebungsvariable, konvertiert sie automatisch in einen Integer,
    falls möglich. Falls die Variable nicht existiert, wird ein Standardwert zurückgegeben.
    """
    value = os.getenv(var_name, default)
    try:
        # Versucht, den Wert in einen Integer zu konvertieren
        return int(value)
    except (TypeError, ValueError):
        # Wenn der Wert kein Integer ist, wird der String zurückgegeben
        return value