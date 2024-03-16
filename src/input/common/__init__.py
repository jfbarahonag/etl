from .config import *

def get_database_path():
  return os.path.join(DATABASE_DIR, DATABASE_NAME)