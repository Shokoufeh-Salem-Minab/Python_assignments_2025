

import random
import library_utils



books = ["Python 101", "Data Science", "Machine Learning"]



book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)
book3 = ("Machine Learning", "David Lee", 2022)



genres = {"Programming", "AI", "Math"}



library = {
    1: book1,
    2: book2
}


library_utils.add_book(library, 3, book3)

print("\nAll books in the library:")
library_utils.list_books(library)

print("\nSearching for a book:")
library_utils.search_book(library, "Python 101")


random_book = random.choice(list(library.values()))
print("\nSuggested book for reading:")
print(f"Title: {random_book[0]}, Author: {random_book[1]}, Year: {random_book[2]}")

print("\nAvailable genres in the library:")
print(genres)
