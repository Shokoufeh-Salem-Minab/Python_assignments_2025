import string
import secrets

def passwordGen(firstName, lastName, phoneNum, count):
    firstName = firstName.strip()
    lastName = lastName.strip()
    phoneNum = phoneNum.replace(" ", "").replace("-", "")

    part1 = firstName[:2].upper()
    part2 = lastName[-2:].lower()
    part3 = phoneNum[-4:][::-1]

    extras = ""
    for _ in range(count):
        extras += secrets.choice(string.digits + string.punctuation)

    password = part1 + part2 + part3 + extras

    # ensure at least 8 chars
    while len(password) < 8:
        password += secrets.choice(string.digits)

    return password

firstName = input("First name: ")
lastName = input("Last name: ")
phoneNum = input("Phone number: ")
extra = int(input("How many extra digits/symbols? "))

password = passwordGen(firstName, lastName, phoneNum, extra)

print("Generated password:", password)

with open("assignment4/passwords.txt", "a") as f:
    f.write(password + "\n")
