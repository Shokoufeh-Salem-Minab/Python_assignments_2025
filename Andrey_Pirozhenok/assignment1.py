from typing import Callable


def main() -> None:
    # String analysis

    print("Hello user!")
    firstname = input("What is your firstname? ")
    lastname = input("What is your lastname? ")

    print(f"Firstname is {len(firstname)} characters long.")
    print(f"Lastname is {len(lastname)} characters long.")

    if len(firstname) == 0 or len(firstname) == 0:
        print("Refusing to process empty strings.")
        return

    vowel_count = sum(1 for c in firstname if c.lower() in "aeiou")

    def is_consonant(c: str) -> bool:
        return c.isascii() and c.isalpha() and c.lower() not in "aeiou"

    consonant_count = sum(1 for c in firstname if is_consonant(c))
    print(f"Firstname contains {vowel_count} vowels and {consonant_count} consonants.")

    print(f"First name in uppercase: {firstname.upper()}")
    print(f"First name in lowercase: {firstname.lower()}")

    print(f"Last name reversed: {lastname[::-1]}")

    # Loop practise

    print("Characters of the firstname:", end="")
    for char in firstname:
        print(" " + char, end="")
    print()

    print("Removing characters from firstname:")
    name = firstname
    while len(name) > 0:
        print(f"char={name[0]} full={name}")
        name = name[1:]

    # Conditional statements

    if len(firstname) > len(lastname):
        print("Firstname is longer then lastname.")
    elif len(firstname) < len(lastname):
        print("Lastname is longer then firstname.")
    else:
        print("Firstname is the same length as lastname")

    # Personal password generator

    password = f"{firstname[0]}{lastname[-1]}{len(firstname) +len(lastname)}"
    print(f"Your super secret password is {password}")

    # List method practise

    chars = list(lastname)
    print(f"List of characters from the last name: {chars}")

    chars.append("*")
    chars.insert(0, "@")
    _ = chars.pop(1)
    chars.reverse()
    print(f"List of characters after all operations: {chars}")


if __name__ == "__main__":
    main()
