# Helper to handle file operations

def save_to_file(filename, text):
    """Saves the given text to a file with the specified filename.

    Args:
        filename (str): The name of the file where the text will be saved.
        text (str): The text content to be saved in the file.
    """
    with open(filename, 'a') as file:
        file.write(text + "\n")
        
def read_from_file(filename):
    """Reads and returns the content of the specified file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        str: The content of the file.
    """
    with open(filename, 'r') as file:
        return file.read()