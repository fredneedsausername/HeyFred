<div align="center">

  # HeyFred - L'Effimera IA Veloce
  
  **Un'interfaccia chat moderna e veloce per interagire con l'intelligenza artificiale**
  
  **[✨ Features](#features-)** | **[🚀 Installazione](#installazione--linux)** | **[⚙️ Configurazione](#configurazione-%EF%B8%8F)** | **[💻 Utilizzo](#utilizzo-%EF%B8%8F-linux)** | **[🏗️ Architettura](#architettura-%EF%B8%8F)**
  
</div>

---

## 📋 Descrizione

**HeyFred** è un'applicazione web moderna che prioritizza la velocità per chattare con un LLM. Progettata per essere elegante e user-friendly, offre un'esperienza di conversazione fluida con supporto per markdown, syntax highlighting e streaming in tempo reale delle risposte con velocità maggiori rispetto ai principali siti che offrono lo stesso servizio.

## Features ✨

### 💬 Chat Intelligente
- **Streaming in Tempo Reale**: Le risposte dell'IA vengono visualizzate mentre vengono generate
- **Supporto Markdown**: Rendering completo di markdown con syntax highlighting per il codice
- **Gestione Conversazioni**: Sistema di limiti intelligenti per limitare i costi legati a chat lunghe
- **Suggerimenti Rapidi**: Bottoni per iniziare conversazioni su vari argomenti e discipline

### 🎨 Interfaccia Utente
- **Design Moderno**: Interfaccia pulita e minimalista con Tailwind CSS
- **Responsività**: Ottimizzazione per desktop e mobile
- **Animazioni Fluide**: Transizioni e animazioni per un'esperienza utente fluida
- **Tema Elegante**: Combinazione di colori nel codice generato studiata per ridurre l'affaticamento visivo

### ⚡ Performance e Tecnologia
- **WebSocket**: Comunicazione bidirezionale per streaming dei messaggi in tempo reale
- **Asincronicità**: Uso del production server Gevent per performance ottimali
- **Crash Logging**: Sistema di logging della libreria fredcrash per la diagnosi degli errori

### 🔐 Sicurezza e Controllo
- **Autenticazione**: Sistema di login protetto con password
- **Sanitizzazione**: Input sanitizzato con DOMPurify per prevenire XSS

## Installazione 🚀 (linux)

### Setup 

1. **Installa Python 3.13.2**

2. **Clona la repository**:
```bash
git clone https://github.com/fredneedsausername/HeyFred.git
cd HeyFred
```

3. **Crea il virtual environment**
```bash
python -m venv .venv
```

4. **Attiva il virtual environment**
```bash
source .venv/bin/activate
```

5. **Installa le dipendenze**:
```bash
pip install -r requirements.txt
```

## Configurazione ⚙️

### File .env

Crea un file `.env` nella root del progetto e configuralo sulla base di `.env.example`, trovato nel root del progetto.

### Configurazione OpenAI

1. Registrati sulla piattaforma API di OpenAI
2. Crea una nuova API key
3. Assicurati di avere crediti sufficienti per le richieste
4. Inserisci la chiave nel file `.env`

## Utilizzo 🖥️ (linux)

### Avvio dell'Applicazione

**Development**:
```bash
python src/main.py
```

**Production** (con Gunicorn):
```bash
./.venv/bin/gunicorn -c gunicorn.conf.py src.main:app
```

### Interfaccia Utente

#### 🏠 Pagina di Login
- Inserisci la password configurata nel file `.env`
- Il sistema ti reindrizzerà automaticamente alla chat

#### 💬 Interfaccia Chat
- **Area messaggi**: Visualizza la conversazione con scroll automatico
- **Input area**: Textarea che si ridimensiona automaticamente
- **Bottone invio**: Invia messaggi (Enter o click)
- **Suggerimenti**: Bottoni di suggerimento per conversazioni predefinite
- **Indicatori**: Animazioni durante il caricamento della risposta

## Architettura 🏗️

### Stack Tecnologico

**Frontend**:
- **HTMX**: Interattività avanzata senza JavaScript complesso
- **Alpine.js**: Reattività e gestione stato lato client
- **Tailwind CSS**: Classi pre-esistenti per ridurre il CSS
- **WebSocket**: Per lo streaming della chat

**Backend**:
- **Flask**: Framework web backend leggero e flessibile
- **Flask-SocketIO**: Supporto per i WebSocket
- **API OpenAI**: Integrazione con modelli GPT per generazione testo
- **Gevent**: Async I/O per performance ottimali

**Librerie Specializzate**:
- **markdown-it**: Rendering markdown avanzato
- **highlight.js**: Syntax highlighting per codice
- **DOMPurify**: Sanitizzazione HTML per sicurezza

### Architettura del Sistema

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend       │    │   OpenAI API    │
│                 │    │                  │    │                 │
│ • HTMX          │◄──►│ • Flask          │◄──►│ • Modelli GPT   │
│ • Alpine.js     │    │ • SocketIO       │    │ • Streaming     │
│ • Tailwind CSS  │    │ • Gevent         │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

## 🔒 Sicurezza

### Misure Implementate

- **Validazione dell'Input**: Tutti gli input sono validati e sanitizzati
- **Prevenzione da XSS**: DOMPurify previene attacchi cross-site scripting
- **Protezione del CORS**: Origini controllate per richieste cross-origin
- **Privacy delle Key**: Chiavi API protette e non esposte al client

## 📄 Licenza

Questo progetto è rilasciato sotto licenza proprietaria. Vedi il file `LICENSE` nel root del progetto per i dettagli completi.