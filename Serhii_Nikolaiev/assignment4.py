import string
import secrets


def generate_password_from_info():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone_number = input("Enter your phone number: ")

    try:
        digits_to_add = int(input("Enter number of digits to add: "))
        symbols_to_add = int(input("Enter number of symbols to add: "))
    except ValueError:
        raise TypeError("Please enter a valid integer.")

    if (
        len(first_name) < 2
        or len(last_name) < 2
        or len(phone_number) < 6
        or digits_to_add < 0
        or symbols_to_add < 0
    ):
        print(
            "Seriously?? "
            "Do not waste computational power and time if you don't"
            " bother filling out first name and last name and phone number and digits to add and symbols to add. "
            "If you're not willing to provide complete information, don't expect me to run AT ALL."
        )
        exit(1)

    first_name = first_name.strip()
    last_name = last_name.strip()
    phone_number = phone_number.strip()
    phone_number = phone_number.replace("-", "")

    last_4_nums = phone_number[-4:][::-1]
    result = first_name[:2].upper() + last_name[-2:].lower() + last_4_nums

    for _ in range(digits_to_add):
        result += secrets.choice(string.digits)
    for _ in range(symbols_to_add):
        result += secrets.choice(string.punctuation)

    with open("passwords.txt", "w", encoding="utf-8") as file:
        file.write(result)


if __name__ == "__main__":
    generate_password_from_info()
