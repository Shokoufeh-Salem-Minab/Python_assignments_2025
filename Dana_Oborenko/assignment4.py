"""
Assignment 4: Password generator based on user's name + phone number.

Rules (base):
- First 2 letters of first name (uppercase)
- Last 2 letters of last name (lowercase)
- Last 4 digits of phone number reversed
- Add N random digits + M random symbols (user chooses)
Extra:
- Clean input (spaces/dashes)
- Ensure password length >= 8 (auto-increase digits if needed)
- Save to passwords.txt
"""

# to run programm 
# python3 Dana_Oborenko/assignment4.py


from __future__ import annotations

import re
import string
import secrets
from datetime import datetime
from pathlib import Path
from typing import Tuple


def _clean_name(value: str) -> str:
    """Remove spaces and non-letter characters. Keep letters only."""
    value = value.strip()
    # Keep only letters (Unicode). This allows names like "D'Angelo" -> "DAngelo"
    value = re.sub(r"[^A-Za-zÀ-ÿĀ-žА-Яа-яЁё]", "", value)
    return value


def _clean_phone(value: str) -> str:
    """Remove spaces, dashes, plus signs, parentheses. Keep digits only."""
    return re.sub(r"\D", "", value)


def _safe_two_letters_first(name: str) -> str:
    """Get first 2 letters of first name (uppercase). If shorter, pad with 'X'."""
    name = _clean_name(name)
    part = (name[:2] if len(name) >= 2 else (name + "XX")[:2]).upper()
    return part


def _safe_two_letters_last(surname: str) -> str:
    """Get last 2 letters of last name (lowercase). If shorter, pad with 'x'."""
    surname = _clean_name(surname)
    part = (surname[-2:] if len(surname) >= 2 else ("xx" + surname)[-2:]).lower()
    return part


def _last4_reversed(phone_digits: str) -> str:
    """Take last 4 digits and reverse them. If <4 digits, pad on the left with zeros."""
    phone_digits = _clean_phone(phone_digits)
    if len(phone_digits) < 4:
        phone_digits = phone_digits.zfill(4)
    return phone_digits[-4:][::-1]


def _random_digits(n: int) -> str:
    return "".join(secrets.choice(string.digits) for _ in range(max(0, n)))


def _random_symbols(n: int) -> str:
    # punctuation can include tricky quotes/backslashes — still allowed by the task
    return "".join(secrets.choice(string.punctuation) for _ in range(max(0, n)))


def generate_password_from_info(
    first_name: str,
    last_name: str,
    phone: str,
    extra_digits: int = 1,
    extra_symbols: int = 1,
    min_length: int = 8,
) -> Tuple[str, dict]:
    """
    Generate a password based on the task rules + extras.

    Returns:
        password, debug_info (parts used)
    """
    part_first = _safe_two_letters_first(first_name)
    part_last = _safe_two_letters_last(last_name)
    part_phone = _last4_reversed(phone)

    # Base password without extras:
    base = part_first + part_last + part_phone

    # User-chosen extras:
    digits_part = _random_digits(extra_digits)
    symbols_part = _random_symbols(extra_symbols)

    password = base + digits_part + symbols_part

    # Ensure minimum length: if too short, add more random digits at the end
    if len(password) < min_length:
        need = min_length - len(password)
        password = base + digits_part + _random_digits(need) + symbols_part

    debug = {
        "first_2_upper": part_first,
        "last_2_lower": part_last,
        "last4_reversed": part_phone,
        "extra_digits": extra_digits,
        "extra_symbols": extra_symbols,
        "final_length": len(password),
    }
    return password, debug


def _ask_int(prompt: str, default: int) -> int:
    raw = input(f"{prompt} (default {default}): ").strip()
    if raw == "":
        return default
    try:
        value = int(raw)
        return value if value >= 0 else default
    except ValueError:
        return default


def save_password_to_file(file_path: Path, first_name: str, last_name: str, phone: str, password: str) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)

    masked_phone = _clean_phone(phone)
    if len(masked_phone) > 4:
        masked_phone = "*" * (len(masked_phone) - 4) + masked_phone[-4:]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {first_name} {last_name} | phone:{masked_phone} | password:{password}\n"
    file_path.write_text(file_path.read_text(encoding="utf-8") + line if file_path.exists() else line, encoding="utf-8")


def main() -> None:
    print("=== Password Generator (Assignment 4) ===")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Enter your phone number: ")

    # Brain exercise: let user choose extras
    extra_digits = _ask_int("How many random digits to add?", default=1)
    extra_symbols = _ask_int("How many random symbols to add?", default=1)

    password, debug = generate_password_from_info(
        first_name=first_name,
        last_name=last_name,
        phone=phone,
        extra_digits=extra_digits,
        extra_symbols=extra_symbols,
        min_length=8,
    )

    print("\nGenerated password:", password)
    print("Details:", debug)

    # Save to file
    out_file = Path(__file__).parent / "passwords.txt"
    save_password_to_file(out_file, first_name, last_name, phone, password)
    print(f"Saved to: {out_file}")


if __name__ == "__main__":
    main()
