# Build Instructions

## Requisiti per la Build
- Python 3.11 o superiore
- pip (Package installer for Python)
- PyInstaller

## Dipendenze
```bash
pip install -r requirements.txt
```

## Generazione dell'eseguibile
1. Dalla root del progetto, eseguire:
```bash
pyinstaller --name="WizardTower" ^
            --windowed ^
            --icon="assets/ui/icon.ico" ^
            --add-data="assets;assets" ^
            --add-data="instances;instances" ^
            src/main.py
```

2. L'eseguibile verrà creato in:
   - `dist/WizardTower/WizardTower.exe`

## Struttura del Package
```
dist/WizardTower/
├── WizardTower.exe
├── assets/
│   ├── sprites/
│   ├── sounds/
│   └── ui/
├── instances/
└── python3x.dll
```
