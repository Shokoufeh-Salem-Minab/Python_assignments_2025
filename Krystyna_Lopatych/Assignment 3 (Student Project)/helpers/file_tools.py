def save_to_file(filename, text):
    with open(filename, "a", encoding='utf-8') as f:
        f.write(text + "\n")

def read_file(filename):
    try:
        with open(filename, "r", encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found yet"
