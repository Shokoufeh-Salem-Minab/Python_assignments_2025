first_name = input("First name: ") or "Adrians"
last_name = input("Last name: ") or "Belahs"

print(first_name,last_name)
print()

print("Length of first name:",len(first_name))
print("Length of last name:",len(last_name))

vowels = {'a','e','i','o','u'}
vowels_first_name = 0
consonants_first_name = 0

print()
for letter in first_name.lower():
    if letter.isalpha():
        if letter in vowels:
            vowels_first_name+=1
        else:
            consonants_first_name+=1
print("Vowels in first name:",vowels_first_name)
print("Consonants in first name:",consonants_first_name)

first_name_upper = first_name.upper()
first_name_lower = first_name.lower()
last_name_reversed = last_name[::-1]
print("First name (upper):",first_name_upper)
print("First name (lower):", first_name_lower)
print("Last name (reversed):",last_name_reversed)
print()

print("Characters in first name (for loop):")
for letter in first_name:
    print(letter)
print()

if len(first_name)>len(last_name):
    print("Comparison result: First name is longer than last name.")
elif len(first_name)<len(last_name):
    print("Comparison result: First name is shorter than last name.")
else: print("Comparison result: First name is as long as the last name.")

personal_password = list(first_name)[0] + list(last_name).pop() + str(len(first_name)+len(last_name))
print(personal_password)

first_name_list = list(first_name)
last_name_list = list(last_name)
last_name_list.append('*')
last_name_list.insert(0,'@')
last_name_list.pop(3) #Deletes 4th element in current list
last_name_list.reverse()
print(last_name_list)

