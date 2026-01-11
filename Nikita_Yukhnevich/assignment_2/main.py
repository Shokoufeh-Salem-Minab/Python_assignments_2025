import random
import library_utils as lib

# list of book titles
books = ["Intro to Python", "Understanding Data", "ML Fundamentals"]

# tuple examples
book1 = ("Intro to Python", "Marcus Rivera", 2020)
book2 = ("Understanding Data", "Priya Desai", 2021)

# set of unique genres
genres = {"Programming", "Data Analysis", "Math"}

# dictionary with book id as key and tuple as value
library = {
    1: ("Intro to Python", "Marcus Rivera", 2020),
    2: ("Understanding Data", "Froak Linja", 2021),
    3: ("ML Fundamentals", "Jamal Waylay", 2019)
}

print("=== library system ===")

# show all books
lib.list_books(library)

# add a new book
new_book = ("Web Design Basics", "Elena Kowalski", 2022)
lib.add_book(library, 4, new_book)

# search for a book
print("\nsearching for books:")
lib.search_book(library, "python")

# show updated library
lib.list_books(library)

# random book suggestion using standard library
random_id = random.choice(list(library.keys()))
random_book = library[random_id]
print(f"\nrandom suggestion: {random_book[0]} by {random_book[1]}")

print(f"\ntotal books: {len(library)}")
print(f"genres available: {genres}")