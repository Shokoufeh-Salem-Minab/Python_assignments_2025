# ~~~~~~~~LIBRARY UTILS~~~~~~~~
# functions --> LIBRARY SYSTEM
def add_book(library, id, book):
    # add new book to dictionary
    library[id] = book

def search_book(library, title):
    # search book x title
    for key in library:
        if library[key][0] == title:
            print("book found:", library[key])
            return
    print("book not found")

def list_books(library):
    # printing ALL books library
    for key in library:
        print("id:", key, "book:", library[key])
