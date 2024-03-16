"""Create database and tables for the project"""

import sqlite3

DATABASE_PATH = "datalake/databases/house_prices.db"


def create_database():
    """Creates database and tables"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.close()


def create_tables():
    """Creates tables"""
    conn = sqlite3.connect(DATABASE_PATH)
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


def main():
    """Orchestrates database creation"""
    create_database()
    create_tables()


if __name__ == "__main__":
    main()
