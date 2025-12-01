type Book = tuple[str, str, int]
type Library = dict[int, Book]


def add_book(library: Library, book_id: int, book: Book) -> bool:
    """
    Adds a book to the library.

    Args:
        library: The library to add the book to.
        book_id: The id of the book to add.
        book: The book to add.

    Returns:
        bool: `True` if the book was added, `False` if the book id is already in the library.
    """
    if book_id in library:
        return False
    library[book_id] = book
    return True


def search_book(library: Library, title: str) -> int | None:
    """
    Searches a book in the library.

    Args:
        library: The library to search in.
        title: The title of the book.

    Returns:
        int | None: book id if found, None otherwise.
    """
    for book_id in library:
        if library[book_id][0] == title:
            return book_id
    return None


def list_books(library: Library):
    """
    Lists all books in the library.

    Args:
        library: The library with books to list.

    Returns:
        None.
    """
    for book_id in library:
        print(f"Book id: {book_id}. Book information: {library[book_id]}")
