
# this is a library used later in main.py, providing functions to manage a book collection

import random

def add_book(library, book_id, book):
    if book_id in library:
        print(f"Book ID {book_id} already exists. Try a different ID.")
    else:
        library[book_id] = book
        print(f"Book '{book[0]}' by {book[1]} ({book[2]}) added successfully!")

def search_book(library, title):
    found = False
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            print(f"Found ID={book_id} | '{book[0]}' by {book[1]} ({book[2]})")
            found = True
    if not found:
        print(f"No book found with the title '{title}'.")

def list_books(library):
    if not library:
        print("The library is currently empty.")
        return
    print("Books in the library:")
    print("=" * 40)
    for book_id, book in library.items():
        print(f"ID={book_id} | '{book[0]}' by {book[1]} ({book[2]})")
    print("=" * 40)

def suggest_random_book(library):
    if not library:
        print("The library is empty. Cannot suggest anything.")
        return
    book = random.choice(list(library.values()))
    print(f"How do you feel about '{book[0]}' by {book[1]} ({book[2]})?")
