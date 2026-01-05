# here i will create a functions for a simple library management system.

#---------------------------------------------------------------------------------------------------------------------------------------------
# Add a new book to the library dictionary.
# library: dict where key = book_id, 
# value = (title, author, year)
# book: tuple (title, author, year)

# this function is made to add a new book into dictionary.
# if ID is taken, returns false
# if not -> adds a book into library by
    # library[book_id] = book
# adds a "book" for the "book_id" key
# returns true
def add_book(library, book_id, book):

    if book_id in library:
        print("This ID already exists. Choose another ID.")
        return False

    library[book_id] = book
    print("Book added.")
    return True

#---------------------------------------------------------------------------------------------------------------------------------------------
# Search a book by title (case-insensitive).
# Returns a list of matches: [(id, book_tuple), ...]

# creates an empty list results. we will return them us the result of the function work.
# using for loop we're sorting through dictionary. looking for each key and each value. (.items() is used for it)
# then we take the first [0] thing from the tuple (the name of the book) and store it in book_title
# then, by lowercasing the book_title and checking if it == lowercased title,
# we add this book into results list and retirn it.
def search_book(library, title):

    results = []
    for book_id, book in library.items():
        book_title = book[0]
        if book_title.lower() == title.lower():
            results.append((book_id, book))
    return results

#---------------------------------------------------------------------------------------------------------------------------------------------
# Print all books from the library.
# if the library is empty - prints that it is empty
# the function sorting through dictionary
# assigns the variables to the current tuple
# prints it while there is something left in the dictionary.
def list_books(library):

    if len(library) == 0:
        print("Library is empty.")
        return

    for book_id, book in library.items():
        title, author, year = book
        print(f"ID: {book_id} | Title: {title} | Author: {author} | Year: {year}")
