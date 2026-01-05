# Dana Oborenko do23008

from library_utils import add_book, search_book, list_books, suggest_random_book

# List: titles of books 
book_titles = ["Python 101", "Data Science", "Machine Learning", "Clean Code"]

# Tuples: each book as (title, author, year)
book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "Bob Lee", 2019)
book4 = ("Clean Code", "Robert C. Martin", 2008)

#Set: unique genres 
genres = {"Programming", "AI", "Math"}
genres.add("Software Engineering") 

# Dictionary: the library 
library = {
    1: book1,
    2: book2,
    3: book3,
}

# Use function from module to add a new book
add_book(library, 4, book4)

# Print all books
print("ALL BOOKS:")
for line in list_books(library):
    print(" ", line)

# Search by title (case-insensitive, substring)
query = "python"
print(f"\nSEARCH by title: '{query}'")
results = search_book(library, query)
if results:
    for bid, (title, author, year) in results:
        print(f"  Found [{bid}] {title} — {author} ({year})")
else:
    print("  No results.")

# Show list example (list of titles)
print("\nBOOK TITLES (list example):")
print(" ", book_titles)

# Show set example (genres)
print("\nGENRES (set example):")
print(" ", genres)

# Suggest a random book using the standard library 'random'
print("\nRANDOM SUGGESTION:")
suggestion = suggest_random_book(library)
if suggestion is None:
    print("  Library is empty.")
else:
    bid, (title, author, year) = suggestion
    print(f"  Read next → [{bid}] {title} — {author} ({year})")
