import regex as re
import secrets
import string
import assignment_3.file_operations as fo

# Ask user's input:
print("Enter first name:")
first_name = input()
print("Enter last name:")
last_name = input()
print("Enter phone number (without country code):")
phone_number = input()

print("How many random digits to add to the password?:")
random_digits_num = input()

print("How many random symbols to add to the password?:")
random_symbols_num = input()



# Password generator based on user's name and phone number!

# 1. Asks for user's first name, last name, and phone number.
# 2. Cleans up the input (remove spaces or dashes).
# 3. Builds a password based on rules described below.
# 4. Prints the generated password.
def generate_password_from_info(first_name, last_name, phone_number, random_digits_num, random_symbols_num):


    # Use regular expression to clean up everything from input
    # Keep only letters for names and digits for phone number
    first_name = re.sub(r'[^A-Za-z]', '', first_name)
    last_name = re.sub(r'[^A-Za-z]', '', last_name)
    phone_number = re.sub(r'[^0-9]', '', phone_number)
    random_digits_num = re.sub(r'[^0-9]', '', random_digits_num)
    random_symbols_num = re.sub(r'[^0-9]', '', random_symbols_num)

    # Password rule
    # 1. Take first 2 letters of first name (uppercase).
    # 2. Take last 2 letters of last name (lowercase).
    # 3. Take last 4 digits of phone number and reverse them.
    # 4. Add one random digit and one random symbol at the end.
    # 5. Combine all parts without spaces.

    # Random last 2 symbols for password:
    # Use string library for predefined list of symbols/characters
    digit = ""
    symbol = ""

    # Add n number of digits / symbols to the variables:
    for n in range(int(random_digits_num)):
       digit += secrets.choice(string.digits)
    for n in range(int(random_symbols_num)):
       symbol += secrets.choice(string.punctuation)

    # Use slicing for password generation:
    password = (first_name[:2].upper() +
                last_name[-2:] +
                phone_number[-4:][::-1] +
                digit +
                symbol
                )
    return password

generated_password = generate_password_from_info(first_name, last_name, phone_number, random_digits_num, random_symbols_num)

# Use module from assignemnt 3 to write password
def write_password(generated_password):
    base_directory = fo.os.path.dirname(fo.os.path.abspath(__file__)) # Path to the current file
    file_path = fo.os.path.join(base_directory, "password.txt") # Add exact location of password file
    
    fo.write_message(generated_password, file_path)
    print("Generated password is written to the password.txt file!")

if len(generated_password) >= 8:
    print(f"Generated password: {generated_password}")
    write_password(generated_password)
else:
    print("Password is too short! (min 8 characters)")