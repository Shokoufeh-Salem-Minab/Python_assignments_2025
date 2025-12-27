import string
import secrets

def generate_password_from_info(first_name, last_name, phone_number, num_digits=1, num_symbols=1):
    first_name = first_name.strip()
    last_name = last_name.strip()
    phone_number = phone_number.replace(" ", "").replace("-", "")
    
    first_part = first_name[:2].upper()
    last_part = last_name[-2:].lower()
    reversed_phone = phone_number[-4:][::-1]
    random_digits = ''.join(secrets.choice(string.digits) for _ in range(num_digits))
    random_symbols = ''.join(secrets.choice(string.punctuation) for _ in range(num_symbols))
    
    password = first_part + last_part + reversed_phone + random_digits + random_symbols
    
    if len(password) < 8:
        needed = 8 - len(password)
        password += ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(needed))
    
    return password

def save_password_to_file(password):
    with open("password.txt", "a") as f:
        f.write(f"{password}\n")

print("Password Generator")
first = input("First name: ")
last = input("Last name: ")
phone_num = input("Phone number: ")

while True:
    try:
        num_digits = int(input("Digits to add: ") or "1")
        num_symbols = int(input("Symbols to add: ") or "1")
        break
    except:
        print("Enter valid numbers.")

password = generate_password_from_info(first, last, phone_num, num_digits, num_symbols)

print(f"Password: {password}")
save_password_to_file(password)
print("Saved to 'passwords.txt'")