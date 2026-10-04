import library_utils   # my own module with the functions

# LIST - just the titles of the books
books = ["Python 101", "Data Science", "Machine Learning"]

# TUPLES - each book is (title, author, year)
# tuples can't be changed after creating them
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "David Lee", 2022)

# SET - unique genres (no duplicates allowed)
genres = {"Programming", "AI", "Math"}
genres.add("AI")   # testing this one, AI is already there so nothing changes
genres.add("Statistics")   # this one is new so it gets added

# DICTIONARY - key is the book ID, value is the book tuple
library = {
    1: book1,
    2: book2
}

print("=== Welcome to the Library ===")
print()

print("Book titles:", books)
print("Genres:", genres)
print()

# adding a new book using my function
library_utils.add_book(library, 3, book3)

# trying to add with the same id again, this should give an error message
library_utils.add_book(library, 3, book3)
print()

# print all the books
print("All books in the library:")
library_utils.list_books(library)
print()

# search for a book
search_word = "python"
print("Searching for:", search_word)
results = library_utils.search_book(library, search_word)

if len(results) > 0:
    for book in results:
        print("Found:", book)
else:
    print("No book found.")
print()

# random book suggestion (uses the random library)
suggestion = library_utils.suggest_book(library)
print("You should read:", suggestion[0], "by", suggestion[1])

