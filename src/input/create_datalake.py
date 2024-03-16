"""Create a datalake in the main directory"""

import os

STAGGING_PATH = "datalake/raw/stagging/"
INGESTED_PATH = "datalake/raw/ingested/"
DATABASE_PATH = "datalake/databases/"
LOGS_PATH = "datalake/logs/"


def create_datalake():
    """Create the datalake"""
    os.makedirs(STAGGING_PATH, exist_ok=True)
    os.makedirs(INGESTED_PATH, exist_ok=True)
    os.makedirs(DATABASE_PATH, exist_ok=True)
    os.makedirs(LOGS_PATH, exist_ok=True)


if __name__ == "__main__":
    create_datalake()