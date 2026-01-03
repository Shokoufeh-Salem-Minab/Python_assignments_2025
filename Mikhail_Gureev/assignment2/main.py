# main.py

# Import standard library
import random

# Import our custom module
import library_utils


# LIST: Book titles

books = ["history", "harry potter", "john wick"]


# SET: Unique genres
genres = {"cheese", "potato", "Math"}


# DICTIONARY: Library

library = {
    1: ("history", "John Smith", 2020),
    2: ("harry potter", "Alice Brown", 2021)
}


# DISPLAY GENRES

print("Library Genres:", genres)


# LIST ALL BOOKS

print("\nAll Books:")
library_utils.list_books(library)


# ADD A NEW BOOK

new_book = ("Machine Learning", "Tom White", 2022)
library_utils.add_book(library, 3, new_book)


# SEARCH FOR A BOOK

library_utils.search_book(library, "Python 101")


# RANDOM BOOK SUGGESTION

random_book = random.choice(list(library.values()))
print("Random Book Suggestion:")
print(f"Title: {random_book[0]}, Author: {random_book[1]}, Year: {random_book[2]}")

