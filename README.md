# Wizard Tower

Un gioco puzzle dove guidi un mago attraverso torri piene di sfide!

---

## **Descrizione**
Wizard Tower è un puzzle game dove il giocatore controlla un mago che deve raccogliere pozioni per sconfiggere mostri e raggiungere il portale di uscita. Il gioco presenta 10 livelli di difficoltà crescente, dall'introduzione fino alle sfide più complesse. Si faccia riferimento al file `progetto.pdf` caricato per le specifiche principali del progetto.

---

## **Requisiti di Sistema**
- Windows 10 o superiore
- Minimo 4GB di RAM
- Risoluzione minima: 1280x720
- Python 3.11 o superiore
- Dipendenze Python:
  - pygame >= 2.6.1
  - opencv-python >= 4.8.0
  - numpy >= 1.24.0

---

## **Installazione**
### Opzione 1: Eseguibile
1. Estrai la cartella ZIP in una posizione a tua scelta.
2. Avvia `WizardTowerSetup.exe`.
3. Avvia l'eseguibile creato

### Opzione 2: Codice sorgente
Non modificare la struttura delle cartelle interne

1. Clona il repository:
   ```bash
   git clone https://github.com/tuousername/wizard_tower.git
   cd wizard_tower
   ```
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
3. Avvia il gioco, spostati nella root e compila con:
   ```bash
   python run.py
   ```

## **Passaggi per generare l'eseguibile**

1. **Assicurati che le dipendenze siano installate:**
   - Esegui il comando nella root del progetto:
     ```bash
     pip install -r requirements.txt
     ```

2. **Controlla che `pyinstaller` sia installato correttamente:**
   - Testa l'installazione con:
     ```bash
     pyinstaller --version
     ```
   - Se non è installato, installalo manualmente:
     ```bash
     pip install pyinstaller
     ```

3. **Usa lo script `build.py` fornito nel progetto:**
   - Nella root del tuo progetto, esegui il file `build.py` che hai già nel progetto:
     ```bash
     python build.py
     ```
   - Puoi trovare il file `WizardTower.exe` in `/build/WizardTower`

   - Questo script utilizza PyInstaller per creare un file `.exe` con le configurazioni necessarie, in /installer 
   come specificato nel comando `create_executable()` all'interno di `build.py`.

   - Per generare l'installer esegui come amministratore il file `buil.bat`.
     Creerá il `WizardTowerInstaller.exe` nella cartella `/installer`

### Supporto per macOS e Linux
Per eseguire il progetto su macOS o Linux, devi creare versioni specifiche per quei sistemi operativi. Ecco come procedere:

## **Per macOS e Linux**
- Usa **PyInstaller** su macOS o Linux per generare un eseguibile nativo per quel sistema operativo.
  - Su **macOS**:
    ```bash
    pyinstaller --onefile --windowed run.py
    ```
  - Su **Linux**:
    ```bash
    pyinstaller --onefile run.py
    ```
  - **Nota**: Puoi eseguire questi comandi direttamente sui rispettivi sistemi operativi o utilizzare una macchina virtuale o Docker.

---

## **Come Giocare**
1. All'avvio viene mostrata un'introduzione animata.
2. Nel menu principale seleziona il livello desiderato.
3. Obiettivi di ogni livello:
   - Raccogli pozioni per sconfiggere i mostri.
   - Sconfiggi tutti i mostri per sbloccare il portale.
   - Raggiungi il portale per completare il livello.

### Controlli:
- **Mouse**: Navigazione menu e interazione con il gioco.
- **M**: Ritorno al menu principale.
- **ESC**: Chiudi il gioco.
- **Slider Volume**: Regolazione audio in-game.

---

## **Risoluzione Problemi**
Se incontri problemi:
1. Verifica che tutte le cartelle siano presenti.
2. Controlla il file di log in `logs/error.log`.
3. Assicurati di avere i permessi di scrittura nella cartella del gioco.

---

## **Struttura del Progetto**
```
wizard_tower/
├── assets/               # File multimediali
│   ├── sprites/          # Sprite del gioco
│   ├── sounds/           # File audio
│   └── ui/               # Elementi dell'interfaccia
├── instances/            # File dei livelli
├── docs/                 # Documentazione
└── src/                  # Codice sorgente
```

---

## **Librerie Utilizzate**
- Python 3.11
- Pygame 2.6.1 - Framework di gioco principale
- OpenCV-Python 4.8.0 - Gestione video e immagini
- NumPy 1.24.0 - Operazioni matematiche e gestione array
- PyInstaller 6.3.0 - Creazione dell'eseguibile

---

## **Note sul Progetto**
### Come vengono letti i file di input:
- Riga: linea del file + 6.
- Colonna: colonna del file + 1 (leggo la lettera a destra del cursore).

### Livelli con posizioni iniziali invalide:
- Livello 4: B.
- Livello 9: C.

### Miglioramenti Proposti:
1. **Schermata di caricamento**:
   - Percentuale con barra di caricamento nella schermata di caricamento livello.
2. **Visualizzazione della mappa**:
   - Mostrare la mappa iniziale in background durante il calcolo o in caso di errore.
3. **Interattività della mappa**:
   - Zoom con la rotellina del mouse.
   - Spostare la mappa trascinandola con il mouse.
4. **Prestazioni**:
   - Parallelizzazione della ricerca su più core.

---

## 💖 Supporta il progetto

Ti piace questo tool? Offrimi un caffè ☕:

[![PayPal](https://img.shields.io/badge/Supporta%20su-PayPal-blue?logo=paypal)](https://paypal.me/PrimeBuildOfficial?country.x=IT&locale.x=it_IT)

---

## **Ringraziamenti Speciali**
- ClaudeAI Free Plan e OpenAI DALL-E Free Plan

---

## **Licenza**
Questo gioco è distribuito sotto la licenza: **Creative Commons - CC BY-NC**. Vedi il file `LICENSE.md` per i dettagli completi.

---

## **Note sulla Versione**
- Versione corrente: 1.0.0
- Data rilascio: 30/11/2024
- Changelog completo disponibile in `CHANGELOG.md`.

---

## **Supporto**
Per segnalare problemi o richiedere supporto:
- Mail: lorenzo.massafra@edu.unife.it

Per bug o problemi tecnici, per favore includi:
- Il file di log (`logs/error.log`).
- Una descrizione dettagliata del problema.
- I passi per riprodurre il problema.
- La versione del gioco che stai usando.

---

### Immagini
![start](https://github.com/user-attachments/assets/7d23f85e-cedd-4ce0-916a-b5a5a8e51eb2)
![Immagine](https://github.com/user-attachments/assets/487e0e71-9439-4d0d-8147-d37c8a5cb2eb)
![Immagine1](https://github.com/user-attachments/assets/6b154df1-5d6d-47c3-9cef-76343ce9de40)
