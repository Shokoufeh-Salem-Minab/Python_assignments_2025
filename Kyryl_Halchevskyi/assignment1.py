first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# 1. Print lengths
print("\nLength of first name:", len(first_name))
print("Length of last name:", len(last_name))

# 2. Count vowels in first name
vowels = 0
for char in first_name:
    if char.lower() in "aeiou":
        vowels = vowels + 1
print("Vowels in first name:", vowels)

# 3. Count consonants in first name
consonants = 0
for char in first_name:
    if char.isalpha() and char.lower() not in "aeiou":
        consonants = consonants + 1
print("Consonants in first name:", consonants)

# 4. Print first name in uppercase and lowercase
print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())

# 5. Print last name reversed
print("Last name (reversed):", last_name[::-1])

# Loop Practice
# 1. For loop - print each character
print("\nCharacters in first name (for loop):")
for char in first_name:
    print(char)

# 2. While loop - print and remove characters
print("\nCharacters in first name (while loop):")
temp_name = first_name
while len(temp_name) > 0:
    print(temp_name[0])
    temp_name = temp_name[1:]

# Conditional Statements - compare lengths
print("\nComparison result:")
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are equal in length.")

# Personal Password Generator
password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print("\nGenerated password:", password)

# List Methods Practice
last_name_list = list(last_name)
last_name_list.append("*")
last_name_list.insert(0, "@")
last_name_list.remove(last_name_list[1])  # removes first character after @
last_name_list.reverse()
print("\nList methods example on last name:", last_name_list)