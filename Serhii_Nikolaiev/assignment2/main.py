import random

from library_utils import add_book, search_book, list_books, Library


def main():
    _books = ["Python 101", "Data Science", "Machine Learning"]
    _genres = {"Programming", "AI", "Math"}

    book1 = ("Python 101", "John Smith", 2020)
    book2 = ("Data Science", "Alice Brown", 2021)
    book3 = ("Machine Learning", "Oliver Theobald", 2017)

    library: Library = {}

    assert add_book(library, 0, book1)
    assert add_book(library, 1, book2)
    assert add_book(library, 2, book3)

    list_books(library)

    random_book_id = random.choice(library)
    print(f"Random book: {random_book_id}")

    book_id = search_book(library, "Python 101")
    if book_id is not None:
        print(f"Book id: {book_id}")
    else:
        print("Book was not found")


if __name__ == '__main__':
    main()
