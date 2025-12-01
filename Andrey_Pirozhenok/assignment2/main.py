from library_utils import (
    add_book,
    Book,
    Library,
    list_books,
    pick_random_book,
    search_book,
)


def main() -> None:
    library: Library = {
        1: ("Python 101", "John Smith", 2020),
        2: ("Data Science", "Alice Brown", 2021),
    }

    print("Initial:")
    list_books(library)

    add_book(library, 11, ("DOUG: A DougDoug Story", "Douglas Scott Wreden", 2025))
    print("After adding a new book")
    list_books(library)

    print(f"search_book(<non existing>) = {search_book(library, 'Hehehaha')}")
    print(f"search_book(Python 101) = {search_book(library, 'Python 101')}")

    print("Picking a random book 10 times:")
    for _i in range(10):
        print(pick_random_book(library))


if __name__ == "__main__":
    main()
