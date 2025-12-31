# Applicazione Flask Base

Questo piccolo repository dimostra una struttura di file appropriata per un'applicazione Flask. Le cartelle denominate *static* e *templates* sono obbligatorie.

**Le route** e i **file statici** sono gestiti correttamente in tutti gli attributi `src` e `href` nei file template.

## Requisiti

Installa tutte le dipendenze necessarie:

```bash
pip install -r requirements.txt
```

## Esecuzione dell'Applicazione

### Server Flask

Dopo aver installato tutte le dipendenze, esegui l'applicazione entrando nella sua cartella e digitando:

```bash
python routes.py <numero-porta>
```

### Esecuzione di Server Multipli

Per rendere eseguibile lo script:

```bash
chmod +x kill_process.sh
```

Esegui server Flask multipli:

```bash
sh run.sh
```

Attualmente, questo comando avvierà quattro server Flask sulle porte da 5001 a 5003.

### Server Tornado

È disponibile anche un server Tornado alternativo:

```bash
python tornado_server.py --port=<numero-porta>
```

## Terminare i Server

Per terminare tutti i server Flask in esecuzione:

```bash
./kill_process.sh
```

Questo script terminerà tutti i server Flask avviati.

## Struttura del Progetto

```
basic-flask-app-ss/
├── routes.py           # File principale dell'applicazione Flask
├── tornado_server.py   # Server alternativo basato su Tornado
├── requirements.txt    # Dipendenze Python
├── run.sh             # Script per eseguire server multipli
├── kill_process.sh    # Script per terminare i server
├── static/            # File CSS, JS e immagini
├── templates/         # Template HTML
└── uploads/           # Cartella per i file caricati
```

## Funzionalità

### Applicazione Flask (routes.py)
- **Pagina principale** (`/` o `/index.html`): Pagina iniziale dell'applicazione
- **Pagina simbolo** (`/symbol.html`): Informazioni sulla tigre come simbolo
- **Pagina mito** (`/myth.html`): La tigre nel mito e nella leggenda

### Server Tornado (tornado_server.py)
- **Endpoint principale** (`/`): Messaggio di benvenuto
- **Upload di file** (`/upload`): Funzionalità di caricamento file tramite richieste POST

## Nota sulla Sicurezza

Questo progetto utilizza versioni obsolete di Flask e altre dipendenze. Per ambienti di produzione, si consiglia di aggiornare tutte le dipendenze alle versioni più recenti per garantire la sicurezza.
