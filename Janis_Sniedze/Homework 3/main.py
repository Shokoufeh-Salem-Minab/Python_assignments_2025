# Jānis Sniedze
# js23127
# Homework 3
# Final edit date: 30/12/2025

from expense import addExpense, summarizeByCategory, latestEntries

def promptAdd():  # prompt the user for a single expense and save it
	print("Add a new expense")  # notify the user this action collects category, amount and description
	category = input("Category: ").strip()  # read category and trim whitespace for cleanliness
	amount = input("Amount: ").strip()  # read amount as text to validate/convert in one place
	description = input("Description: ").strip()  # optional short description of the expense
	try:
		df = addExpense(category, float(amount), description)  # convert amount and persist the new expense
		print("Saved. Current total entries:", len(df))  # show how many rows are stored after adding
	except Exception as e:  # catch broad errors to keep the small CLI resilient
		print("Error saving expense:", e)  # report the error to the user without crashing


def showSummary():  # compute and display aggregated totals per category
	s = summarizeByCategory()  # get aggregated totals sorted by highest expense
	if s.empty:  # when no data has been recorded inform the user
		print("No expenses recorded yet.")
		return
	print("Summary by category:")  # header before printing the DataFrame
	print(s.to_string(index=False))  # print a compact table without the index column


def showLatest():  # show the most recent N expense rows, default 5 when input empty or invalid
	n = input("How many recent entries? (default 5): ")  # ask the user how many entries they want
	try:
		nVal = int(n) if n.strip() else 5  # parse to int, fallback to 5 when empty
	except ValueError:
		nVal = 5  # fallback to 5 for non-integer input
	df = latestEntries(nVal)  # get the most recent rows from storage
	if df.empty:  # when there are no stored expenses inform the user
		print("No expenses recorded yet.")
		return
	print(df.to_string(index=False))  # print the recent entries in a compact table form


def main():  # small command-line UI loop exposing add, summary and latest actions
	menu = {
		"1": ("Add expense", promptAdd),
		"2": ("Show summary by category", showSummary),
		"3": ("Show latest entries", showLatest),
		"q": ("Quit", None),
	}  # mapping of user choices to labels and handler functions
	while True:
		print("\nSimple Expenses Tracker")  # title for the interactive menu loop
		for k, v in menu.items():  # list available actions for the user to pick
			print(f"{k}) {v[0]}")  # show the key and human-friendly label
		choice = input("Choose an option: ").strip().lower()  # read the user's selection
		if choice == "q":  # allow quitting cleanly
			break
		action = menu.get(choice)  # lookup the selected action in the menu
		if action:
			action[1]()  # call the associated handler function
		else:
			print("Invalid choice")  # simple feedback for unknown menu options


if __name__ == "__main__":
	main()  # run when executed directly as a script
