# add a new book to the library
def add_book(library, book_id, book_tuple):
    if book_id in library:
        print(f"book id {book_id} already exists")
        return False
    library[book_id] = book_tuple
    print(f"added: {book_tuple[0]}")
    return True

# search for a book by its title
def search_book(library, title):
    for book_id, book_info in library.items():
        if title.lower() in book_info[0].lower():
            print(f"found: {book_info[0]} by {book_info[1]} ({book_info[2]})")
            return book_info
    print(f"no book found with '{title}'")
    return None

# display all books in the library
def list_books(library):
    print("\nlibrary books:")
    for book_id, book_info in library.items():
        print(f"{book_id}: {book_info[0]} - {book_info[1]} ({book_info[2]})")