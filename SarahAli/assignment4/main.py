import string
import secrets
import os

def generate_password_from_info():
    # Get folder where this file is located
    current_folder = os.path.dirname(__file__)
    file_path = os.path.join(current_folder, "passwords.txt")

    # Ask user for input
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")

    # Clean phone number
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    # Password parts
    part1 = first_name[0:2].upper()
    part2 = last_name[-2:].lower()
    part3 = phone[-4:][::-1]

    num_digits = int(input("How many random digits to add? "))
    num_symbols = int(input("How many random symbols to add? "))

    extra = ""

    for i in range(num_digits):
        extra = extra + secrets.choice(string.digits)

    for i in range(num_symbols):
        extra = extra + secrets.choice(string.punctuation)

    password = part1 + part2 + part3 + extra

    while len(password) < 8:
        password = password + secrets.choice(string.digits)

    print("Generated password:", password)

    # Save to passwords.txt INSIDE assignment4 folder
    file = open(file_path, "a")
    file.write(password + "\n")
    file.close()


generate_password_from_info()
