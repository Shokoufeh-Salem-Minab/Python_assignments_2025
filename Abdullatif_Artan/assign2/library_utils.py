

def add_book(library, book_id, book):
    
    if book_id in library:
        print("Book ID already exists.")
    else:
        library[book_id] = book
        print("Book added successfully.")


def search_book(library, title):
    
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            print(f"Book found (ID: {book_id}): {book}")
            return
    print("Book not found.")


def list_books(library):
  

    if not library:
        print("Library is empty.")
    else:
        for book_id, book in library.items():
            print(f"ID {book_id}: Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")
