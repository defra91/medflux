# src/config.py

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ORIGINAL_DB_PATH = BASE_DIR / "db.xlsx"
DESTINATION_DB_PATH = BASE_DIR / "db_copy.xlsx"

OUTPUT_DIR = BASE_DIR / "output"