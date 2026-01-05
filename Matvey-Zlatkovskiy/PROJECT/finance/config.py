import os

APP_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(APP_DIR)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
CSV_PATH = os.path.join(DATA_DIR, "transactions.csv")
LOG_PATH = os.path.join(LOG_DIR, "app.log")
COLUMNS = ["id", "date", "type", "category", "amount", "note"]
DEFAULT_CATEGORIES = ["food", "transport", "bills", "rent", "entertainment", "shopping", "health", "other"]
