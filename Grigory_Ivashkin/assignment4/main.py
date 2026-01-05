import string
import secrets
import os

def clean_phone(phone):
    # remove spaces and dashes
    #.replace function is used to replace " " and "-", "+" to "" in phone numbers
    #e.g. +371 000-0-00 00 will become 37100000000
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")
    phone = phone.replace("+", "")
    return phone


def generate_password_from_info(first_name, last_name, phone, digits_count, symbols_count):
# cleaning
# i explained how .strip() works in the first assignment
    first_name = first_name.strip()
    last_name = last_name.strip()
    phone = clean_phone(phone)

# we take the first 2 letters from name and set the to uppercase
#and we take 2 last digits and set them to lowercase
    first2 = first_name[:2].upper()
    last2 = last_name[-2:].lower()

# we check one by one if the symbols in phone is digits
# e.g. if phone is 000p0000, we will take only 0000000. we will ignore p.
    only_digits = ""
    for ch in phone:
        if ch.isdigit():
            only_digits += ch

# we take only digits that we found, take last 4 of them, reversing them.
    last4_reversed = only_digits[-4:][::-1]

# if phone has less than 4 digits, still works (will just take what exists)
    password = first2 + last2 + last4_reversed

# add random digits
# _ is the same as i (e.g. for i in range...), so, in terms of optimisation, we use _
    for _ in range(digits_count):
        # secrets is a python module for safety. ( for passwords for exaple). choice() is a function to take random symbol from the line
        # the line is declared by string.digits (0123456789)
        password += secrets.choice(string.digits)

# add random symbols
    for _ in range(symbols_count):
        # string.punctuation (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
        password += secrets.choice(string.punctuation)

    # ensure password is at least 8 characters
    # if password is shorter than 8 digits ( in case, user inputed the invalid phone number, or choused not enough random symbols and 
    # digits, wil will add some random digits to his password)
    while len(password) < 8:
        password += secrets.choice(string.digits)

    return password

# i explained all this things in previous assignement
def save_password_to_file(password, filename="passwords.txt"):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, filename)

    with open(path, "a", encoding="utf-8") as f:
        f.write(password + "\n")

# _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

first_name = input("First name: ")
last_name = input("Last name: ")
phone = input("Phone number: ")

digits_count = int(input("How many random digits to add? "))
symbols_count = int(input("How many random symbols to add? "))

generated = generate_password_from_info(first_name, last_name, phone, digits_count, symbols_count)

print("Generated password:", generated)

save_password_to_file(generated)
print("Saved to passwords.txt")
