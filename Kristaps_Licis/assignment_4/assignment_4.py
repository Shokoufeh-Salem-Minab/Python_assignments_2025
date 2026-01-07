import string
import secrets
from datetime import datetime


def clean_input(text):
    """
    Clean input by removing spaces and dashes.
    
    Args:
        text (str): Input string to clean
    
    Returns:
        str: Cleaned string
    """
    return text.replace(" ", "").replace("-", "")


def generate_password_from_info(first_name, last_name, phone, num_digits=1, num_symbols=1):
    """
    Generate a password based on user's personal information.
    
    Args:
        first_name (str): User's first name
        last_name (str): User's last name
        phone (str): User's phone number
        num_digits (int): Number of random digits to add (default 1)
        num_symbols (int): Number of random symbols to add (default 1)
    
    Returns:
        str: Generated password
    """
    # Clean inputs
    first_name = clean_input(first_name)
    last_name = clean_input(last_name)
    phone = clean_input(phone)
    
    # Validate inputs
    if len(first_name) < 2:
        raise ValueError("First name must be at least 2 characters long")
    if len(last_name) < 2:
        raise ValueError("Last name must be at least 2 characters long")
    if len(phone) < 4:
        raise ValueError("Phone number must have at least 4 digits")
    
    # Build password components
    # 1. First 2 letters of first name (uppercase)
    part1 = first_name[:2].upper()
    
    # 2. Last 2 letters of last name (lowercase)
    part2 = last_name[-2:].lower()
    
    # 3. Last 4 digits of phone reversed
    last4 = phone[-4:]
    part3 = last4[::-1]
    
    # 4. Random digits
    random_digits = ''.join(secrets.choice(string.digits) for _ in range(num_digits))
    
    # 5. Random symbols
    random_symbols = ''.join(secrets.choice(string.punctuation) for _ in range(num_symbols))
    
    # Combine all parts
    password = part1 + part2 + part3 + random_digits + random_symbols
    
    # Ensure password is at least 8 characters
    while len(password) < 8:
        password += secrets.choice(string.ascii_letters + string.digits)
    
    return password


def save_password_to_file(filename, first_name, last_name, phone, password):
    """
    Save generated password to a file with timestamp.
    
    Args:
        filename (str): Output filename
        first_name (str): User's first name
        last_name (str): User's last name
        phone (str): User's phone number
        password (str): Generated password
    """
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"\n{'='*70}\n")
            file.write(f"Generated: {timestamp}\n")
            file.write(f"User: {first_name} {last_name}\n")
            file.write(f"Phone: {phone}\n")
            file.write(f"Password: {password}\n")
            file.write(f"Length: {len(password)} characters\n")
        
        print(f"\n✓ Password saved to '{filename}'")
        return True
    except Exception as e:
        print(f"\n✗ Error saving to file: {e}")
        return False


def main():
    """Main program function."""
    print("="*70)
    print("PASSWORD GENERATOR")
    print("="*70)
    print("\nThis program generates a secure password based on your information.")
    print("\nPassword Rules:")
    print("  • First 2 letters of first name (UPPERCASE)")
    print("  • Last 2 letters of last name (lowercase)")
    print("  • Last 4 digits of phone number (reversed)")
    print("  • Random digits and symbols")
    print("  • Minimum 8 characters total")
    
    # Get user input
    print("\n" + "-"*70)
    print("ENTER YOUR INFORMATION")
    print("-"*70)
    
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    phone = input("Phone number: ").strip()
    
    # Ask user for customization
    print("\n" + "-"*70)
    print("CUSTOMIZATION OPTIONS")
    print("-"*70)
    
    try:
        num_digits = int(input("How many random digits to add? (default 1): ") or "1")
        num_symbols = int(input("How many random symbols to add? (default 1): ") or "1")
    except ValueError:
        print("Invalid input. Using defaults (1 digit, 1 symbol).")
        num_digits = 1
        num_symbols = 1
    
    # Generate password
    print("\n" + "-"*70)
    print("GENERATING PASSWORD")
    print("-"*70)
    
    try:
        password = generate_password_from_info(
            first_name, 
            last_name, 
            phone, 
            num_digits, 
            num_symbols
        )
        
        # Display breakdown
        cleaned_first = clean_input(first_name)
        cleaned_last = clean_input(last_name)
        cleaned_phone = clean_input(phone)
        
        print("\nPassword Breakdown:")
        print(f"  First 2 letters (uppercase): {cleaned_first[:2].upper()}")
        print(f"  Last 2 letters (lowercase): {cleaned_last[-2:].lower()}")
        print(f"  Last 4 digits reversed: {cleaned_phone[-4:][::-1]}")
        print(f"  Random digits: {num_digits} digit(s)")
        print(f"  Random symbols: {num_symbols} symbol(s)")
        
        print("\n" + "="*70)
        print(f"Generated password: {password}")
        print(f"Password length: {len(password)} characters")
        print("="*70)
        
        # Save to file
        save_to_file = input("\nSave password to 'passwords.txt'? (y/n): ").strip().lower()
        if save_to_file == 'y':
            save_password_to_file('passwords.txt', first_name, last_name, phone, password)
        
        # Generate another password?
        print("\n" + "-"*70)
        another = input("Generate another password with same info? (y/n): ").strip().lower()
        
        if another == 'y':
            print("\nGenerating new password...")
            new_password = generate_password_from_info(
                first_name, 
                last_name, 
                phone, 
                num_digits, 
                num_symbols
            )
            print(f"\nNew password: {new_password}")
            print(f"Length: {len(new_password)} characters")
            
            if input("\nSave this one too? (y/n): ").strip().lower() == 'y':
                save_password_to_file('passwords.txt', first_name, last_name, phone, new_password)
        
    except ValueError as e:
        print(f"\n✗ Error: {e}")
        return
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return
    
    print("\n" + "="*70)
    print("THANK YOU FOR USING PASSWORD GENERATOR!")
    print("="*70)


if __name__ == "__main__":
    main()
