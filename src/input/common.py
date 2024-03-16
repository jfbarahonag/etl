import os

from config import DATABASE_DIR, DATABASE_NAME

def get_database_path():
  return os.path.join(DATABASE_DIR, DATABASE_NAME)
