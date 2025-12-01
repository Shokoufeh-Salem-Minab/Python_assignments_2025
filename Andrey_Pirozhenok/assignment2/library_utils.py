import random
from typing import Tuple

Book = Tuple[str, str, int]
Library = dict[int, Book]


def add_book(library: Library, book_id: int, book: Book) -> None:
    library[book_id] = book


def search_book(library: Library, title: str) -> Book | None:
    for book in library.values():
        if book[0] == title:
            return book
    return None


def list_books(library: Library) -> None:
    if len(library) == 0:
        print("Library: <empty>")
        return

    keys = list(library.keys())
    keys.sort()
    print("Library:")
    for key in keys:
        book = library[key]
        print(f'\t#{key:02}: "{book[0]}" by {book[1]} ({book[2]})')


def pick_random_book(library: Library) -> Book:
    assert len(library) > 0
    return random.choice(list(library.values()))
