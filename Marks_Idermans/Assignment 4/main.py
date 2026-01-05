#Marks Idermans
#mi24027

import string
import secrets
import os

def generate_password_from_info(first_name, last_name, phone, extra_digits=1, extra_symbols=1):
    first_name = first_name.strip()
    last_name = last_name.strip()
    phone = phone.replace(" ", "").replace("-", "")

    #Ensure first_name and last_name are long enough
    if len(first_name) < 2 or len(last_name) < 2 or len(phone) < 4:
        raise ValueError("First name, last name or phone number too short for password generation.")

    #password parts
    first_part = first_name[:2].upper()
    last_part = last_name[-2:].lower()
    phone_part = phone[-4:][::-1]

    #Add random digits
    digits_part = ''.join(secrets.choice(string.digits) for _ in range(extra_digits))
    
    #Add random symbols
    symbols_part = ''.join(secrets.choice(string.punctuation) for _ in range(extra_symbols))

    #Combine
    password = first_part + last_part + phone_part + digits_part + symbols_part

    #password is at least 8 characters long
    if len(password) < 8:
        # Pad with random digits if too short
        password += ''.join(secrets.choice(string.digits) for _ in range(8 - len(password)))

    #Save password to file
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

    return password

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Enter your phone number: ")

    #choose extra digits and symbols
    try:
        extra_digits = int(input("How many extra digits to add? (default 1): ") or 1)
        extra_symbols = int(input("How many extra symbols to add? (default 1): ") or 1)
    except ValueError:
        print("Invalid input, using 1 digit and 1 symbol by default.")
        extra_digits, extra_symbols = 1, 1

    password = generate_password_from_info(first_name, last_name, phone, extra_digits, extra_symbols)
    print(f"Generated password: {password}")
    print("Saved to:", os.path.abspath("passwords.txt"))
