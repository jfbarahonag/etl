"""Create database and tables for the project"""

import sqlite3
from common import LOGS_DIR, get_database_path
import logging
import os

logging.basicConfig(
    filename=os.path.join(LOGS_DIR, "create_database.log"),
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

def create_database():
    """Creates database and tables"""
    logging.info(f"Creating database -> {get_database_path()}")
    conn = sqlite3.connect(get_database_path())
    conn.close()
    logging.info(f"Database created -> {get_database_path()}")


def create_tables():
    """Creates tables"""
    logging.info("Creating tables")
    conn = sqlite3.connect(get_database_path())
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS house_prices (
            date DATE,
            price INTEGER,
            bedrooms INTEGER,
            bathrooms FLOAT,
            sqft_living INTEGER,
            sqft_lot INTEGER,
            floors FLOAT,
            waterfront INTEGER,
            view INTEGER,
            condition INTEGER,
            grade INTEGER,
            sqft_above INTEGER,
            sqft_basement INTEGER,
            yr_built INTEGER,
            yr_renovated INTEGER,
            zipcode INTEGER,
            lat FLOAT,
            long FLOAT,
            sqft_living15 INTEGER,
            sqft_lot15 INTEGER
        )"""
    )
    conn.commit()
    conn.close()
    logging.info("Tables created")


def main():
    """Orchestrates database creation"""
    create_database()
    create_tables()


if __name__ == "__main__":
    main()
