import string

import secrets

def generate_password_from_info(first_name, last_name, phone_number, des_nums, des_symbols) -> str:
    password = (first_name[:2].upper() + 
        last_name[-2:].lower() + 
        phone_number[-4:][::-1] + 
        "".join(str(secrets.choice(string.digits)) for i in range(des_nums)) + 
        "".join(secrets.choice(string.punctuation) for i in range(des_symbols))
    )

    return password

def main() -> None:
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone_number = input("Phone number: ").strip()

    phone_number = phone_number[1:]

    numbers = int(input("Numbers: ").strip())
    assert numbers >= 0

    symbols = int(input("Numbers: ").strip())
    assert numbers >= 0
    
    password = generate_password_from_info(
        first_name, last_name, phone_number, numbers, symbols
    )
    
    print(password)

    with open("password.txt", "a") as f:
        f.write(password + "\n")

if __name__ == "__main__":
    main()
