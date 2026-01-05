from colorama import Fore, init
import utils

init()  # initialize colorama

file_path = "data/notes.txt"

# Write to file
with open(file_path, "a") as file:
    file.write("Hello! Time: " + utils.get_time() + "\n")

# Read from file
print(Fore.GREEN + "File Contents:")
with open(file_path, "r") as file:
    print(file.read())

