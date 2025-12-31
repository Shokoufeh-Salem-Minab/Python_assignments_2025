

import os         
import datetime    
from utils import file_utils



DATA_DIR = "data"
FILE_PATH = os.path.join(DATA_DIR, "notes.txt")


if not os.path.exists(DATA_DIR):
    os.mkdir(DATA_DIR)



current_time = datetime.datetime.now()
note = f"Note added at {current_time}"

file_utils.write_note(FILE_PATH, note)



print("Reading notes from file:\n")
content = file_utils.read_notes(FILE_PATH)
print(content)
