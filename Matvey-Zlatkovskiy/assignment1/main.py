
"""
This program analyzes the user's first and last name in various ways.
You can re-run the program :)
print() is used to create blank lines for better readability.
"""
answer = 'y'
while answer.lower() == 'y':
    
    # Initial input and greeting
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print()
    print(f"Hello, {first_name} {last_name}!")
    print("Here is some analysis of you:")
    print("-" * 40)
    
    # For vowels and consonants count
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in first_name if char in vowels)
    consonant_count = sum(1 for char in first_name if char.isalpha() and char not in vowels)

    # Name and last name lengtha
    print(f"Length of first name: {len(first_name)}")
    print(f"Length of last name: {len(last_name)}")
    
    # Vowel and consonant count
    print(f"Vowels in first name: {vowel_count}")
    print(f"Consonants in first name: {consonant_count}")
    
    # ALL CAPS and all lowercase
    print(f"First name (upper): {first_name.upper()}")
    print(f"First name (lower): {first_name.lower()}")
    
    # Reverse last name
    print(f"Last name (reverse): {last_name[::-1]}")
    print()
    
    # For loop: characters
    print("Characters in first name (for loop):")
    for ch in first_name:
        print(ch)
    print()
    
    # While loop: removing characters until empty
    print("Characters in first name (while loop):")
    temp_name = first_name
    while temp_name:
        print(temp_name[0]) # First character placed
        temp_name = temp_name[1:] # First character removed
    print()
    
    # Conditionals if/elif/else and comparison
    if len(first_name) > len(last_name):
        print("Comparison result: First name is longer than last name.")
    elif len(first_name) < len(last_name):
        print("Comparison result: First name is shorter than last name.")
    else:
        print("Comparison result: First name and last name are equal in length.")
    print()
    
    # Password Generation
    password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
    print("Generated password:", password)
    print()
    
    # List manipulation
    last_name_list = list(last_name)
    last_name_list.append("*")
    last_name_list.insert(0, "@")
    last_name_list.pop(1)
    last_name_list.reverse()
    print(last_name_list)
    print()
    
    # Small pause
    input("Press Enter to continue...")
    print()
    
    # Restart prompt and validation        
    answer = input("Would you like to restart? (y/n): ")
    while answer.lower() not in ['y', 'n']:
        answer = input("Please enter 'y' to restart or 'n' to quit: ")