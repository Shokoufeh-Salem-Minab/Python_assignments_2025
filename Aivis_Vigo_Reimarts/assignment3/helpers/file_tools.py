def save_to_file(filename, text):
    """Append text to a file"""
    with open(filename, "a") as f:
        f.write(text + "\n")

def read_file(filename):
    """Read entire file contents"""
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

def clear_file(filename):
    """Clear file contents"""
    with open(filename, "w") as f:
        f.write("")
