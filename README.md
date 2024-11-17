# Discord-Bot

## Funktionen
<details>
  <summary><b>Liste der Funktionen</b></summary>

  /commands
  - /initiate_agnai_chat
    - initialisiert den Chat mit einem guten KI-Chat Modell. Hier wird angegeben, wie der Chat auf Nachrichten reagieren soll, wenn also z.B. 'You will constantly curse' angegeben wird, wird der Chat diesen Anforderungen folgen.
    - Nach dem Initialisieren, kann in dem Channel chat-with-bot mit dem geschrieben werden. Es muss kein Command mehr eingegeben werden.
    - Der Chat ist bislang nur bis zum Restart des Bots consistent, d.h. dass der Chat nach dem Neustart wieder initialisiert werden muss.
  - /submit_idea
    - Hier kann eine Idee für die Entwicklung des Bots eingegeben werden, die dann in einem Google Document gespeichert wird.
  - /generate_picture
    - pos_prompt: Hier wird das angegeben, wie das Bild aussehen soll, z.B. 'photorealistic picture of man with a beer in hand'
    - neg_prompt: Hier wird angegeben, was nicht vorhanden sein soll, z.B. 'drawn, unrealistic, low quality'
    - Das Modell ist nicht sonderlich gut, deshalb sehen Bilder gerne etwas kacke aus. Zudem funktioniert es auf englisch am besten.
  - /chat
    - Chat mit KI, wird aber vermutlich entfernt, da /initiate_agnai_chat deutlich besser ist
  - /kacken
    - kacken
  - /roadmap
    - Schickt einen Link, der die Roadmap anzeigt. Also was geplant, was in Arbeit und was fertig ist.

  Funktionen
  - Jede Änderung, die am Bot vorgenommen wird, wird im Channel bot-versionen angezeigt
</details>

## V0.2.4.2
<details>
  <summary><b>Changes</b></summary>

  Frontend
  - Chat und Idee entfernt
    
  Backend
  - dotenv_loader gefixt
</details>


## Frühere Änderungen

<details>
  <summary><b>Versionshistorie</b></summary>

  ## V0.2.4.1
  <details>
    <summary><b>Changes</b></summary>

    Frontend
    - Command /bot_version gegen /roadmap getauscht
    - Chat hat jetzt DEUTLICH bessere KI
      
    Backend
    - Discord ids in .env ausgelagert
    - dotenv_loader erstellt, um Laden der .env Konstanten zu erleichtern
  </details>

  ## V0.2.4
  <details>
    <summary><b>Changes</b></summary>
    
    Frontend
    - KI-Chat muss jetzt mit /initiate_agnai_chat im Channel chat-with-bot initialisiert werden.
    - Beim Initialisieren kann ein system_prompt angegeben werden, was den Chat beeinflusst. Komischer Weise hat er Probleme mit Mütter beleidigen, nicht aber mit Dirty-Talk...
  </details>

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
