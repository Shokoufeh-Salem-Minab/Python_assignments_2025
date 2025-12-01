def main() -> None:
    
    # String Analysis

    print("Hello!")
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    first_name = first_name.strip()
    last_name = last_name.strip()

    # 1. Print the lenght of the first name and last name.

    if len(first_name) == 0 or len(last_name) == 0:
        print("Please dont forget to type your information")
        exit(1)

    print("First name length is", len(first_name))
    print("Last name length is", len(last_name))

    # 2. Count vowels (a, e, i, o, u) in the first name.
    
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vow_sum = sum(1 for ch in first_name if ch.lower() in vowels)
    print("First name number of vowels is", vow_sum)

    # 3.Count consonants in the first name.

    print("First name number of consonants is", len(first_name) - vow_sum)

    # 4.Print the first name in uppercase and lowercase.
    
    print("Uppercase and lowercase first name is", first_name.upper(), first_name.lower())

    # 5. Print the last name reversed.
    
    print("Reversed last name is", last_name[::-1])
    
    # Loop Practice
    
    # 1. Use a for loop to print each character of the first name.
    
    print("Print of each character is", end="")
    for char in first_name:
        print(" " + char, end="")
    print()

    # 2. Use a while loop to print and remove characters from the first name until it is empty. 
    
    print("String where remove character of string is")
    
    temp_name = first_name
    while temp_name:
        print(temp_name)
        temp_name = temp_name[:-1]
    
    # Conditional Statements

    print("Comprasion")
    if len(first_name) > len(last_name):
        print("First name is longer than last name.")
    elif len(first_name) < len(last_name):
        print("Last name is longer than first name.")
    else:
        print("First name and last name are equal in length")
    
    # Personal Password Generator
    
    print("Generated password is",f"{first_name[0]}{last_name[-1]}{len(first_name) + len(last_name)}")

    # List Methods Practice 
    
    # 1.Create a list of characters from your last name.

    char_list = list(last_name)

    print("List before all changes is", char_list)

    # 2.Use .append() to add "*" at the end.

    char_list.append("*")

    # 3.Use .insert() to add "@" at the beginning.
    
    char_list.insert(0, "@")

    # 4. Use .remove() (or .pop()) to remove a character.
    
    char_list.pop(2)

    # 5. Use .reverse() to reverse the list.
    
    char_list.reverse()

    print("List after all changes is", char_list)


if __name__ == "__main__":
    main()
 