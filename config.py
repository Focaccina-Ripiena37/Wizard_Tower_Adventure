import os
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
SRC_DIR = ROOT_DIR / "src"
ASSETS_DIR = BASE_DIR / "assets"
INSTANCES_DIR = BASE_DIR / "instances"
LOGS_DIR = BASE_DIR / "logs"

# Logging
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = LOGS_DIR / "wizard_tower.log"

# Game Settings
DEBUG = False
SAVE_REPLAY = False
MAX_FPS = 60
ANIMATION_SPEED = 5

# Advanced Settings
PATHFINDING_TIMEOUT = 5  # seconds
MAX_LEVEL_SIZE = 50     # maximum grid dimension
AUDIO_CHANNELS = 8      # number of simultaneous sound channels

# Verifica esistenza directory critiche
for dir_path in [ASSETS_DIR, INSTANCES_DIR, LOGS_DIR]:
    if not dir_path.exists():
        raise FileNotFoundError(f"Directory {dir_path} non trovata")
