def add_book(library, book_id, book):
    """Add a new book to the library"""
    if book_id in library:
        print("Book ID already exists!")
    else:
        library[book_id] = book
        print(f"Book '{book[0]}' added successfully!")

def search_book(library, title):
    """Search for a book by title"""
    found = False
    for book_id, book in library.items():
        if book[0].lower() == title.lower():
            print(f"\nBook Found!")
            print(f"ID: {book_id}")
            print(f"Title: {book[0]}")
            print(f"Author: {book[1]}")
            print(f"Year: {book[2]}")
            found = True
            break
    
    if not found:
        print(f"Book '{title}' not found in library.")

def list_books(library):
    """Print all books in the library"""
    if len(library) == 0:
        print("Library is empty!")
    else:
        print("\n--- Library Books ---")
        for book_id, book in library.items():
            print(f"ID: {book_id} | Title: {book[0]} | Author: {book[1]} | Year: {book[2]}")

def remove_book(library, book_id):
    """Remove a book from the library"""
    if book_id in library:
        removed_book = library.pop(book_id)
        print(f"Book '{removed_book[0]}' removed successfully!")
    else:
        print("Book ID not found!")

def list_genres(genres):
    """Print all genres"""
    print("\n--- Available Genres ---")
    for genre in genres:
        print(f"- {genre}")