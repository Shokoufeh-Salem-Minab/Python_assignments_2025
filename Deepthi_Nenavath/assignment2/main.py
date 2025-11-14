#Main library management program

from library_utils import *
import random

def initialize_library():
    # List of book titles
    book_titles = ["Python 101", "Data Science", "Machine Learning", "Deep Learning", "Statistics Basics"]
    
    # Tuples for each book (title, author, year)
    books_data = [
        ("Python 101", "John Smith", 2020),
        ("Data Science", "Alice Brown", 2021),
        ("Machine Learning", "Bob Wilson", 2019),
        ("Deep Learning", "Carol Davis", 2022),
        ("Statistics Basics", "David Miller", 2018)
    ]
    
    # Set of unique genres
    genres = {"Programming", "Data Science", "AI", "Mathematics", "Computer Science"}
    
    # Dictionary to store books
    library = {}
    
    # Add books to library dictionary
    for i, book in enumerate(books_data, 1):
        library[i] = book
    
    return library, book_titles, genres

def display_menu():
    print("\n" + "="*50)
    print("LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. List all books")
    print("2. Search for a book")
    print("3. Add a new book")
    print("4. Get book suggestion")
    print("5. Show library statistics")
    print("6. Exit")
    print("="*50)

def main():
    # Initialize library data
    library, book_titles, genres = initialize_library()
    
    print("Welcome to the Library Management System!")
    print(f"Initialized with {len(library)} books and {len(genres)} genres.")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            # List all books
            list_books(library)
            
        elif choice == '2':
            # Search for a book
            title = input("Enter book title to search: ").strip()
            if title:
                results = search_book(library, title)
                if results:
                    print(f"\nFound {len(results)} matching book(s):")
                    for book_id, book in results:
                        print(f"ID: {book_id} | {book[0]} by {book[1]} ({book[2]})")
                else:
                    print("No books found with that title.")
                    
        elif choice == '3':
            # Add a new book
            try:
                book_id = int(input("Enter book ID: "))
                title = input("Enter book title: ").strip()
                author = input("Enter author: ").strip()
                year = int(input("Enter publication year: "))
                
                if title and author:
                    new_book = (title, author, year)
                    add_book(library, book_id, new_book)
                else:
                    print("Title and author cannot be empty!")
            except ValueError:
                print("Please enter valid numbers for ID and year!")
                
        elif choice == '4':
            # Get random book suggestion
            suggestion = suggest_random_book(library)
            if suggestion:
                book_id, book = suggestion
                print(f"\n🌟 READING SUGGESTION 🌟")
                print(f"We suggest: '{book[0]}' by {book[1]}")
                print(f"Published in {book[2]} | Book ID: {book_id}")
                
        elif choice == '5':
            # Show statistics
            get_book_statistics(library, genres)
            
        elif choice == '6':
            print("Thank you for using the Library Management System!")
            break
            
        else:
            print("Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()