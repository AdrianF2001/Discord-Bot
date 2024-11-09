from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import os
import pickle

# Anwendungsbereich festlegen
SCOPES = ['https://www.googleapis.com/auth/documents']

# Funktion zur Authentifizierung mit OAuth 2.0
def authenticate_with_oauth():
    creds = None
    # Überprüfen, ob vorherige Anmeldedaten vorhanden sind
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # Wenn keine gültigen Anmeldedaten vorhanden sind, Authentifizierungsprozess starten
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'files/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Speichern der Anmeldedaten für zukünftige Verwendung
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds

def append_text_to_doc(document_id, text):
    try:
        creds = authenticate_with_oauth()
        service = build('docs', 'v1', credentials=creds)
        requests = [
            {
                'insertText': {
                    'location': {
                        'index': 1,
                    },
                    'text': text + '\n'
                }
            }
        ]
        service.documents().batchUpdate(documentId=document_id, body={'requests': requests}).execute()
        print("Text erfolgreich hinzugefügt.")
    except Exception as e:
        print(f"Fehler beim Hinzufügen des Textes: {e}")
