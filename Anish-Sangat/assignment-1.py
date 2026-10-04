# ask the user for input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# stop the program if a name is empty, otherwise first_name[0] would crash later
if len(first_name) == 0 or len(last_name) == 0:
    print("Error: names must not be empty.")
    raise SystemExit

# ---------- string analysis ----------

print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

# count vowels and consonants in the first name
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for letter in first_name.lower():   # .lower() so capital letters count too
    if letter in vowels:
        vowel_count += 1
    elif letter.isalpha():          # a letter that is not a vowel = consonant
        consonant_count += 1

print("Vowels in first name:", vowel_count)
print("Consonants in first name:", consonant_count)

# extra: same counting for the last name
last_vowels = 0
last_consonants = 0
for letter in last_name.lower():
    if letter in vowels:
        last_vowels += 1
    elif letter.isalpha():
        last_consonants += 1
print("Vowels in last name:", last_vowels)
print("Consonants in last name:", last_consonants)

print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())
print("Last name (reversed):", last_name[::-1])

#loops

# for loop: print each character
print("Characters in first name (for loop):")
for char in first_name:
    print(char)

# while loop
print("Characters in first name (while loop):")
temp = first_name
while len(temp) > 0:
    print(temp[0])
    temp = temp[1:]    # cut off the first character

#conditions

if len(first_name) > len(last_name):
    print("Comparison result: First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("Comparison result: First name is shorter than last name.")
else:
    print("Comparison result: Both names have the same length.")

#password 

# first letter of first name + last letter of last name + total characters
total = len(first_name) + len(last_name)
password = first_name[0] + last_name[-1] + str(total)   # str() because total is a number
print("Generated password:", password)

#data types
print("Type of first_name:", type(first_name))   # str
print("Type of total:", type(total))             # int
print("Type of vowel_count:", type(vowel_count)) # int

#list methods

letters = list(last_name)   # list of characters of the last name
letters.append("*")         # add * to the end
letters.insert(0, "@")      # add @ at the beginning
# remove the 2nd letter of the last name (index 2 now, because of the @)
# I check the length first so it doesn't crash on very short names
if len(letters) > 2:
    letters.pop(2)
letters.reverse()           # reverse the list
print(letters)