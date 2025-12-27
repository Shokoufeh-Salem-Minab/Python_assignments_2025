first_name = raw_input("Enter your first name: ")
last_name = raw_input("Enter your last name: ")

print "\nLength of first name:", len(first_name)
print "Length of last name:", len(last_name)

vowels = "aeiouAEIOU"
vowel_count = 0
for char in first_name:
    if char in vowels:
        vowel_count += 1
print "Vowels in first name:", vowel_count

consonant_count = 0
for char in first_name:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print "Consonants in first name:", consonant_count

print "First name (upper):", first_name.upper()
print "First name (lower):", first_name.lower()

print "Last name (reversed):", last_name[::-1]

print "\nCharacters in first name (for loop):"
for char in first_name:
    print char

print "\nCharacters in first name (while loop):"
temp_name = first_name
while len(temp_name) > 0:
    print temp_name[0]
    temp_name = temp_name[1:]

print "\nComparison result:",
if len(first_name) > len(last_name):
    print "First name is longer than last name."
elif len(first_name) < len(last_name):
    print "First name is shorter than last name."
else:
    print "First name and last name have equal length."

first_letter = first_name[0]
last_letter = last_name[-1]
total_chars = len(first_name) + len(last_name)
password = first_letter + last_letter + str(total_chars)
print "\nGenerated password:", password

last_name_list = list(last_name)
last_name_list.append("*")
last_name_list.insert(0, "@")
last_name_list.remove(last_name_list[1]) 
last_name_list.reverse()

print "\n", last_name_list
