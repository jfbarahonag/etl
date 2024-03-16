"""ETL for importing house prices data from csv file to database"""

import glob
import os.path
import shutil
import sqlite3

import pandas as pd

from config import STAGGING_DIR, INGESTED_DIR
from common import get_database_path

def extract():
    """Extracts data from csv file"""
    filenames = glob.glob(STAGGING_DIR + "*.csv.zip")
    dataframes = [pd.read_csv(f, compression="zip") for f in filenames]
    data = pd.concat(dataframes)
    return data


def transform(data):
    """Transforms data to be ready for loading"""
    data["date"] = pd.to_datetime(data["date"])
    return data


def load(data):
    """Loads data to database"""
    conn = sqlite3.connect(get_database_path())
    data.to_sql("house_prices", conn, if_exists="replace", index=False)
    conn.close()


def move_files():
    """Moves files from stagging to ingested folder"""
    for filename in glob.glob(STAGGING_DIR + "*.csv.zip"):
        shutil.move(filename, INGESTED_DIR + os.path.basename(filename))


def etl():
    """Orchestrates ETL process"""
    data = extract()
    data = transform(data)
    load(data)
    move_files()


if __name__ == "__main__":
    etl()

    
    
    
    
    
    
    
    
    