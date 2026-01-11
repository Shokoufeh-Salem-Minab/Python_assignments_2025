import string
import secrets

# function to generate password from user info
def generate_password_from_info(first_name, last_name, phone, num_digits=1, num_symbols=1):
    # get first 2 letters of first name in uppercase
    first_part = first_name[:2].upper()
    
    # get last 2 letters of last name in lowercase with slicing 
    last_part = last_name[-2:].lower()
    
    # get last 4 digits of phone and reverse them
    last4 = phone[-4:][::-1]
    
    # add random digits
    random_digits = ""
    for i in range(num_digits):
        random_digits += secrets.choice(string.digits)
    
    # add random symbols
    random_symbols = ""
    for i in range(num_symbols):
        random_symbols += secrets.choice(string.punctuation)
    
    # combine everything
    password = first_part + last_part + last4 + random_digits + random_symbols
    
    return password

# clean up input by removing spaces and dashes
def clean_input(text):
    cleaned = text.replace(" ", "").replace("-", "")
    return cleaned

# save password to file
def save_to_file(name, password):
    with open("passwords.txt", "a") as f:
        f.write(f"{name}: {password}\n")
    print("password saved to passwords.txt")

# main program
print("password generator\n")

# ask for user info
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
phone = input("enter your phone number: ")

# clean up the inputs
first_name = clean_input(first_name)
last_name = clean_input(last_name)
phone = clean_input(phone)

# ask user how many random digits and symbols they want
try:
    num_digits = int(input("how many random digits to add? (press enter for 1): ") or "1")
    num_symbols = int(input("how many random symbols to add? (press enter for 1): ") or "1")
except:
    num_digits = 1
    num_symbols = 1
    print("using default: 1 digit and 1 symbol")

# generate password
password = generate_password_from_info(first_name, last_name, phone, num_digits, num_symbols)

# make sure password is at least 8 characters
if len(password) < 8:
    print("\nwarning: password is too short, adding more random characters...")
    while len(password) < 8:
        password += secrets.choice(string.digits + string.punctuation)

# show the password
print(f"\ngenerated password: {password}")
print(f"password length: {len(password)} characters")

# save to file
save_choice = input("\nsave this password to file? (y/n): ")
if save_choice.lower() == 'y':
    full_name = first_name + " " + last_name
    save_to_file(full_name, password)

print("\ndone!")