def addBook(library, id, book):
    library[id] = book

def searchBook(library, title):
    for book in library.values():
        if book[0].lower() == title.lower():
            return book
    return None

def listBooks(library):
    for id, book in library.items():
        print(id, book)
