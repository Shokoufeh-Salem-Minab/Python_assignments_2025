firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

print("Length of first name:", len(firstName))
print("Length of last name:", len(lastName))

vowels = "aeiouAEIOU"

vowelCount = 0
consonantCount = 0

for chars in firstName:
    if chars.isalpha():
        if chars in vowels:
            vowelCount += 1
        else:
            consonantCount += 1

print("Vowels in first name:", vowelCount)
print("Consonants in first name:", consonantCount)
print("First name (upper):", firstName.upper())
print("First name (lower):", firstName.lower())
print("Last name (reversed):", lastName[::-1])

print("Characters in first name (for loop):")
for ch in firstName:
    print(ch, end=" ")
print()

tempName = firstName
print("Characters in first name (while loop):")
while tempName:
    print(tempName[0], end=" ")
    tempName = tempName[1:]
print()

if len(firstName) > len(lastName):
    print("First name is longer than last name.")
elif len(firstName) < len(lastName):
    print("Last name is longer than first name.")
else:
    print("First name and last name are equal in length.")

password = firstName[0] + lastName[-1] + str(len(firstName) + len(lastName))
print("Generated password:", password)

chars = list(lastName)
chars.append("*")
chars.insert(0, "@")
chars.pop()
chars.reverse()
print("Final list:", chars)
