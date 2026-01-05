import string
import secrets
from pathlib import Path

# password generator from name and phone


def generatePasswordFromInfo(firstName: str, lastName: str, phone: str,
 	extraDigits: int = 1, extraSymbols: int = 1) -> str:  # generate a password using name parts and secure randomness
	firstClean = ''.join(firstName.split())  # remove spaces so name parts are deterministic and compact
	lastClean = ''.join(lastName.split())  # remove spaces from last name for consistent suffix extraction
	digitsOnlyPhone = ''.join(ch for ch in phone if ch.isdigit())  # keep only digits from phone input to avoid punctuation

	firstPart = firstClean[:2].upper() if firstClean else ''  # use up to two uppercase letters from start of first name
	lastPart = lastClean[-2:].lower() if lastClean else ''  # use up to two lowercase letters from end of last name

	if len(digitsOnlyPhone) >= 4:
		lastFourReversed = digitsOnlyPhone[-4:][::-1]  # take last four digits and reverse them to make pattern less obvious
	else:
		lastFourReversed = digitsOnlyPhone[::-1]  # reverse whatever digits are available when fewer than four

	randomDigits = ''.join(secrets.choice(string.digits) for _ in range(max(0, extraDigits)))  # securely chosen digits to increase entropy
	randomSymbols = ''.join(secrets.choice(string.punctuation) for _ in range(max(0, extraSymbols)))  # securely chosen symbols to increase entropy

	password = f"{firstPart}{lastPart}{lastFourReversed}{randomDigits}{randomSymbols}"  # deterministic prefix then extras

	while len(password) < 8:
		password += secrets.choice(string.digits)  # pad with secure digits until minimum length is satisfied

	return password


def savePassword(password: str, firstName: str, lastName: str, phone: str, filePath: str = None) -> None:  # append generated entry to a log file
	if filePath:
		outPath = Path(filePath)  # respect explicit path when provided
	else:
		outPath = Path(__file__).parent / 'passwords.txt'  # default log file next to script for easy access

	outPath.parent.mkdir(parents=True, exist_ok=True)  # ensure containing directory exists to avoid write errors
	with outPath.open('a', encoding='utf-8') as fh:
		fh.write(f"{firstName} {lastName} {phone} -> {password}\n")  # write one record per line for traceability


def askInt(prompt: str, default: int) -> int:  # prompt the user for a non-negative integer, on error return default
	raw = input(f"{prompt} [{default}]: ").strip()
	if not raw:
		return default  # empty input means accept the default
	try:
		val = int(raw)
		return max(0, val)  # enforce non-negative
	except ValueError:
		print("Invalid number, using default.")  # inform about fallback
		return default


def main():
	print("Password generator from name and phone")  # friendly header for interactive use

	firstName = input("First name: ").strip()
	lastName = input("Last name: ").strip()
	phone = input("Phone: ").strip()

	extraDigits = askInt("How many extra random digits to add", 1)
	extraSymbols = askInt("How many extra random symbols to add", 1)

	pwd = generatePasswordFromInfo(firstName, lastName, phone, extraDigits, extraSymbols)
	print(f"Generated password: {pwd}")  # show result so user can copy it
	savePassword(pwd, firstName, lastName, phone)  # save generated password for records


if __name__ == '__main__':
	main()

