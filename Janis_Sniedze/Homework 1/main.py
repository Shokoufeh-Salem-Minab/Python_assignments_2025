# Jānis Sniedze
# js23127
# Homework 8
# Final edit date: 30/12/2025


def main():
    firstName = input("Enter your first name: ").strip()  # read and trim the user's first name input
    lastName = input("Enter your last name: ").strip()  # read and trim the user's last name input
    firstNameLen = len(firstName)  
    lastNameLen = len(lastName)  
    vowels = set("aeiouAEIOU")
    vowelCount = sum(1 for ch in firstName if ch in vowels)  # count vowels occurring in the first name
    consonantCount = sum(1 for ch in firstName if ch.isalpha() and ch not in vowels)  # count consonants in first name

    print(f"Length of first name: {firstNameLen}")  # display the computed length of the first name
    print(f"Length of last name: {lastNameLen}")  # display the computed length of the last name
    print(f"Vowels in first name: {vowelCount}")  # show how many vowels are in the first name
    print(f"Consonants in first name: {consonantCount}")  # show how many consonants are in the first name
    print(f"First name (upper): {firstName.upper()}")  # display the first name converted to uppercase
    print(f"First name (lower): {firstName.lower()}")  # display the first name converted to lowercase
    print(f"Last name (reversed): {lastName[::-1]}")  # display the last name reversed for a quick transformation

    print("\nCharacters in first name (for loop):", end=" ")  # header before printing characters with a for-loop
    for ch in firstName:  # iterate characters of first name in order to show each one
        print(ch, end=" ")  # print each character separated by a space on the same line
    print()  # newline to finish the for-loop output

    print("\nCharacters in first name (while loop):", end=" ")  # header before printing characters with a while-loop
    i = 0 
    while i < firstNameLen:  
        print(firstName[i], end=" ")  # print character at current index
        i += 1
    print() 

    if firstNameLen > lastNameLen:  # compare the lengths of the two names to produce a message
        comparison = "First name is longer than last name."  # message when first name is longer
    elif firstNameLen < lastNameLen:  # other comparison branch
        comparison = "Last name is longer than first name."  # message when last name is longer
    else:  # equal length case
        comparison = "First name and last name are equal in length."  # message when lengths match

    print(f"\nComparison result: {comparison}")  # print the comparison result to the user

    generatedPassword = f"{firstName[0]}{lastName[-1]}{firstNameLen + lastNameLen}" if firstName and lastName else ""  # form a simple personal password from initials and combined length
    print(f"\nGenerated password: {generatedPassword}")  # show the generated password

    charList = list(lastName)  # create a mutable list of last name characters for list method examples
    charList.append("*")  # append a marker to the end to demonstrate list append
    charList.insert(0, "@")  # insert a marker at the beginning to demonstrate list insert

    if lastNameLen >= 2:  # attempt to remove the original second character of the last name if it exists
        try:
            charList.remove(lastName[1])  # remove the first occurrence of that second-character value from the list
        except ValueError:
            pass  # if that character isn't present, just ignore the error and continue
    else:  # fallback for very short last names where second character isn't available
        for c in charList:  # scan for the first alphabetic character to remove as a simple fallback
            if c.isalpha():
                charList.remove(c)  # remove the found alphabetic character and stop
                break

    charList.reverse()  # reverse the list in-place to demonstrate list reverse
    print(f"\nList methods example on last name: {charList}")  # display the transformed list as an example


if __name__ == "__main__":
    main()  # execute the interactive main when the script is run directly