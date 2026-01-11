# library_utils.py


# FUNCTION: Add a new book

def add_book(library, book_id, book):
    """
    Adds a new book to the library dictionary.
    """
    library[book_id] = book
    print("Book added successfully")


# FUNCTION: Search a book

def search_book(library, title):
    """
    Searches for a book by title.
    """
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            print(f"Book found (ID: {book_id}): {book}")
            return
    print("Book not found.")

# FUNCTION: List all books

def list_books(library):
    """
    Prints all books in the library.
    """
    if not library:
        print("Library is empty.")
        return

    for book_id, book in library.items():
        print(f"ID: {book_id} | Title: {book[0]} | Author: {book[1]} | Year: {book[2]}")

