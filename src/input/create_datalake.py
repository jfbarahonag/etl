"""Create a datalake in the main directory"""

import os

from config import STAGGING_DIR, INGESTED_DIR, DATABASE_DIR, LOGS_DIR

def create_datalake():
    """Create the datalake"""
    os.makedirs(STAGGING_DIR, exist_ok=True)
    os.makedirs(INGESTED_DIR, exist_ok=True)
    os.makedirs(DATABASE_DIR, exist_ok=True)
    os.makedirs(LOGS_DIR, exist_ok=True)


if __name__ == "__main__":
    create_datalake()