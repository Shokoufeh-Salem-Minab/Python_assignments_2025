import os
from pathlib import Path

from mylib import File

FILE_NAME = "test.bin"
MY_DATA = b"My data bytes"


# Create new file
def save_example():
    file = File(True, False)
    file.add_bytes(MY_DATA)
    file.write_file(Path(FILE_NAME))


# Load new File
def load_example():
    file = File.from_file(Path(FILE_NAME))
    bytes_ = file.get_bytes()
    assert bytes_ == MY_DATA


if __name__ == "__main__":
    save_example()
    load_example()
    os.remove(Path(FILE_NAME))
