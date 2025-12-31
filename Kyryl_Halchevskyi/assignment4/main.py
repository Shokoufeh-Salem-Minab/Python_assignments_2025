import string
import secrets

def generate_password_from_info(first_name, last_name, phone, num_digits, num_symbols):
    """Generate a password based on user information"""
    
    # Clean up inputs - remove spaces and dashes
    first_name = first_name.replace(" ", "").replace("-", "")
    last_name = last_name.replace(" ", "").replace("-", "")
    phone = phone.replace(" ", "").replace("-", "")
    
    # Step 1: First 2 letters of first name (uppercase)
    first_part = first_name[:2].upper()
    
    # Step 2: Last 2 letters of last name (lowercase)
    last_part = last_name[-2:].lower()
    
    # Step 3: Last 4 digits of phone reversed
    last4 = phone[-4:]
    reversed_digits = last4[::-1]
    
    # Step 4: Add random digits
    random_digits = ""
    for i in range(num_digits):
        random_digits = random_digits + secrets.choice(string.digits)
    
    # Step 5: Add random symbols
    random_symbols = ""
    for i in range(num_symbols):
        random_symbols = random_symbols + secrets.choice(string.punctuation)
    
    # Combine all parts
    password = first_part + last_part + reversed_digits + random_digits + random_symbols
    
    return password

def save_password_to_file(first_name, last_name, password):
    """Save the password to a file"""
    with open("passwords.txt", "a") as file:
        file.write(f"Name: {first_name} {last_name} | Password: {password}\n")
    print("Password saved to 'passwords.txt'!")

# Main Program
print("=== PASSWORD GENERATOR ===\n")

# Get user input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
phone = input("Enter your phone number: ")

# Let user choose how many random characters to add
print("\n--- Customization ---")
num_digits = int(input("How many random digits to add? (default 1): ") or "1")
num_symbols = int(input("How many random symbols to add? (default 1): ") or "1")

# Generate password
password = generate_password_from_info(first_name, last_name, phone, num_digits, num_symbols)

# Display the password
print("\n--- Password Generation Steps ---")
clean_first = first_name.replace(" ", "").replace("-", "")
clean_last = last_name.replace(" ", "").replace("-", "")
clean_phone = phone.replace(" ", "").replace("-", "")

print(f"First 2 letters (uppercase): {clean_first[:2].upper()}")
print(f"Last 2 letters (lowercase): {clean_last[-2:].lower()}")
print(f"Last 4 digits reversed: {clean_phone[-4:][::-1]}")

print(f"\nGenerated password: {password}")
print(f"Password length: {len(password)} characters")

# Check if password is at least 8 characters
if len(password) < 8:
    print("⚠️ Warning: Password is shorter than 8 characters!")
else:
    print("✓ Password meets minimum length requirement!")

# Save to file
print()
save_password_to_file(first_name, last_name, password)

print("\n=== END OF PROGRAM ===")