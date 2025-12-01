import random

def add_book(library, book_id, book):
   
    if book_id in library:
        print(f"The book with id - {book_id} already exist")
        return False
    else:
        library[book_id] = book
        print(f"The book '{book[0]}' has been added")
        return True

def search_book(library, title):

    search_lower = title.lower()
    results = []
    
    for book_id, book in library.items():
        book_title_lower = book[0].lower()
        if search_lower in book_title_lower:
            results.append((book_id, book))
    
    return results

def list_books(library):
   
    if not library:
        print("Library is empty!")
        return
    
    for book_id, book in library.items():
        print(f"id: {book_id}, Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")

def random_book(library):
   
    if not library:
        print("Library is empty!")
        return None
    
    keys_list = list(library.keys())
    random_index = random.randint(0, len(keys_list) - 1)
    random_id = keys_list[random_index]
    random_book = library[random_id]
    print(f"I think You can read this: '{random_book[0]}' from {random_book[1]} ({random_book[2]})")
    return random_book
