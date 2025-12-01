"""
Library Management System

This program allows users to manage a small library interactively.
You can list all books, search for a specific book, add new books, 
and get a random book suggestion. 

The program demonstrates the use of:
* Lists, Tuples, Sets, Dictionaries
* Functions and Modules
* Python's standard library (random)
* Simple user interaction with input() and print()

Enter options to navigate the menu. Invalid choices are counted,
and after several incorrect attempts, the session will terminate.
"""

from library_utils import list_books, search_book, add_book, suggest_random_book

# Pre-defined books (by Homework requirement)
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "Bob Green", 2022)

# Set of genres
genres = {"Programming", "AI", "Math"}

# Library dictionary
library = {
    1: book1,
    2: book2,
    3: book3
}

count = 0
print("\nWelcome to the Library!")

def show_menu():
    print("1. List all books")
    print("2. Search for a book")
    print("3. Add a new book")
    print("4. Suggest a random book")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Please, choose an option (1-5): ").strip()
    
    if choice == "1":
        list_books(library)
        count = 0
    elif choice == "2":
        title = input("Enter the book title to search: ").strip()
        search_book(library, title)
        count = 0
    elif choice == "3":
        try:
            book_id = int(input("Enter a new book ID: ").strip())
            title = input("Enter book title: ").strip()
            author = input("Enter author name: ").strip()
            year = int(input("Enter publication year: ").strip())
            new_book = (title, author, year)
            add_book(library, book_id, new_book)
        except ValueError:
            print("Invalid input! Please enter correct details.")
        count = 0
    elif choice == "4":
        suggest_random_book(library)
        count = 0
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number between 1 and 5.")
        count += 1
        if count >= 5:
            print("ENOUGH!!! I'm terminating session!")
            break
