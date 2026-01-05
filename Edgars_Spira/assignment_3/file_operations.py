from datetime import datetime
from emoji import emojize
import os


base_directory = os.path.dirname(os.path.abspath(__file__)) # Path to the current file
file_path = os.path.join(base_directory, "data", "message.txt") # Add exact location of message files

# Write a message into message file, appending a message and datetime of the operation and a thumbs up emoji
def write_message(text, file_path = file_path, ):
    file = open(file_path, "a", encoding="utf-8")
    file.write(emojize(text + " - " + str(datetime.now()) + ":thumbs_up:" "\n"))
    file.close()

# Read all messages from file and return them
def read_messages():
    file = open(file_path, "r", encoding="utf-8")
    content = file.read()
    file.close()
    return content
