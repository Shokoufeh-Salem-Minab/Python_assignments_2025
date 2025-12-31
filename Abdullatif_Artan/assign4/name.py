import string
import secrets


def generate_password_from_info(first_name, last_name, phone, extra_count):
   
    first_name = first_name.strip()
    last_name = last_name.strip()
    phone = phone.replace(" ", "").replace("-", "")

    
    part1 = first_name[:2].upper()

    
    part2 = last_name[-2:].lower()

    
    part3 = phone[-4:][::-1]

    
    random_part = ""
    for _ in range(extra_count):
        random_part += secrets.choice(string.digits)
        random_part += secrets.choice(string.punctuation)

    password = part1 + part2 + part3 + random_part

    
    while len(password) < 8:
        password += secrets.choice(string.digits)

    return password




first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
phone = input("Enter phone number: ")
extra_count = int(input("How many extra digit-symbol pairs to add? "))

password = generate_password_from_info(first_name, last_name, phone, extra_count)

print("Generated password:", password)

# Save to file
with open("passwords.txt", "a") as file:
    file.write(password + "\n")
