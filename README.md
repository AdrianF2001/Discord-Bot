# Discord-Bot

## V0.2.4
<details>
  <summary><b>Changes</b></summary>
  
  Frontend
  - KI-Chat muss jetzt mit /initiate_agnai_chat im Channel chat-with-bot initialisiert werden.
  - Beim Initialisieren kann ein system_prompt angegeben werden, was den Chat beeinflusst. Komischer Weise hat er Probleme mit Mütter beleidigen, nicht aber mit Dirty-Talk...
</details>


## Frühere Änderungen

<details>
  <summary><b>Versionshistorie</b></summary>

  ## V0.2.3
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - Bot antwortet nun in Channel 'chat-with-bot', es muss kein Command eingegeben werden, damit er antwortet.

    Backend
    - command_loader.py effizienter gemacht.
    - Bugs beim Laden der Commands und Events behoben, welcher es verhindert hat, dass neue Commands angezeigt werden.
    - on_ready.py entfernt
  </details>

  ## V0.2.2
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - Text To Image hinzugefügt. Es kann einmal ein Prompt eingegeben werden und optional ein negativ Prompt.
  </details>

  ## V0.2.1
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - system_prompt zum ChatBot hinzugefügt, funktioniert aber nicht so gut
  </details>


  ## V0.2.0
  <details>
    <summary><b>Changes</b></summary>
  
    Frontend
    - Chatbot hinzugefügt (/chat). Ist eine richtige KI, antwortet also auf alles.
  </details>


  ## V0.1.6
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - on_member_online_event hinzugefügt, was eine Nachricht sendet, wenn ein Mitglied on kommt

    Backend
    - Code modularer gemacht
  </details>

  ## V0.1.5.1
  <details>
    <summary><b>Changes</b></summary>
    
    Backend
    - Code neu organisiert
  </details>


  ## V0.1.5
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - Kleiner Bug-Fix, bei dem Schnauze! immer ausgelöst wurde
    - Command /submit_idea hinzugefügt, um Ideen in ein docs zu schreiben
    
    Backend
    - Utils Folder hinzugefügt
    - command_loader.py erstellt, um Code modularer zu machen
  </details>
  
  ## V0.1.4
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - Webhook für Updates hinzugefügt
    - Kleiner Bug-Fix
  </details>
  
  ## V0.1.3
  <details>
    <summary><b>Changes</b></summary>
    
    Backend
    - .env hinzugefügt, um Token geheim zu halten
  </details>
  
  
  ## V0.1.2
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - Kacken Command hinzugefügt
    - Schnauze!
    
    Backend
    - README formatiert
  </details>
  
  ## V0.1.1
  <details>
    <summary><b>Changes</b></summary>
    
    Backend
    - Kleiner Bug-Fix
  </details>
  
  ## V0.1
  <details>
    <summary><b>Changes</b></summary>
    
    ### Frontend
    - erster Slash-Command hinzugefügt
    
    ### Backend
    - Bot läuft
    - Code aufgeräumt
    - README.md aktualisiert
  </details>
</details>
