"""ETL for importing house prices data from csv file to database"""

import glob
import os.path
import shutil
import sqlite3

import pandas as pd

STAGGING_PATH = "datalake/raw/stagging/"
INGESTED_PATH = "datalake/raw/ingested/"
DATABASE_PATH = "datalake/databases/house_prices.db"
LOGS_PATH = "datalake/logs/"


def extract():
    """Extracts data from csv file"""
    filenames = glob.glob(STAGGING_PATH + "*.csv.zip")
    dataframes = [pd.read_csv(f, compression="zip") for f in filenames]
    data = pd.concat(dataframes)
    return data


def transform(data):
    """Transforms data to be ready for loading"""
    data["date"] = pd.to_datetime(data["date"])
    return data


def load(data):
    """Loads data to database"""
    conn = sqlite3.connect(DATABASE_PATH)
    data.to_sql("house_prices", conn, if_exists="replace", index=False)
    conn.close()


def move_files():
    """Moves files from stagging to ingested folder"""
    for filename in glob.glob(STAGGING_PATH + "*.csv.zip"):
        shutil.move(filename, INGESTED_PATH + os.path.basename(filename))


def etl():
    """Orchestrates ETL process"""
    data = extract()
    data = transform(data)
    load(data)
    move_files()


if __name__ == "__main__":
    etl()

    
    
    
    
    
    
    
    
    