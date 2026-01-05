# input
first_name = input("Enter your first name: ").strip()
last_name  = input("Enter your last name: ").strip()

# String analysis
VOWELS = set("aeiouAEIOU")

len_first = len(first_name)
len_last = len(last_name)

vowels_cnt = sum(1 for ch in first_name if ch.isalpha() and ch in VOWELS)
consonants_cnt = sum(1 for ch in first_name if ch.isalpha() and ch not in VOWELS)

print()
print(f"Length of first name: {len_first}")
print(f"Length of last name: {len_last}")
print(f"Vowels in first name: {vowels_cnt}")
print(f"Consonants in first name: {consonants_cnt}")
print(f"First name (upper): {first_name.upper()}")
print(f"First name (lower): {first_name.lower()}")
print(f"Last name (reversed): {last_name[::-1]}")

# Loops
print("\nCharacters in first name (for loop):")
for ch in first_name:
    print(ch)

print("Characters in first name (while loop):")
temp = first_name
while temp:
    print(temp[0])
    temp = temp[1:]  

# Conditions
print()
if len_first > len_last:
    print("Comparison result: First name is longer than last name.")
elif len_first < len_last:
    print("Comparison result: First name is shorter than last name.")
else:
    print("Comparison result: First name and last name are equal in length.")

#password: first letter + last letter + total length
password = f"{first_name[0]}{last_name[-1]}{len_first + len_last}"
print(f"\nGenerated password: {password}")

chars = list(last_name)  # each character of the last name
chars.append("*")        # add "*" at the end
chars.insert(0, "@")     # add "@" at the beginning
if len(chars) > 1:
    chars.pop(1)         # delete one character (the original first letter)
chars.reverse()          # reverse the list
print(f"\n{chars}")

