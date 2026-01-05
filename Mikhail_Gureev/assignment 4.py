import string
import secrets

def generate_password_from_info(first_name, last_name, phone, extra_digits=1, extra_symbols=1):
    # Clean inputs
    first_name = first_name.replace(" ", "")
    last_name = last_name.replace(" ", "")
    phone = phone.replace(" ", "").replace("-", "")
    
    # Take first 2 letters of first name (uppercase)
    part1 = first_name[:2].upper()
    
    # Take last 2 letters of last name (lowercase)
    part2 = last_name[-2:].lower()
    
    # Take last 4 digits of phone number and reverse
    part3 = phone[-4:][::-1]
    
    # Add random digits
    random_digits = ''.join(secrets.choice(string.digits) for _ in range(extra_digits))
    
    # Add random symbols
    random_symbols = ''.join(secrets.choice(string.punctuation) for _ in range(extra_symbols))
    
    # Combine all parts
    password = part1 + part2 + part3 + random_digits + random_symbols
    
    # Ensure password is at least 8 characters long
    if len(password) < 8:
        # Add extra random digits if too short
        while len(password) < 8:
            password += secrets.choice(string.digits)
    
    return password

# --- Main Program ---
# Ask for user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone = input("Enter your phone number: ")

# Ask how many extra digits/symbols to add
extra_digits = int(input("How many extra random digits to add? "))
extra_symbols = int(input("How many extra random symbols to add? "))

# Generate password
password = generate_password_from_info(first_name, last_name, phone, extra_digits, extra_symbols)

# Print password
print("Generated password:", password)

# Save to file
with open("passwords.txt", "a") as file:
    file.write(password + "\n")
