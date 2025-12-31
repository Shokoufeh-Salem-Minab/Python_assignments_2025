# --------------------------------------------
# Name Analysis & Practice Assignment
# --------------------------------------------

# Ask the user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print("\n--------------------------------------------")

# -------------------------------
# String Analysis
# -------------------------------

# Length of names
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

# Vowel and consonant counting (first name)
vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for char in first_name:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels in first name:", vowel_count)
print("Consonants in first name:", consonant_count)

# Uppercase and lowercase
print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())

# Reverse last name
print("Last name (reversed):", last_name[::-1])

print("\n--------------------------------------------")

# -------------------------------
# Loop Practice
# -------------------------------

# For loop
print("Characters in first name (for loop):")
for char in first_name:
    print(char)

print("\nCharacters in first name (while loop):")

# While loop (remove characters)
temp_name = first_name
while len(temp_name) > 0:
    print(temp_name[0])
    temp_name = temp_name[1:]

print("\n--------------------------------------------")

# -------------------------------
# Conditional Statements
# -------------------------------

if len(first_name) > len(last_name):
    comparison = "First name is longer than last name."
elif len(first_name) < len(last_name):
    comparison = "Last name is longer than first name."
else:
    comparison = "First name and last name are equal in length."

print("Comparison result:", comparison)

print("\n--------------------------------------------")

# -------------------------------
# Personal Password Generator
# -------------------------------

password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print("Generated password:", password)

print("\n--------------------------------------------")

# -------------------------------
# List Methods Practice
# -------------------------------

# Create list from last name
char_list = list(last_name)

# Append "*"
char_list.append("*")

# Insert "@"
char_list.insert(0, "@")

# Remove a character (remove last letter of last name)
if last_name[0] in char_list:
    char_list.remove(last_name[0])

# Reverse list
char_list.reverse()

print("List methods example on last name:")
print(char_list)

print("\n--------------------------------------------")
