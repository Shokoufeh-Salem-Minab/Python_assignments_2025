# Import the library_utils module
import library_utils
# Import random from standard library
import random

# List of book titles
books = ["No Country for Old Men", "The Great Gatsby", "To Kill a Mockingbird"]

# Tuple examples - each book is (title, author, year)
book1 = ("No Country for Old Men", "Cormac McCarthy", 2005)
book2 = ("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book3 = ("To Kill a Mockingbird", "Harper Lee", 1960)

# Set of unique genres
genres = {"Fiction", "Mystery", "Drama"}

# Dictionary - library with book_id as key and book tuple as value
library = {
    1: ("No Country for Old Men", "Cormac McCarthy", 2005),
    2: ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    3: ("To Kill a Mockingbird", "Harper Lee", 1960)
}

# Display initial library
print("=== LIBRARY MANAGEMENT SYSTEM ===\n")
library_utils.list_books(library)

# Display genres
library_utils.list_genres(genres)

# Add a new book
print("\n--- Adding New Book ---")
new_book = ("1984", "George Orwell", 1949)
library_utils.add_book(library, 4, new_book)

# List all books after adding
library_utils.list_books(library)

# Search for a book
print("\n--- Searching for a Book ---")
library_utils.search_book(library, "The Great Gatsby")

# Search for a book that doesn't exist
print("\n--- Searching for Non-existent Book ---")
library_utils.search_book(library, "The Hobbit")

# Random book suggestion using standard library
print("\n--- Random Book Suggestion ---")
if len(library) > 0:
    random_id = random.choice(list(library.keys()))
    random_book = library[random_id]
    print(f"We suggest you read: '{random_book[0]}' by {random_book[1]} ({random_book[2]})")

# Remove a book
print("\n--- Removing a Book ---")
library_utils.remove_book(library, 2)

# List books after removal
library_utils.list_books(library)

# Add a new genre to the set
print("\n--- Adding New Genre ---")
genres.add("Thriller")
print("Added 'Thriller' to genres")
library_utils.list_genres(genres)

print("\n=== END OF PROGRAM ===")