# import os and datetime
import os
from datetime import datetime

# set the file name
FILE_NAME = "notes.txt"

# set the directory path where our file will appear. (it is set that the file will appear in the assignment3 dir)
# in a simple words, this is made to put the notes. txt file in the assignment3 folder.
# as you can see the function was used twice. if we would use it once, the file would be putted into utils dir.

# __file__ is a var that contains a path to the current file. ( notes_utils.py)
# os.path.dirname() is the function that takes the folder from the path, but we take a folder, that contain a 
# folder from the path to chose it to be the folder to contain notes.txt
# This is done to prevent the file from appearing in a random folder, so that everything is correct and neat, regardless of where we launch main.py
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# sets path correctly for Windows/Mac. (e.g. BASE_DIR = assignment3, FILE_NAME = notes.txt, the path will be .../assignment_3/notes.txt)
    # for Window it will be ...\assignment3\notes.txt, but join() will will put everything in its place
def ensure_notes_file():
    path = os.path.join(BASE_DIR, FILE_NAME)

    # if there is no such file, like we set two lines above, we will create it.
    if not os.path.exists(path): # the check if such file exists
        # Mode "w" = write (create/overwrite file).
            # but we get here only if there is no such file, so it is create for us.
        # encoding="utf-8" so, not only latin symbols saves correctly.
        #with ... as f ensures that the file will be closed when we will finish the work.
        with open(path, "w", encoding="utf-8") as f:
            f.write("")
# returning the path, so, other functions could use it.
    return path

# creates new note. write in file note content and date and time
# firstly, ensures that notes.txt exist and get the path.
def add_note(note_text):
    path = ensure_notes_file()

    # then, we receive the current date and time.
    # strftime("%Y-%m-%d %H:%M:%S") is made to save the content as a string by sample (year, month, day  hour, minute, second)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Mode "a" = append. It means, we will add the result to the end and won't delete what we already have in a file. 
    with open(path, "a", encoding="utf-8") as f:
        # using f.write() we write one line in a file.
        f.write(f"[{timestamp}] {note_text}\n")

# read full file and print it in the console
def read_notes():
    # ensure that the path and that such file exist.
    path = ensure_notes_file()

    # Mode "r" = read. 
    # we open file to read. ensure we will close it.
    with open(path, "r", encoding="utf-8") as f:
        # f.read() reads the entire file as a single line and returns it.
        # that is why we have
            # notes = read_notes()
            # print(notes)
        # in main.py
        return f.read()
