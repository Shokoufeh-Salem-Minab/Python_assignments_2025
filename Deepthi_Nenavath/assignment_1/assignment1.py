#Ask for input:
def get_user_input():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    return first_name, last_name


#String analysis:
def analyze_strings(first_name, last_name):
    first_len = len(first_name)
    last_len = len(last_name)

    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in first_name if char in vowels)
    consonant_count = sum(1 for char in first_name if char.isalpha() and char not in vowels)
    
    first_upper = first_name.upper()
    first_lower = first_name.lower()
    last_reversed = last_name[::-1]
    
    return {
        'first_len': first_len,
        'last_len': last_len,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'first_upper': first_upper,
        'first_lower': first_lower,
        'last_reversed': last_reversed
    }
#Loop practice:
def practice_loops(first_name):
    print("Characters in first name (for loop):", end=" ")
    for char in first_name:
        print(char, end=" ")
    print()
    
    print("Characters in first name (while loop):", end=" ")
    temp_name = list(first_name)
    while temp_name:
        print(temp_name.pop(0), end=" ")
    print()

#Conditions (if/elif/else):
def compare_lengths(first_len, last_len):
    if first_len > last_len:
        return "First name is longer than last name."
    elif first_len < last_len:
        return "Last name is longer than first name."
    else:
        return "First name and last name are equal in length."

#Generate a personal password:
def generate_password(first_name, last_name, first_len, last_len):
    first_letter = first_name[0] if first_name else ""
    last_letter = last_name[-1] if last_name else ""
    return f"{first_letter}{last_letter}{first_len + last_len}"

#List methods practice
def practice_list_methods(last_name):
    """Practice list methods on last name"""
    name_list = list(last_name)
    print(f"Original list: {name_list}")
    
    name_list.append("*")
    name_list.insert(0, "@")
 
    if len(name_list) > 2:
        name_list.pop(2)  
    
    name_list.reverse()
    return name_list

def display_results(first_name, last_name, analysis, comparison, password, final_list):
    """Display all results in organized sections"""
    sections = [
        ("STRING ANALYSIS", [
            f"Length of first name: {analysis['first_len']}",
            f"Length of last name: {analysis['last_len']}",
            f"Vowels in first name: {analysis['vowel_count']}",
            f"Consonants in first name: {analysis['consonant_count']}",
            f"First name (upper): {analysis['first_upper']}",
            f"First name (lower): {analysis['first_lower']}",
            f"Last name (reversed): {analysis['last_reversed']}"
        ]),
        ("LOOP PRACTICE", []),  # Loops are printed separately
        ("CONDITIONAL STATEMENTS", [
            f"Comparison result: {comparison}"
        ]),
        ("PERSONAL PASSWORD GENERATOR", [
            f"Generated password: {password}"
        ]),
        ("LIST METHODS PRACTICE", [
            f"Final list: {final_list}"
        ])
    ]
    
    for section_name, items in sections:
        print(f"\n{'='*50}")
        print(section_name)
        print('='*50)
        
        if section_name == "LOOP PRACTICE":
            practice_loops(first_name)
        else:
            for item in items:
                print(item)

def main():
    """Main function to run the entire program"""
    # Get user input
    first_name, last_name = get_user_input()
    
    # Analyze strings
    analysis = analyze_strings(first_name, last_name)
    
    # Compare lengths
    comparison = compare_lengths(analysis['first_len'], analysis['last_len'])
    
    # Generate password
    password = generate_password(first_name, last_name, analysis['first_len'], analysis['last_len'])
    
    # Practice list methods
    final_list = practice_list_methods(last_name)
    
    # Display all results
    display_results(first_name, last_name, analysis, comparison, password, final_list)

# Run the program
if __name__ == "__main__":
    main()