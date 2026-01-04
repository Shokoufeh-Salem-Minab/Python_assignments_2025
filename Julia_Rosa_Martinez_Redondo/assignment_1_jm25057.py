# A C T I V I T Y 1 PYTHON - Name & Strings
# By Julia Rosa Martinez Redondo jm25057

# ~~~~~~~~INPUT SOLICITED~~~~~~~~
my_name = input("enter your 1st name: ")
surname = input("enter your surname: ")

# ~~~~~~~~ANALYSIS OF STRINGS RECEIVED~~~~~~~~
print("\nlength 1st name:", len(my_name))
print("length surname:", len(surname))

# count vowels & consonants (1st name tho)
vowels = "aeiou"
vowels_total = 0
consonants_total = 0

for letter in my_name.lower():      # letter per letter loop
    if letter in vowels:            # if it's vowel:
        vowels_total += 1
    else:
        if letter.isalpha():        # only letters
            consonants_total += 1
            
print("vowels 1st name:", vowels_total)
print("consonants 1st name:", consonants_total)
print("1st name upper:", my_name.upper())
print("1st name lower:", my_name.lower())
print("surname reversed:", surname[::-1])

# ~~~~~~~~LOOPING~~~~~~~~
print("\ncharacters 1st name to loop:")
for letter in my_name:
    print(letter)

print("\ncharacters 1st name meanwhile loop:")
name_copy = my_name    # copy first name
while len(name_copy) > 0:
    print(name_copy[0])    # printing the 1st char
    name_copy = name_copy[1:]  # removing first char

# ~~~~~~~~CONDITIONAL'S~~~~~~~~
if len(my_name) > len(surname):
    print("\n1st name > surname")
elif len(my_name) < len(surname):
    print("\nsurname > 1st name")
else:
    print("\n1st name & surname SAME length")

# ~~~~~~~~PASSWORD PERSONAL~~~~~~~~
# first letter + last letter + total length
letters_sum = len(my_name) + len(surname)

if len(my_name) > 0 and len(surname) > 0:
    password = my_name[0] + surname[-1] + str(letters_sum)
else:
    password = "??" + str(letters_sum)
print("generated password:", password)

# ~~~~~~~~METHODS THAT LISTED~~~~~~~~
surname_list = list(surname)   # list made from surname
surname_list.append("*")       # add * at in ending
surname_list.insert(0, "@")    # add @ at start
surname_list.reverse()         # reverse this list

print("finale list:", surname_list)
