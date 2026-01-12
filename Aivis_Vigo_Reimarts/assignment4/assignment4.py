#!/usr/bin/env python3
"""
Advanced Password Generator
A comprehensive password generation tool with multiple features
"""

import string
import secrets
import re
from datetime import datetime
import json
import os


# ======================= PASSWORD GENERATION =======================

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, 
                     use_symbols=True, exclude_chars='', min_upper=1, min_lower=1, 
                     min_digits=1, min_symbols=1):
    """
    Generate a secure random password with customizable options.
    
    Args:
        length: Password length (default 12)
        use_upper: Include uppercase letters
        use_lower: Include lowercase letters
        use_digits: Include digits
        use_symbols: Include symbols
        exclude_chars: Characters to exclude
        min_upper/lower/digits/symbols: Minimum count for each type
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    # Build character pools
    upper_pool = string.ascii_uppercase
    lower_pool = string.ascii_lowercase
    digits_pool = string.digits
    symbols_pool = string.punctuation
    
    # Remove excluded characters
    if exclude_chars:
        upper_pool = ''.join(c for c in upper_pool if c not in exclude_chars)
        lower_pool = ''.join(c for c in lower_pool if c not in exclude_chars)
        digits_pool = ''.join(c for c in digits_pool if c not in exclude_chars)
        symbols_pool = ''.join(c for c in symbols_pool if c not in exclude_chars)
    
    # Build password with minimum requirements
    password_list = []
    
    if use_upper and upper_pool:
        password_list.extend(secrets.choice(upper_pool) for _ in range(min_upper))
    if use_lower and lower_pool:
        password_list.extend(secrets.choice(lower_pool) for _ in range(min_lower))
    if use_digits and digits_pool:
        password_list.extend(secrets.choice(digits_pool) for _ in range(min_digits))
    if use_symbols and symbols_pool:
        password_list.extend(secrets.choice(symbols_pool) for _ in range(min_symbols))
    
    # Build complete pool for remaining characters
    complete_pool = ''
    if use_upper: complete_pool += upper_pool
    if use_lower: complete_pool += lower_pool
    if use_digits: complete_pool += digits_pool
    if use_symbols: complete_pool += symbols_pool
    
    if not complete_pool:
        raise ValueError("No characters available for password generation")
    
    # Fill remaining length
    remaining = length - len(password_list)
    if remaining > 0:
        password_list.extend(secrets.choice(complete_pool) for _ in range(remaining))
    
    # Shuffle for security
    secrets.SystemRandom().shuffle(password_list)
    
    return ''.join(password_list[:length])


def generate_memorable_password(num_words=4, separator='-', capitalize=True, 
                               add_number=True, add_symbol=False):
    """Generate a memorable passphrase using random words."""
    word_list = [
        'apple', 'brave', 'cloud', 'delta', 'eagle', 'frost', 'globe', 'happy',
        'ivory', 'jolly', 'knife', 'laser', 'magic', 'noble', 'ocean', 'piano',
        'quest', 'royal', 'storm', 'tiger', 'ultra', 'vivid', 'waltz', 'xenon',
        'yield', 'zebra', 'amber', 'blaze', 'cyber', 'dream', 'echo', 'flash',
        'gamma', 'hydra', 'index', 'karma', 'lunar', 'metro', 'nexus', 'orbit',
        'prism', 'quark', 'radar', 'solar', 'theta', 'unity', 'viper', 'wave'
    ]
    
    words = [secrets.choice(word_list) for _ in range(num_words)]
    
    if capitalize:
        words = [word.capitalize() for word in words]
    
    passphrase = separator.join(words)
    
    if add_number:
        passphrase += separator + str(secrets.randbelow(9999)).zfill(2)
    
    if add_symbol:
        passphrase += secrets.choice('!@#$%')
    
    return passphrase


def generate_pin(length=4):
    """Generate a random PIN code."""
    return ''.join(secrets.choice(string.digits) for _ in range(length))


# ======================= PASSWORD STRENGTH CHECKER =======================

def check_password_strength(password):
    """Analyze password strength and return detailed feedback."""
    score = 0
    feedback = []
    length = len(password)
    
    # Length scoring
    if length >= 16:
        score += 30
    elif length >= 12:
        score += 25
    elif length >= 8:
        score += 15
        feedback.append("[WARNING] Increase length to 12+ characters")
    else:
        score += 5
        feedback.append("[ERROR] Password too short (minimum 8 characters)")
    
    # Character variety
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_symbol = bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))
    
    variety_score = sum([has_lower, has_upper, has_digit, has_symbol])
    score += variety_score * 12
    
    if not has_lower: feedback.append("[ERROR] Add lowercase letters")
    if not has_upper: feedback.append("[ERROR] Add uppercase letters")
    if not has_digit: feedback.append("[ERROR] Add numbers")
    if not has_symbol: feedback.append("[ERROR] Add special characters")
    
    # Bonus for high variety
    if variety_score == 4:
        score += 10
    
    # Check for patterns (penalties)
    patterns = {
        r'(.)\1{2,}': "[WARNING] Avoid repeating characters",
        r'(012|123|234|345|456|567|678|789|890)': "[WARNING] Avoid sequential numbers",
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)': "[WARNING] Avoid sequential letters"
    }
    
    for pattern, message in patterns.items():
        if re.search(pattern, password.lower()):
            score -= 10
            if message not in feedback:
                feedback.append(message)
    
    # Common words check
    common_words = ['password', 'admin', 'user', 'login', 'welcome', '12345', 'qwerty']
    for word in common_words:
        if word in password.lower():
            score -= 15
            feedback.append(f"[ERROR] Avoid common word: '{word}'")
            break
    
    # Calculate final score
    score = max(0, min(100, score))
    
    # Determine strength level
    if score >= 80:
        strength = "STRONG"
        color = "strong"
    elif score >= 60:
        strength = "GOOD"
        color = "good"
    elif score >= 40:
        strength = "FAIR"
        color = "fair"
    else:
        strength = "WEAK"
        color = "weak"
    
    if not feedback:
        feedback = ["[OK] Password meets all security requirements!"]
    
    return {
        'score': score,
        'strength': strength,
        'color': color,
        'feedback': feedback,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_symbol': has_symbol
    }


# ======================= FILE OPERATIONS =======================

def save_password(password, description="Generated Password", filename="passwords.txt"):
    """Save password to text file with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {description}: {password}\n"
    
    with open(filename, "a") as f:
        f.write(entry)
    
    print(f"[SUCCESS] Password saved to {filename}")


def save_password_json(password_data, filename="password_history.json"):
    """Save password with metadata in JSON format."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"passwords": []}
    
    entry = {
        "timestamp": datetime.now().isoformat(),
        "password": password_data.get("password", ""),
        "length": len(password_data.get("password", "")),
        "type": password_data.get("type", "standard"),
        "strength": password_data.get("strength", {}),
        "description": password_data.get("description", "")
    }
    
    data["passwords"].append(entry)
    
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def view_password_history(filename="passwords.txt"):
    """View saved passwords."""
    try:
        with open(filename, "r") as f:
            content = f.read()
            if content:
                print("\n" + "="*60)
                print("PASSWORD HISTORY")
                print("="*60)
                print(content)
            else:
                print("[ERROR] No password history found")
    except FileNotFoundError:
        print("[ERROR] No password history file found")


def get_statistics(filename="password_history.json"):
    """Get password generation statistics."""
    try:
        with open(filename, "r") as f:
            data = json.load(f)
        
        passwords = data.get("passwords", [])
        if not passwords:
            print("[ERROR] No statistics available")
            return
        
        total = len(passwords)
        avg_length = sum(p.get("length", 0) for p in passwords) / total
        
        types = {}
        for p in passwords:
            ptype = p.get("type", "unknown")
            types[ptype] = types.get(ptype, 0) + 1
        
        print("\n" + "="*60)
        print("STATISTICS")
        print("="*60)
        print(f"Total passwords generated: {total}")
        print(f"Average password length: {avg_length:.1f}")
        print(f"\nPassword types:")
        for ptype, count in types.items():
            print(f"  - {ptype}: {count}")
        print("="*60)
        
    except (FileNotFoundError, json.JSONDecodeError):
        print("[ERROR] No statistics available")


# ======================= USER INTERFACE =======================

def print_header():
    """Print application header."""
    print("\n" + "="*60)
    print(" ADVANCED PASSWORD GENERATOR".center(60))
    print("="*60)


def print_menu():
    """Display main menu."""
    menu = """
MENU OPTIONS:
============================================================
  1. Generate Standard Password
  2. Generate Custom Password (Advanced Options)
  3. Generate Memorable Passphrase
  4. Generate Multiple Passwords
  5. Generate PIN Code
  6. Check Password Strength
  7. View Password History
  8. View Statistics
  9. Exit
============================================================
"""
    print(menu)


def get_int_input(prompt, default=None, min_val=None, max_val=None):
    """Get integer input with validation."""
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input and default is not None:
                return default
            
            value = int(user_input)
            
            if min_val is not None and value < min_val:
                print(f"[ERROR] Value must be at least {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"[ERROR] Value must be at most {max_val}")
                continue
            
            return value
        except ValueError:
            print("[ERROR] Please enter a valid number")


def get_yes_no(prompt, default=True):
    """Get yes/no input."""
    default_str = "Y/n" if default else "y/N"
    user_input = input(f"{prompt} ({default_str}): ").strip().lower()
    
    if not user_input:
        return default
    
    return user_input in ['y', 'yes']


def display_password(password, strength_info=None):
    """Display password with formatting."""
    print("\n" + "="*60)
    print(f"Generated Password: {password}")
    print(f"Length: {len(password)} characters")
    
    if strength_info:
        print(f"Strength: {strength_info['strength']} (Score: {strength_info['score']}/100)")
        print("\nFeedback:")
        for item in strength_info['feedback']:
            print(f"   {item}")
    
    print("="*60)


# ======================= MAIN PROGRAM =======================

def option_1_standard():
    """Generate standard password."""
    length = get_int_input("Enter password length (default 16): ", default=16, min_val=4, max_val=128)
    
    password = generate_password(length=length)
    strength = check_password_strength(password)
    
    display_password(password, strength)
    
    if get_yes_no("Save this password?", default=False):
        desc = input("Enter description (optional): ").strip() or "Standard Password"
        save_password(password, desc)
        save_password_json({
            "password": password,
            "type": "standard",
            "strength": strength,
            "description": desc
        })


def option_2_custom():
    """Generate custom password with advanced options."""
    print("\nCustom Password Options")
    print("-"*60)
    
    length = get_int_input("Password length: ", default=16, min_val=4, max_val=128)
    
    use_upper = get_yes_no("Include uppercase letters?", True)
    use_lower = get_yes_no("Include lowercase letters?", True)
    use_digits = get_yes_no("Include digits?", True)
    use_symbols = get_yes_no("Include symbols?", True)
    
    exclude = input("Characters to exclude (leave empty for none): ").strip()
    
    try:
        password = generate_password(
            length=length,
            use_upper=use_upper,
            use_lower=use_lower,
            use_digits=use_digits,
            use_symbols=use_symbols,
            exclude_chars=exclude
        )
        
        strength = check_password_strength(password)
        display_password(password, strength)
        
        if get_yes_no("Save this password?", default=False):
            desc = input("Enter description (optional): ").strip() or "Custom Password"
            save_password(password, desc)
            save_password_json({
                "password": password,
                "type": "custom",
                "strength": strength,
                "description": desc
            })
    
    except ValueError as e:
        print(f"[ERROR] {e}")


def option_3_memorable():
    """Generate memorable passphrase."""
    print("\nMemorable Passphrase Options")
    print("-"*60)
    
    num_words = get_int_input("Number of words (default 4): ", default=4, min_val=2, max_val=8)
    separator = input("Word separator (default '-'): ").strip() or '-'
    capitalize = get_yes_no("Capitalize words?", True)
    add_number = get_yes_no("Add number at end?", True)
    add_symbol = get_yes_no("Add symbol at end?", False)
    
    passphrase = generate_memorable_password(
        num_words=num_words,
        separator=separator,
        capitalize=capitalize,
        add_number=add_number,
        add_symbol=add_symbol
    )
    
    strength = check_password_strength(passphrase)
    display_password(passphrase, strength)
    
    if get_yes_no("Save this passphrase?", default=False):
        desc = input("Enter description (optional): ").strip() or "Memorable Passphrase"
        save_password(passphrase, desc)
        save_password_json({
            "password": passphrase,
            "type": "memorable",
            "strength": strength,
            "description": desc
        })


def option_4_multiple():
    """Generate multiple passwords."""
    count = get_int_input("How many passwords to generate? ", default=5, min_val=1, max_val=20)
    length = get_int_input("Password length: ", default=16, min_val=4, max_val=128)
    
    print(f"\nGenerating {count} passwords...")
    print("="*60)
    
    for i in range(1, count + 1):
        password = generate_password(length=length)
        print(f"{i:2d}. {password}")
    
    print("="*60)


def option_5_pin():
    """Generate PIN code."""
    length = get_int_input("PIN length (default 4): ", default=4, min_val=4, max_val=12)
    
    pin = generate_pin(length)
    
    print("\n" + "="*60)
    print(f"Generated PIN: {pin}")
    print(f"Length: {length} digits")
    print("="*60)
    
    if get_yes_no("Save this PIN?", default=False):
        desc = input("Enter description (optional): ").strip() or f"{length}-digit PIN"
        save_password(pin, desc)


def option_6_check():
    """Check password strength."""
    password = input("\nEnter password to check: ").strip()
    
    if not password:
        print("[ERROR] No password entered")
        return
    
    strength = check_password_strength(password)
    display_password(password, strength)


def main():
    """Main program loop."""
    print_header()
    print("Welcome to the Advanced Password Generator!")
    print("Generate secure passwords with multiple options and features.")
    
    while True:
        print_menu()
        choice = input("Select an option (1-9): ").strip()
        
        if choice == '1':
            option_1_standard()
        elif choice == '2':
            option_2_custom()
        elif choice == '3':
            option_3_memorable()
        elif choice == '4':
            option_4_multiple()
        elif choice == '5':
            option_5_pin()
        elif choice == '6':
            option_6_check()
        elif choice == '7':
            view_password_history()
        elif choice == '8':
            get_statistics()
        elif choice == '9':
            print("\nThank you for using Advanced Password Generator!")
            print("Stay secure!\n")
            break
        else:
            print("[ERROR] Invalid option. Please select 1-9.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()