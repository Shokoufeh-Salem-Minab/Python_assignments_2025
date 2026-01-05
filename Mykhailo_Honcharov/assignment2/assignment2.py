import library_utils 

def main() -> None:
    library = { 
        1: ("Python 101", "John Smith", 2020), 
        2: ("Data Science", "Alice Brown", 2021) 
        } 
    
    print("Current Library: ")
    library_utils.list_books(library)

    library_utils.add_book(library, 3, ("Hello", "World", 2022))
    
    print("Library with new book: ")
    library_utils.list_books(library)

    print("Search book (Hello): ")
    print(library_utils.search_book(library, "Hello"))

    print("Search book (123) no in the library: ")
    print(library_utils.search_book(library, "123"))

    print("Random 5 books: ")
    for i in range(5):
        print(library_utils.random_book(library))
    

if __name__ == "__main__":
    main()