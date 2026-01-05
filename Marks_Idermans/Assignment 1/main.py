#Marks Idermans mi24027
#Assignment 1

run_again = 'y'

while run_again.lower() == 'y':

    #user input
    first = input("Type your first name: ")
    print()
    last = input("Type your last name: ")
    print()
    print(f"Hello, {first} {last}! Here is an analysis of your name:")
    print("-" * 45)

    #vowels and consonants
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for c in first if c in vowels)
    consonant_count = sum(1 for c in first if c.isalpha() and c not in vowels)

    #name lengths
    print(f"Your first name has {len(first)} letters.")
    print(f"Your last name has {len(last)} letters.")
    print(f"Vowels in your first name: {vowel_count}")
    print(f"Consonants in your first name: {consonant_count}")

    #Uppercase/lowercase
    print(f"First name in Uppercase: {first.upper()}")
    print(f"First name in lowercase: {first.lower()}")

    #Reverse last name
    print(f"Your last name backwards: {last[::-1]}")
    print()

    #For-loop
    print("Letters in your first name (for loop):")
    for char in first:
        print(char)
    print()

    #While-loop
    print("Removing one letter at a time (while loop):")
    shrinking = first
    while shrinking:
        print(shrinking)
        shrinking = shrinking[1:]  #remove first character
    print()

    #Compare lengths
    if len(first) > len(last):
        print("Your first name is longer than your last name.")
    elif len(first) < len(last):
        print("Your last name is longer than your first name.")
    else:
        print("Your first and last name are the same length.")
    print()

    #Create password
    password = first[0] + last[-1] + str(len(first) + len(last))
    print("A password based on your name:", password)
    print()

    #List with last name
    last_list = list(last)
    last_list.append("*")
    last_list.insert(0, "@")

    # Remove something (if there's enough to remove)
    if len(last_list) > 2:
        last_list.pop(2)

    last_list.reverse()

    print("Your last name list:")
    print(last_list)
    print()

    #run again
    run_again = input("Want to try again? (y/n): ")
    while run_again.lower() not in ['y', 'n']:
        run_again = input("Please type 'y' to restart or 'n' to quit: ")