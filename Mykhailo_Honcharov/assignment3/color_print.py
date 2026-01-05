import random 
import datetime
from colorama import Fore, Style
def log_to_file(text) -> None:
    with open("assignment3/data/logs.txt", "a") as f:
        x = datetime.datetime.now()
        f.write(x.strftime("%d %b %Y") + " " + str(text) + "\n")

def color_print(text) -> None:
    COLORS = ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]
    color = getattr(Fore, random.choice(COLORS))
    print(color + str(text) + Style.RESET_ALL)
    log_to_file(text)

