@echo off
cd /d "%~dp0"
echo Creating executable...

REM Pulisci le vecchie build
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "installer" rd /s /q "installer"

REM Crea l'eseguibile
python -m PyInstaller ^
    --name=WizardTower ^
    --windowed ^
    --icon="assets\\ui\\icon.ico" ^
    --add-data="assets;assets" ^
    --add-data="instances;instances" ^
    --add-data="src;src" ^
    --hidden-import=src.main ^
    --hidden-import=src.constants ^
    --hidden-import=src.game_state ^
    --hidden-import=src.sound ^
    --hidden-import=src.sprite_loader ^
    --hidden-import=src.menu ^
    --hidden-import=src.level ^
    --hidden-import=src.wizard_tower_merged ^
    --hidden-import=src.intro_screen ^
    --hidden-import=src.video_handler ^
    --hidden-import=src.ui ^
    --hidden-import=src.sprites ^
    --collect-all pygame ^
    --debug=all ^
    --log-level=DEBUG ^
    --paths="src" ^
    run.py

echo Creating logs directory...
if not exist "dist\WizardTower\logs" mkdir "dist\WizardTower\logs"

echo Creating installer directory...
if not exist "installer" mkdir "installer"

echo Creating installer using Inno Setup...
"C:\Program Files (x86)\Inno Setup 6\ISCC.exe" /Q "installer_script.iss"

echo Build completato!
pause