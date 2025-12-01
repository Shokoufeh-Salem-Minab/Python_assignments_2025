# Create a password generator based on user's name and phone number!
## Write a Python program that:

1. Asks for user's first name, last name, and phone number.
2. Cleans up the input (remove spaces or dashes).
3. Builds a password based on rules described below.
4. Prints the generated password.

**password rules**
1. Take first 2 letters of first name (uppercase).
2. Take last 2 letters of last name (lowercase).
3. Take last 4 digits of phone number and reverse them.
4. Add one random digit and one random symbol at the end.
5. Combine all parts without spaces.

**Example**
Input:
First name: Ivan
Last name: Doska
Phone: 09123456789

Steps:
- First 2 letters (uppercase): IV
- Last 2 letters (lowercase): ka
- Last 4 digits reversed: 9876
- Random digit: 4
- Random symbol: #

Output:
Generated password: IVka98764#

**Hints**

Use modules:

    import string
    
    import secrets

To pick random elements:

    secrets.choice(string.digits)
    secrets.choice(string.punctuation)

To reverse last 4 digits:

    last4 = phone[-4:][::-1]


    **Your brain exercise:** 

 • Let the user choose how many digits/symbols to add.
    
• Ensure password is at least 8 characters long.

• Save the result to a file 'passwords.txt'.

• Write a function generate_password_from_info().






