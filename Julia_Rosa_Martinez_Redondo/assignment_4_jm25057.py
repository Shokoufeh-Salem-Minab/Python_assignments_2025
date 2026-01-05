# ~~~~~~~~A C T I V I T Y 4 PYTHON , to generate password~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

import string   # importing libraries usefuls
import secrets


# ~~~~~~~~FUNCTION~~~~~~~~
def generate_password_from_info(name, sur_name, phone_num, extra_stuff):

    # clean inputs (removing spaces & -)
    name = name.strip()
    sur_name = sur_name.strip()
    phone_num = phone_num.replace(" ", "").replace("-", "")

    # first 2 letters name (upper)
    part1 = name[:2].upper()

    # last 2 letters surname (lower)
    part2 = sur_name[-2:].lower()

    # last 4 digits phone reversed
    last4 = phone_num[-4:][::-1]
    pwd = part1 + part2 + last4
    # add random digits 6 symbols
    count = 0
    while count < extra_stuff:
        pwd += secrets.choice(string.digits)
        pwd += secrets.choice(string.punctuation)
        count += 1
    # ensure password has at least 8 chars
    while len(pwd) < 8:
        pwd += secrets.choice(string.digits)

    return pwd


# ~~~~~~~~INPUT~~~~~~~~
name = input("enter 1st name: ")
sur_name = input("enter surname: ")
phone_num = input("enter phone number: ")
extra_stuff = int(input("how many extra digits or aka symbols?: "))

# ~~~~~~~~PASSWORD CREATION~~~~~~~~
final_pwd = generate_password_from_info(name, sur_name, phone_num, extra_stuff)
print("generated password resulting:", final_pwd)

# ~~~~~~~~SAVE TO FILE~~~~~~~~
file = open("passwords.txt", "a")
file.write(final_pwd + "\n")
file.close()
