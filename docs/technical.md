# Documentazione Tecnica Wizard Tower

## Architettura del Sistema

### Componenti Principali

1. **Game (main.py)**
   - Gestisce il loop principale del gioco
   - Coordina gli stati e le transizioni
   - Gestisce input utente e rendering

2. **GameStateManager (game_state.py)**
   - Gestisce gli stati del gioco: INTRO, MENU, PLAYING, LEVEL_COMPLETE
   - Mantiene i dati di stato tra le transizioni
   - Coordina il flusso del gioco

3. **LevelVisualizer (level.py)**
   - Rendering dei livelli
   - Gestione animazioni
   - Visualizzazione statistiche in-game

4. **SoundManager (sound.py)**
   - Gestione musica di sottofondo
   - Effetti sonori
   - Controllo volume

5. **SpriteLoader (sprite_loader.py)**
   - Caricamento e gestione sprite
   - Scalatura automatica delle immagini
   - Fallback per asset mancanti

6. **UI (ui.py)**
   - Componenti interfaccia utente riutilizzabili
   - Sistema di pulsanti interattivi
   - Gestione popup e loading bar

### Formato File Livelli
```
[numero_righe]
[numero_colonne]
[numero_pozioni]
[numero_mostri]
[riga_iniziale] [colonna_iniziale]
[griglia]

Legenda griglia:
'B' = Muro
'M' = Pozione
'C' = Mostro
'P' = Portale
' ' = Spazio vuoto
```

## Risoluzioni Supportate
- **Intro**: 500x276 pixel
- **Gioco**: 1280x720 pixel

## Configurazione Audio
- Musica di sottofondo in loop
- Effetti sonori per interazioni UI
- Volume regolabile (0.0 - 1.0)
- Funzione mute

## Performance
- Frame rate bloccato a 60 FPS
- Ottimizzazione sprite con pygame.Surface
- Gestione memoria con pulizia risorse

## Debug e Logging
Il gioco include output di debug per:
- Caricamento livelli
- Movimenti del personaggio
- Transizioni di stato
- Errori di caricamento risorse
