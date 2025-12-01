VOWELS = ['a', 'e', 'i', 'o', 'u']
CONSONANTS = [
    'b', 'c', 'd', 'f', 'g', 'j', 'k', 'l', 'm', 'n', 
    'p', 'q', 's', 't', 'v', 'x', 'z', 'h', 'r', 'w', 'y'
]


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    if len(first_name) == 0 or len(last_name) == 0:
        print("Seriously?? " \
        "Do not waste computational power and time if you don't bother filling out first name and last name. " \
        "If you're not willing to provide complete information, don't expect me to run AT ALL.")
        exit(1)
            
    print(f"\nLength of first name: {len(first_name)}")
    print(f"Length of last name: {len(last_name)}")

    vowels_counter = 0
    for char in first_name.lower():
        if char in VOWELS: vowels_counter += 1
    print(f"Vowels in first name: {vowels_counter}")

    consonants_counter = 0
    for char in first_name.lower():
        if char in CONSONANTS: consonants_counter += 1
    print(f"Consonants in first name: {consonants_counter}")

    print(f"First name (upper): {first_name.upper()}")
    print(f"First name (lower): {first_name.lower()}")
    print(f"Last name (reversed): {last_name[::-1]}\n")

    print("Characters in first name (for loop):")
    for char in first_name:
        print(char)
        
    print("\nCharacters in first name (while loop):")
    first_name_list = list(first_name)
    while len(first_name_list) != 0:
        print(first_name_list.pop(0))

    print("\nComparison result: ", end="")
    if len(first_name) > len(last_name):
        print("First name is longer than last name.\n")  
    elif len(first_name) < len(last_name):
        print("Last name is longer than first name.\n")
    else:
        print("First name and last name are equal in length.\n")

    personal_password = first_name[0] + last_name[-1]
    personal_password += str(len(first_name) + len(last_name))
    print(f"Generated password: {personal_password}\n")

    print("List methods example on last name:")
    last_name_list = list(last_name)
    last_name_list.append('*')
    last_name_list.insert(0, '@')
    last_name_list.pop()
    last_name_list.reverse()
    print(last_name_list)

          
if __name__ == "__main__":
    main()
