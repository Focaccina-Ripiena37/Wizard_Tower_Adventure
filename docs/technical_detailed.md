# Documentazione Tecnica Dettagliata - Wizard Tower

## Dipendenze

### Pygame (>= 2.6.1)
- **Utilizzo**: Framework principale per il rendering grafico e la gestione degli input
- **Componenti chiave utilizzati**:
  - `pygame.Surface`: Per la gestione delle superfici di rendering
  - `pygame.mixer`: Gestione audio multicanale
  - `pygame.font`: Rendering del testo
  - `pygame.event`: Gestione input utente
- **Motivazione**: Scelto per la sua semplicità di utilizzo e le ottime performance nel 2D

### OpenCV (cv2)
- **Utilizzo**: Gestione e riproduzione dei video di introduzione
- **Componenti chiave**:
  - `cv2.VideoCapture`: Lettura dei frame video
  - `cv2.cvtColor`: Conversione spazi colore (BGR -> RGB)
- **Motivazione**: Necessario per la riproduzione fluida dei video intro

### NumPy
- **Utilizzo**: Manipolazione efficiente degli array per video e immagini
- **Componenti chiave**:
  - `numpy.array`: Conversione frame video
  - `numpy.ndarray`: Manipolazione matriciale per la griglia di gioco
- **Motivazione**: Ottimizzazione performance nella gestione video e griglia

## Algoritmo di Pathfinding

### A* Search Implementation
```python
class WizardTowerSolver:
    def solve(self):
        # Implementazione A* con ottimizzazioni specifiche:
        # 1. Cycle detection per evitare loop
        # 2. Timeout per livelli complessi
        # 3. Euristica Manhattan Distance
        # 4. Ottimizzazione raccolta pozioni
```

### Logica di Risoluzione
1. **Fase di Pianificazione**
   - Ricerca pozione più vicina
   - Pianificazione percorso verso il mostro più vicino
   - Ottimizzazione finale verso il portale

2. **Gestione Stati**
   - Tracciamento pozioni raccolte
   - Monitoraggio mostri sconfitti
   - Verifica condizioni portale

3. **Ottimizzazioni**
   - Cache dei percorsi calcolati
   - Prevenzione cicli infiniti
   - Gestione timeout per livelli complessi

## Sistema di Rendering

### Gestione Sprite (sprite_loader.py)
```python
class SpriteLoader:
    def __init__(self):
        # Caricamento lazy degli sprite
        # Conversione automatica formato
        # Gestione cache per performance
```

- **Funzionalità chiave**:
  1. Caricamento automatico sprite
  2. Scalatura proporzionale
  3. Fallback per asset mancanti
  4. Cache per ottimizzare memoria

### Visualizzazione Livello (level.py)

#### Sistema di Coordinate
- Conversione grid-to-screen:
  ```python
  screen_x = grid_x * TILE_SIZE + GRID_OFFSET_X
  screen_y = grid_y * TILE_SIZE + GRID_OFFSET_Y
  ```

#### Layer di Rendering
1. **Background Layer**
   - Sfondo base
   - Griglia pavimento

2. **Game Elements Layer**
   - Muri
   - Pozioni
   - Mostri
   - Portale

3. **Player Layer**
   - Sprite mago
   - Animazioni movimento

4. **UI Layer**
   - Statistiche
   - Messaggi stato
   - Overlay completamento

## Sistema Audio (sound.py)

### Architettura Multi-canale
```python
class SoundManager:
    def __init__(self):
        self.music = pygame.mixer.music      # Musica background
        self.sound_channel = pygame.mixer.Channel(1)  # Effetti
```

### Gestione Volume
- Volume indipendente per musica ed effetti
- Sistema mute/unmute
- Fade in/out transizioni

## Interface Utente (ui.py)

### Componenti Base
1. **Button**
   - Rendering dinamico
   - Gestione hover
   - Callback system

2. **StatBox**
   - Display statistiche real-time
   - Aggiornamento automatico
   - Trasparenza configurabile

3. **Popup**
   - Sistema di notifiche
   - Timeout automatico
   - Posizionamento dinamico

### Layout Sistema
```python
# Dimensioni e posizionamento UI
STATS_WINDOW_WIDTH = 300
STATS_WINDOW_HEIGHT = 200
GRID_OFFSET_X = 50
GRID_OFFSET_Y = 50
```

## Gestione Stati (game_state.py)

### Macchina a Stati
1. **INTRO**
   - Riproduzione video
   - Transizione al menu

2. **MENU**
   - Selezione livello
   - Controlli audio
   - Gestione UI

3. **PLAYING**
   - Loop di gioco
   - Aggiornamento stato
   - Rendering real-time

4. **LEVEL_COMPLETE**
   - Statistiche finali
   - Opzioni continuazione
   - Transizioni stato

### Pattern Observer
- Notifiche cambiamento stato
- Update listeners
- Eventi sistema

## Performance e Ottimizzazioni

### Rendering
- Double buffering
- Sprite caching
- Surface prerendering

### Memoria
- Gestione risorse dinamica
- Cleanup automatico
- Pooling oggetti

### CPU
- Frame rate limitato
- Ottimizzazione calcoli pathfinding
- Batch rendering
