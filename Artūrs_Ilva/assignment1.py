first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"\nLength of first name: {len(first_name)}")
print(f"Length of last name: {len(last_name)}")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0

for ch in first_name:
    if ch.isalpha():
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels in first name: {vowel_count}")
print(f"Consonants in first name: {consonant_count}")

print(f"First name (upper): {first_name.upper()}")
print(f"First name (lower): {first_name.lower()}")
print(f"Last name (reversed): {last_name[::-1]}")

print("\nCharacters in first name (for loop):")
for ch in first_name:
    print(ch)

print("\nCharacters in first name (while loop):")
temp = first_name
while len(temp) > 0:
    print(temp[0])
    temp = temp[1:]

if len(first_name) > len(last_name):
    print("\nComparison result: First name is longer than last name.")
elif len(first_name) < len(last_name):
    print("\nComparison result: Last name is longer than first name.")
else:
    print("\nComparison result: Both names are the same length.")

password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print(f"\nGenerated password: {password}")

char_list = list(last_name)
char_list.append("*")
char_list.insert(0, "@")
char_list.remove(last_name[1])
char_list.reverse()

print(char_list)
