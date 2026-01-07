from library_utils import add_book, search_book, list_books, suggest_random_book, display_genres


# List of book titles
books = ["Programmēšanas Pamati", "Mākslīgais Intelekts", "Datu Analīze", "Tīmekļa Izstrāde", "Mākonis Datorika"]

# Tuple: Each book stored as (title, author, year)
book1 = ("Programmēšanas Pamati", "Jānis Bērziņš", 2020)
book2 = ("Mākslīgais Intelekts", "Ilze Gaļitskaja", 2021)
book3 = ("Datu Analīze", "Andris Kalniņš", 2019)
book4 = ("Tīmekļa Izstrāde", "Dace Celmiņa", 2022)
book5 = ("Mākonis Datorika", "Raimonds Vaidere", 2023)

# Set: Unique genres in the library
genres = {"Programming", "Data Science", "AI", "Web", "Cloud"}

# Dictionary: Library with book ID as key and book tuple as value
library = {
    1: book1,
    2: book2,
    3: book3,
    4: book4,
    5: book5
}

# ===== MAIN PROGRAM =====
print("="*60)
print("WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
print("="*60)

# Display initial information
print("\nBook Titles in List:")
for i, title in enumerate(books, 1):
    print(f"  {i}. {title}")

display_genres(genres)

# Show initial library
print("\nInitial Library:")
list_books(library)

# ===== TESTING FUNCTIONS =====

# Add a new book
print("\n--- Adding new books ---")
add_book(library, 6, ("Python Advancēts", "Ieva Ošeniece", 2024))
add_book(library, 7, ("Mašīnmācīšanās Padziļināti", "Kristofers Sīmans", 2023))

# Display updated library
print("\nLibrary after adding new books:")
list_books(library)

# Search for a book
print("\n--- Searching for books ---")
search_result = search_book(library, "Datu Analīze")
if search_result:
    book_id, book_info = search_result
    print(f"[OK] Found: Book ID {book_id} - '{book_info[0]}' by {book_info[1]} ({book_info[2]})")
else:
    print("[NOT FOUND] Book not found!")

search_result = search_book(library, "Programmēšanas Pamati")
if search_result:
    book_id, book_info = search_result
    print(f"[OK] Found: Book ID {book_id} - '{book_info[0]}' by {book_info[1]} ({book_info[2]})")
else:
    print("[NOT FOUND] Book not found!")

# Suggest a random book (using random library)
print("\n--- Random Book Suggestion ---")
suggest_random_book(library)
suggest_random_book(library)

# Display final library statistics
print("\n" + "="*60)
print("LIBRARY STATISTICS")
print("="*60)
print(f"Total Books: {len(library)}")
print(f"Total Genres: {len(genres)}")
print(f"Books tracked in list: {len(books)}")

print("\n" + "="*60)
print("END OF PROGRAM")
print("="*60)
