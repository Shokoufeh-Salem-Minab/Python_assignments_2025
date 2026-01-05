"""
Simple program that output user text with random color and write logs to file
"""

from color_print import color_print

def main() -> None:
    for i in range(5):
        color_print(i)

if __name__ == "__main__":
    main()