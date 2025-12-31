def write_note(filename, text):
    
    with open(filename, "a") as file:
        file.write(text + "\n")


def read_notes(filename):
    
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "File not found."
