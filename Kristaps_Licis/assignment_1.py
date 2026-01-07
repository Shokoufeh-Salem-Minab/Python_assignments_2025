#  INPUT 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# STRING ANALYSIS 
print("\nLength of first name:", len(first_name))
print("Length of last name:", len(last_name))

# Count vowels (a, e, i, o, u) in first name
vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in first_name if char in vowels)
print("Vowels in first name:", vowel_count)

# Count consonants in first name
consonant_count = sum(1 for char in first_name if char.isalpha() and char not in vowels)
print("Consonants in first name:", consonant_count)

# Print first name in uppercase and lowercase
print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())

# Print last name reversed
print("Last name (reversed):", last_name[::-1])

# LOOP PRACTICE
# For loop - print each character of first name
print("\nCharacters in first name (for loop):", end=" ")
for char in first_name:
    print(char, end=" ")
print()

# While loop - print and remove characters from first name until empty
print("Characters in first name (while loop):", end=" ")
temp_name = first_name
while temp_name:
    print(temp_name[0], end=" ")
    temp_name = temp_name[1:]
print()

# CONDITIONAL STATEMENTS 
# Compare lengths of first and last name
print("\nComparison result: ", end="")
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are equal in length.")

# PERSONAL PASSWORD GENERATOR
# Create password by combining:
# - First letter of first name
# - Last letter of last name
# - Total number of letters (first + last name)
password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print("\nGenerated password:", password)

# LIST METHODS PRACTICE 
# Create list of characters from last name
last_name_list = list(last_name)

# Use .append() to add "*" at the end
last_name_list.append("*")

# Use .insert() to add "@" at the beginning
last_name_list.insert(0, "@")

# Use .remove() to remove a character (first character of original last name)
last_name_list.remove(last_name[0])

# Use .reverse() to reverse the list
last_name_list.reverse()

# Print the final list
print("\nList methods example on last name:", last_name_list)
