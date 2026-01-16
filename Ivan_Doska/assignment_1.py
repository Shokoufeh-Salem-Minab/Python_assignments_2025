first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

print(f"\nLength of first name: {len(first_name)}")
print(f"Length of last name: {len(last_name)}")
vowels = sum(1 for c in first_name if c in "aeiouAEIOU")
consonants = sum(1 for c in first_name if c.isalpha() and c not in "aeiouAEIOU")
print(f"Vowels in first name: {vowels}")
print(f"Consonants in first name: {consonants}")
print(f"First name (upper): {first_name.upper()}")
print(f"First name (lower): {first_name.lower()}")
print(f"Last name (reversed): {last_name[::-1]}")
print("\nCharacters in first name (for loop):")
for c in first_name: 
    print(c, end=" ")
print()

print("\nCharacters in first name (while loop):")
t = first_name #t - temp
while t: # while not null
    print(t[0], end=" ")
    t = t[1:]
print() # new line

if len(first_name) > len(last_name):
    result = "First name is longer than last name"
elif len(first_name) < len(last_name):
    result = "Last name is longer than first name"
else:
    result = "First name and last name are equal"

print(f"\nComparison result: {result}")
password = first_name[0] + last_name[-1] + str(len(first_name) + len(last_name))
print(f"\nGenerated password: {password}")

l = list(last_name)
l.pop()  # removes 1 original character
l.append("*")
l.insert(0, "@")
# l.pop()        
l.reverse()

print(f"\nList methods example on last name: {l}")
