import string
import secrets
import os

def generate_password_from_info():
    name = "".join([c for c in input("Your name:") if c not in " -"])
    surname = "".join([c for c in input("Your surname:") if c not in " -"])
    number = "".join([c for c in input("Your number:") if c not in " -"])

    digit_num = int(input("How many digits to generate:"))
    digits = "".join([str(secrets.choice(string.digits)) for _ in range(digit_num)])

    symbol_num = int(input("How many symbols to generate:"))
    symbols = "".join([str(secrets.choice(string.punctuation)) for _ in range(symbol_num)])

    pw = name[:2].upper() + surname[-2:].lower() + number[-4:][::-1] + digits + symbols

    if(len(pw)<8):
        # * The name and surname can't be smaller than 2 chars
        # * The number can't be smaller than 8 chars
        # * If the data is entered correctly the length of 8 is guaranteed 
        # even if the number of generated digits and symbols is set to 0
        print("\nThe data entered is incorrect!\n") 
    else:
        # Save each password in "passwords.txt"
        base_dir = os.path.dirname(__file__)    # current directory path (so that code still works the same when executed from the student folder)
        with open(base_dir+"/passwords.txt","a") as f:
            f.write(pw+"\n")
        print("\nOK!\n")
# Test the function
generate_password_from_info()