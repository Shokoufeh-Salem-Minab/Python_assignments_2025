# Dana Oborenko do23008
import random

# A book is represented as a tuple: (title, author, year)
def add_book(library, book_id, book):
    """
    Add a new book to the dictionary.
    library: dict {id: book_tuple}
    book_id: int
    book: (title, author, year)
    """
    if book_id in library:
        raise ValueError(f"Book ID {book_id} already exists")
    library[book_id] = book


def search_book(library, title_query):
    """
    Find books where title will contains the query.
    Returns a list of (id, book) pairs.
    """
    q = title_query.strip().lower()
    results = []
    for bid, (title, author, year) in library.items():
        if q in title.lower():
            results.append((bid, (title, author, year)))
    return results


def list_books(library):
    lines = []
    for bid in sorted(library.keys()):
        title, author, year = library[bid]
        lines.append(f"[{bid}] {title} — {author} ({year})")
    return lines


def suggest_random_book(library):
    """
    Pick a random book using the standard library 'random'.
    """
    if not library:
        return None
    bid = random.choice(list(library.keys()))
    return bid, library[bid]
