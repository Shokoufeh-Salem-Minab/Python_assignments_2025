from library_utils import add_book, search_book, list_books, random_book

def main():
    #List
    books = ["Python 101", "Data Science", "Machine Learning"]
    #Tuple
    book1 = ("Python 101", "John Smith", 2020)
    book2 = ("Data Science", "Alice Brown", 2021)
    book3 = ("Machine Learning", "Bob Wilson", 2019)
    #Dictionary
    library = {
        1: book1,
        2: book2,
        3: book3
    }
    
    while True:
        print("1. Show all books in a library")
        print("2. Add new book")
        print("3. Search book")
        print("4. Random suggest")
        print("5. Exit")
        
        choice = input("\n Choose option 1-5: ")
        
        if choice == "1":
            list_books(library)
            
        elif choice == "2":
            try:
                book_id = int(input("Enter book's id: "))
                title = input("Enter title: ")
                author = input("Enter author: ")
                year = int(input("Enter year: "))
                
                new_book = title, author, year
                add_book(library, book_id, new_book)
                
            except ValueError:
                print("Error! Wrong enter")
                
        elif choice == "3":
            title = input("Enter titile for search: ")
            results = search_book(library, title)
            
            if results:
                print(f"\n Found {len(results)} books:")
                for book_id, book in results:
                    print(f"id: {book_id}, {book[0]} - {book[1]} ({book[2]})")
            else:
                print("Not found!")
                
        elif choice == "4":
            random_book(library)
            
        elif choice == "5":
            print("Byee!")
            break
            
        else:
            print("Wrong enter. Try again")

if __name__ == "__main__":
    main()
