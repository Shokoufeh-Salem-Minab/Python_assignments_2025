import random

def add_book(library: dict, book_id: int, book: tuple) -> None:
    library[book_id] = book


def search_book(library: dict, title: str) -> tuple | None:
    for book in library.values():
        if book[0].lower() == title.lower():
            return book
    return None


def list_books(library: dict) -> None:
    for book_id, (title, author, year) in library.items():
        print(f"{book_id}: {title} by {author} ({year})")


def suggest_random_book(library: dict) -> tuple:
    return random.choice(list(library.values()))
