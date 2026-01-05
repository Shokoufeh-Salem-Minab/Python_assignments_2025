# assignment 1 - string analysis and practice
# student: nikita yukhnevich

# ask user for their names
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print()

# print length of both names
print(f"Length of first name: {len(first_name)}")
print(f"Length of last name: {len(last_name)}")

# count vowels in first name
vowels = "aeiouAEIOU"
vowel_count = 0
for i in range(len(first_name)):
    if first_name[i] in vowels:
        vowel_count += 1
print(f"Vowels in first name: {vowel_count}")

# count consonants in first name
consonant_count = 0
for i in range(len(first_name)):
    if first_name[i].isalpha() and first_name[i] not in vowels:
        consonant_count += 1
print(f"Consonants in first name: {consonant_count}")

# show first name in upper and lower case
print(f"First name (upper): {first_name.upper()}")
print(f"First name (lower): {first_name.lower()}")

# print last name backwards
print(f"Last name (reversed): {last_name[::-1]}")

print()

# use for loop to print each character
print("Characters in first name (for loop):")
for i in range(len(first_name)):
    print(first_name[i], end=" ")
print()

print()

# use while loop to print and remove characters
print("Characters in first name (while loop):")
temp_name = first_name
i = 0
while i < len(temp_name):
    print(temp_name[i], end=" ")
    i += 1
print()

print()

# compare which name is longer
print("Comparison result:", end=" ")
if len(first_name) > len(last_name):
    print("First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Last name is longer than first name.")
else:
    print("First name and last name are equal in length.")

print()

# make a password from the names
first_letter = first_name[0]
last_letter = last_name[-1]
total_letters = len(first_name) + len(last_name)
password = first_letter + last_letter + str(total_letters)
print(f"Generated password: {password}")

print()

# create list from last name and do stuff with it
last_name_list = list(last_name)

# add star at the end
last_name_list.append("*")

# add at symbol at the beginning
last_name_list.insert(0, "@")

# remove first letter of original last name
if len(last_name_list) > 2:
    last_name_list.remove(last_name[0])

# flip the list around
last_name_list.reverse()

# show final list
print(f"List methods example on last name: {last_name_list}")