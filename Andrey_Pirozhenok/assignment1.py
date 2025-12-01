def main() -> None:
    # String analysis

    print("Hello user!")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    print(f"First name is {len(first_name)} characters long.")
    print(f"Last name is {len(last_name)} characters long.")

    if len(first_name) == 0 or len(first_name) == 0:
        print("Refusing to process empty strings.")
        return

    vowel_count = sum(1 for c in first_name if c.lower() in "aeiou")

    def is_consonant(c: str) -> bool:
        return c.isascii() and c.isalpha() and c.lower() not in "aeiou"

    consonant_count = sum(1 for c in first_name if is_consonant(c))
    print(f"First name contains {vowel_count} vowels and {consonant_count} consonants.")

    print(f"First name in uppercase: {first_name.upper()}")
    print(f"First name in lowercase: {first_name.lower()}")

    print(f"Last name reversed: {last_name[::-1]}")

    # Loop practise

    print("Characters of the first name:", end="")
    for char in first_name:
        print(" " + char, end="")
    print()

    print("Removing characters from first name:")
    name = first_name
    while len(name) > 0:
        print(f"char={name[0]} full={name}")
        name = name[1:]

    # Conditional statements

    if len(first_name) > len(last_name):
        print("First name is longer then last name.")
    elif len(first_name) < len(last_name):
        print("Last name is longer then first name.")
    else:
        print("First name is the same length as last name")

    # Personal password generator

    password = f"{first_name[0]}{last_name[-1]}{len(first_name) +len(last_name)}"
    print(f"Your super secret password is {password}")

    # List method practise

    chars = list(last_name)
    print(f"List of characters from the last name: {chars}")

    chars.append("*")
    chars.insert(0, "@")
    _ = chars.pop(1)
    chars.reverse()
    print(f"List of characters after all operations: {chars}")


if __name__ == "__main__":
    main()
