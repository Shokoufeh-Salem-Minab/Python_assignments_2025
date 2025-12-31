import random
from library_utils import addBook, searchBook, listBooks

books = ["Python 101", "Data Science", "Machine Learning"]

book1 = ("Python 101", "John Smith", 2020)
book2 = ("Data Science", "Alice Brown", 2021)

genres = {"Programming", "AI", "Math"}

library = {
    1: book1,
    2: book2
}

addBook(library, 3, ("Machine Learning", "Bob Lee", 2022))
listBooks(library)

print(searchBook(library, "Python 101"))

print("Suggested book:", random.choice(list(library.values())))
