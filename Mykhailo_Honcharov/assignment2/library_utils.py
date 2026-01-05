import random

def add_book(library, book_id, book):
    library[book_id] = book;

def search_book(library, title):
    for _, book in library.items():
        if book[0].lower() == title.lower():
            return book
    return None 

def list_books(library):
    for book_id, book in library.items():
        print(f"ID: {book_id}, Title: {book[0]}, Author: {book[1]}, Year: {book[2]}")

def random_book(library):
    return random.choice(list(library.values()))