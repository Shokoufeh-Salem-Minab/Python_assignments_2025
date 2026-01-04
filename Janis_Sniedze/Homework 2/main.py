# Jānis Sniedze
# js23127
# Homework 8
# Final edit date: 30/12/2025


import library_utils as lib  # import helper module containing library data and functions


def printBooks(libDict):  # format and print each stored book in a readable single-line form
	print("Library contents:")  # header shown before listing entries
	for bid, (title, author, year) in libDict.items():  # iterate over id and the book tuple
		print(f"{bid}: {title} — {author} ({year})")  # print id followed by title, author and year
	print()  # blank line for visual separation after the list


def main():  # small demo that exercises the library utilities
	myLib = lib.libraryData.copy()  # copy module data so the demo does not mutate the original

	printBooks(myLib)  # print the starting state of the library

	newBook = ("Machine Learning", "Bob Lee", 2019)  # create a new book tuple to add
	added = lib.addBook(myLib, 3, newBook)  # attempt to add at id 3 and capture success flag
	print(f"Added book id 3: {added}")  # print whether the insertion succeeded
	printBooks(myLib)  # print library after the attempted insertion to show the change

	results = lib.searchBook(myLib, "Python 101")  # perform a case-insensitive title search
	print("Search results for 'Python 101':")  # header for search output
	for bid, book in results:  # iterate matches and display them
		print(f"- {bid}: {book[0]} by {book[1]} ({book[2]})")  # show id, title, author, year for each match
	print()  # spacing after search results

	suggestion = lib.suggestRandomBook(myLib)  # get a random suggestion from the library
	if suggestion:  # when a suggestion exists unpack and display it
		bid, book = suggestion  # unpack the returned (id, book) pair
		print("Suggested book to read:", f"{book[0]} by {book[1]} ({book[2]}) [id {bid}]")  # show the suggestion nicely
	else:  # no suggestion means the library was empty
		print("No books available to suggest.")  # inform the user when nothing can be suggested


if __name__ == "__main__":
	main()  # run the demo when executed as a script

