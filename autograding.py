"""Autograding script"""

import os

data = [
    ("src/input/create_database.py", "create_database.py not found"),
    ("src/input/data_pipeline.py", "data_pipeline.py not found"),
    ("src/input/test_create_database.py", "test_create_database.py not found"),
    ("src/input/test_data_pipeline.py", "test_data_pipeline.py not found"),
    ("datalake/databases/house_prices.db", "house_prices.db not found"),
]

for path, message in data:
    assert os.path.exists(path), message
