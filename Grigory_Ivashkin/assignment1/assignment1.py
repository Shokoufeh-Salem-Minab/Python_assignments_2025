print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
#---------------------------------------------------------------------------------------------------------------------------------------------
# here we take the user's input
# strip() removes spaces and line breaks from the input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

#---------------------------------------------------------------------------------------------------------------------------------------------
# we print the length of the name and surname by using len(x)
print("Length of first name:", len(first_name))
print("Length of last name:", len(last_name))

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we create the vowels variable and store the characters for a, e, i, o, and u
# we also create the variables "vowel_count" and "consonant_count" and set them to 0, because we will use them later.
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

#---------------------------------------------------------------------------------------------------------------------------------------------
# we create a loop to count the vowels.
# ch is a variable that takes every symbol one by one

# .lower makes a new string, but changes all symbols to be lowercase (e.g. R => r)
# that is made, so we won't check every input not only for aeiou, but also for AEIOU.

# .isalpha checks whether the symbol from ch ( our one by one symbol getting from the user's input variable) is a letter, not a number or a special 
# symbol. so, it will return true only if the symbol in ch is a character. (e.g. abcde....) and it will return false if the symbol is 1234-.+= ...
# and won't count them

# this loop checks the symbols in user's input one by one and if they = aeiou => vowel_count += 1
# if not consonant_count += 1
for ch in first_name.lower():
    if ch.isalpha():  
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
#---------------------------------------------------------------------------------------------------------------------------------------------
# here we print how many vowels we have
# and how many consonants we have
print("Vowels in first name:", vowel_count)
print("Consonants in first name:", consonant_count)

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we print the first name in uppercase and lowercase using .upper() and .lower()
print("First name (upper):", first_name.upper())
print("First name (lower):", first_name.lower())

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we print the last name reversed using [::-1]. (string slicing with step -1)

print("Last name (reversed):", last_name[::-1])


#---------------------------------------------------------------------------------------------------------------------------------------------
#\n creates a new line

# in this loop we print the letters one by one

# "for ch in first_name:" is used so we will take every character from user's input letter by letter and print them.
# end=" " is used so we won't have the every letter on a new line. we will have our result letter by letter but on one line. (e.g. G r i s h a)

# print() is just a creating of an empty line. just for the aesthetics. \n would create 2 new lines. in that case

print("\nCharacters in first name (for loop):")
for ch in first_name:
    print(ch, end=" ")
print()

#---------------------------------------------------------------------------------------------------------------------------------------------
# we create temporary variable temp. we store first name input in it. this is made, so we keep the user's input ( we will need it in the future 
# tasks) but will complete this task.

# this while loop will work while length of the temp is more than 0 characters.
# we print the first character temp[0]. end=" " is not to make a lot of lines,
# then we delete the first character using [1:]
# this loop will work while length of temp will be bigger than 0 after every first character deletion.
print("\nCharacters in first name (while loop):")
temp = first_name
while len(temp) > 0:
    print(temp[0], end=" ")
    temp = temp[1:]
print()

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we check the length of the first name and surname.

if len(first_name) > len(last_name):
    print("\nComparison result: First name is longer than last name.")
    
elif len(first_name) < len(last_name):
    print("\nComparison result: Last name is longer than first name.")
    
else:
    print("\nComparison result: First name and last name are equal in length.")

print("First name length is: ", len(first_name)," | ", "Last name length is: ", len(last_name))
    

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we will create a personal password.
# we create a variable first_letter and store in it the [0] (the first) symbol of the user's input
# same for last letter using [-1]
# and we create the variable for total_letters. there we store the sum the len() of first name and last name.
# total_letters is int for now
first_letter = first_name[0] if len(first_name) > 0 else ""
last_letter = last_name[-1] if len(last_name) > 0 else ""
total_letters = len(first_name) + len(last_name)

# here we create a password variable and store in it the string sum of first and last letter + string version of total letters (so, we could sum it in a string way)
password = first_letter + last_letter + str(total_letters)
print("Generated password:", password)

# but, ig it wouldn't work for password, as it will almost every time be 4 symbols
# :_(

#---------------------------------------------------------------------------------------------------------------------------------------------
# here we will create a list from our last name.
# we create a new variable last_list. store the lastname content in it and set it to list status using list()
last_list = list(last_name)

# using .append() we add something TO THE END of the list. It is because we don't "insert", we "add"
# using .insert() we "insert" something, but we must state the place in the list where we insert the new symbol. we set it's index to 0, so it 
# will become the first symbol in the list
last_list.append("*")     
last_list.insert(0, "@")  

# using .remove 'a' or 'A' we remove any 'a' or 'A' symbols from the list
if 'a' in last_list:
    last_list.remove('a')
elif 'A' in last_list:
    last_list.remove('A')
else:
    # in case there won't be any 'a' symbols in the user's input let's delete at least something. we will delete the second symbol
    # so, if the length of the last name is 2 or bigger. we delete the second symbol using .pop()
    # 1 is used because 1 is second, 0 is the first.
    if len(last_list) > 1:
        last_list.pop(1)

# .reverse() is used to reverse our list
last_list.reverse()

# and just printing
print("List methods example on last name:", last_list)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")