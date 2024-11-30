# run.py
import os
import sys
import pygame
import traceback
from datetime import datetime

def setup_logging():
    """Setup logging for the application."""	
    base_path = os.path.dirname(os.path.abspath(sys.executable if getattr(sys, 'frozen', False) else __file__))
    log_dir = os.path.join(base_path, 'logs')
    try:
        os.makedirs(log_dir, exist_ok=True)
    except PermissionError:
        print(f"Permission denied: Unable to create {log_dir}")
    return os.path.join(log_dir, 'error.log')

def write_error(log_file, error_msg):
    """Write error message to log file."""
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"\n{'-'*50}\n")
            f.write(f"Error timestamp: {datetime.now()}\n")
            f.write(error_msg)
    except PermissionError:
        print(f"Permission denied: Unable to write to {log_file}")

def main():
    # Set base path for application files based on frozen or development mode 
    if getattr(sys, 'frozen', False):
        # If exe (frozen)
        base_path = os.path.dirname(sys.executable)
    else:
        # If in development
        base_path = os.path.dirname(os.path.abspath(__file__))

    os.chdir(base_path)
    log_file = setup_logging()

    # Check if src directory exists
    src_path = os.path.join(base_path, 'src')
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    try:
        # Initial game log message
        write_error(log_file, f"""
Starting application...
Base path: {base_path}
Current directory: {os.getcwd()}
Python path: {sys.path}
src directory exists: {os.path.exists('src')}
        """)

        # Importa la classe Game from src.main
        write_error(log_file, "Importing Game class...")
        from src.main import Game
        
        write_error(log_file, "Initializing game...")
        game = Game()
        
        write_error(log_file, "Starting game loop...")
        game.run()

    except Exception as e:
        error_msg = f"""
Error running game: {str(e)}

Traceback:
{traceback.format_exc()}
        """
        write_error(log_file, error_msg)
        
        # Show error message to user
        try:
            import tkinter as tk
            from tkinter import messagebox
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error", 
                f"An error occurred while running the game.\n"
                f"Check logs/error.log for details.\n\n"
                f"Error: {str(e)}")
        except:
            print(f"Fatal error: {str(e)}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
