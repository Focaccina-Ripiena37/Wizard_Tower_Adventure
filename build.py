import os
import shutil
import subprocess
import sys
import time

def install_pyinstaller():
    """Ensure PyInstaller is installed."""
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'pyinstaller'], check=True)

def remove_directory(path):
    """Remove a directory, retrying if it is in use."""
    for _ in range(5):
        try:
            shutil.rmtree(path)
            print(f"Rimossa cartella {path}")
            return
        except PermissionError:
            print(f"PermissionError: {path} è in uso. Riprovo...")
            time.sleep(1)
    print(f"Impossibile rimuovere {path} dopo diversi tentativi.")

def create_executable():
    """Create the executable using PyInstaller."""
    pyinstaller_path = os.path.join(os.path.dirname(sys.executable), 'Scripts', 'pyinstaller.exe')
    if not os.path.exists(pyinstaller_path):
        pyinstaller_path = os.path.join(os.path.dirname(sys.executable), 'Scripts', 'pyinstaller')
    if not os.path.exists(pyinstaller_path):
        pyinstaller_path = shutil.which('pyinstaller')  # Fallback to system PATH
    if not pyinstaller_path:
        raise FileNotFoundError("PyInstaller executable not found.")
    
    command = [
        pyinstaller_path,
        '--name=WizardTower',
        '--windowed',
        '--icon=assets/ui/icon.ico',
        '--add-data=assets;assets',
        '--add-data=instances;instances',
        '--add-data=src;src',
        '--hidden-import=src.main',
        '--hidden-import=src.constants',
        '--hidden-import=src.game_state',
        '--hidden-import=src.sound',
        '--hidden-import=src.sprite_loader',
        '--hidden-import=src.menu',
        '--hidden-import=src.level',
        '--hidden-import=src.wizard_tower_merged',
        '--hidden-import=src.intro_screen',
        '--hidden-import=src.video_handler',
        '--hidden-import=src.ui',
        '--hidden-import=src.sprites',
        '--collect-all=pygame',
        '--debug=all',
        'run.py'
    ]
    
    subprocess.run(command, check=True)

def main():
    """Main entry point for the build script."""
    try:
        print("\n=== Inizio processo di build ===")
        
        install_pyinstaller()
        
        for path in ['build', 'dist', 'installer']:
            if os.path.exists(path):
                remove_directory(path)
        
        create_executable()
        
        print("\n=== Build completata con successo! ===")
        
    except Exception as e:
        print(f"\nERRORE durante la build: {e}")
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    import traceback
    exit(main())