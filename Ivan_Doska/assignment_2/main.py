from library_utils import add_book, search_book, list_books, suggest_random_book
# modules were not redefined 
books = ["Python 101", "Data Science", "Machine Learning"]
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "Bob White", 2022)
genres = {"Programming", "AI", "Math"}
library = { 1: book1, 2: book2 }
add_book(library, 3, book3)
print("Library books:")
list_books(library)
title_to_search = "Python 101"
found = search_book(library, title_to_search)

if found:
    print(f"\nFound book: {found}")
else:
    print("\nBook not found")

suggested = suggest_random_book(library)
print(f"\nSuggested reading: {suggested[0]} by {suggested[1]}")