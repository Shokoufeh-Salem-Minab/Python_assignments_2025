import secrets


def generate_password_from_info(
    first_name: str,
    last_name: str,
    phone_number: str,
    numbers: int,
    symbols: int,
) -> str:
    last_name = "xx" + last_name
    phone_number = "0000" + phone_number
    password = (
        first_name[: min(2, len(first_name))].upper()
        + last_name[-min(2, len(last_name)) :].lower()
        + phone_number[-min(4, len(phone_number)) :][::-1]
        + "".join(str(secrets.randbelow(10)) for i in range(numbers))
        + "".join(secrets.choice("!@#$%^&*_+=`~") for i in range(symbols))
    )
    while len(password) < 8:
        password += str(secrets.randbelow(10))
    return password


def main() -> None:
    first_name = input("First name? ").strip()
    last_name = input("Last name? ").strip()
    phone_number = input("Phone number? ").strip().replace("-", "")
    numbers = int(input("How many numbers? ").strip())
    assert numbers >= 0
    symbols = int(input("How many symbols? ").strip())
    assert symbols >= 0

    password = generate_password_from_info(
        first_name, last_name, phone_number, numbers, symbols
    )

    with open("passwords.txt", "a", encoding="utf-8") as f:
        f.write(password + "\n")

    print("Password written to file passwords.txt")


if __name__ == "__main__":
    main()
