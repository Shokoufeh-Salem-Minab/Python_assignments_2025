
import os

def save_to_file(filename, text):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found. No data available yet."

def clear_file(filename):
   
    with open(filename, "w", encoding="utf-8") as f:
        f.write("")

def get_file_stats(filename):
  
    try:
        file_size = os.path.getsize(filename)
        return {"size_bytes": file_size, "exists": True}
    except FileNotFoundError:
        return {"size_bytes": 0, "exists": False}