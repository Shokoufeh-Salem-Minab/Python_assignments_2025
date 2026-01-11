import string
import secrets

def generate_password_from_info(first_name: str, last_name: str, phone: str, extra_digits: int, extra_symbols: int) -> str:
    first_name = first_name.strip()
    last_name = last_name.strip()
    phone = phone.replace(" ", "").replace("-", "")
    part1 = first_name[:2].upper()
    part2 = last_name[-2:].lower()
    part3 = phone[-4:][::-1]
    rand_digits = "".join(secrets.choice(string.digits) for _ in range(extra_digits))
    rand_symbols = "".join(secrets.choice(string.punctuation) for _ in range(extra_symbols))
    password = part1 + part2 + part3 + rand_digits + rand_symbols
    while len(password) < 8: # Ensure minimum length
        password += secrets.choice(string.ascii_letters + string.digits)

    return password

first_name = input("First name: ")
last_name = input("Last name: ")
phone = input("Phone number: ")
extra_digits = int(input("How many extra digits to add? "))
extra_symbols = int(input("How many extra symbols to add? "))
password = generate_password_from_info(first_name, last_name, phone, extra_digits, extra_symbols)
print(f"Generated password: {password}")
with open("passwords.txt", "a", encoding="utf-8") as f:
    f.write(password + "\n")