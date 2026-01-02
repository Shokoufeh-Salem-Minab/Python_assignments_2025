# 1. User input


first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")


# 2. String analysis

# Length of first and last name
print("\nLength of first name:", len(first_name))
print("Length of last name:", len(last_name))

# Count vowels and consonants in the first name
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in first_name.lower():
    if char.isalpha():  # Check if character is a letter
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels in first name:", vowel_count)
print("Consonants in first name:", consonant_count)

# Uppercase and lowercase
print("First name in uppercase:", first_name.upper())
print("First name in lowercase:", first_name.lower())

# Reverse the last name
print("Last name reversed:", last_name[::-1])

# 3. Loop practise

# For loop: print each character of first name
print("\nCharacters in first name (for loop):")
for char in first_name:
    print(char)

# While looping, remove characters until empty
temp_name = first_name 

print("\nRemoving characters using while loop:")
while len(temp_name) > 0:
    print(temp_name)
    temp_name = temp_name[1:]  # Remove the first character


# 4. Conditional statements


if len(first_name) > len(last_name):
    print("\nFirst name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are equal in length.")


# 5. Password generator


password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print("\nGenerated password:", password)


# 6. List methods practise


# Create a list from last name
last_name_list = list(last_name)

# Add "*" at the end
last_name_list.append("*")

# Add "@" at the beginning
last_name_list.insert(0, "@")

# Remove one character (last one before reversing)
last_name_list.pop()

# Reverse the list
last_name_list.reverse()

print("\nFinal list:", last_name_list)

