# ~~~~~~~~ACTIVITY 2 PYTHON - Library Management~~~~~~~~
# By Julia Rosa Martinez Redondo jm25057

import random
import library_utils          # my module in other py

# ~~~~~~~~LIST~~~~~~~~
books = ["Minecraft", "English British Burgos Accent", "Radon Influence"]

# ~~~~~~~~TUPLES~~~~~~~~
book1 = ("Minecraft", "Peter Martinez", 2020)
book2 = ("English British Burgos Accent", "Maria Sanchez", 2021)
book3 = ("Radon Influence", "Rosa Jimenez", 2019)

# ~~~~~~~~SET~~~~~~~~
genres = {"Gaming", "Languages", "Science"}

# ~~~~~~~~DICTIONARY~~~~~~~~
library = {
    1: book1,
    2: book2
}

# ~~~~~~~~USING FUNCTIONS~~~~~~~~
library_utils.add_book(library, 3, book3)
library_utils.list_books(library)
library_utils.search_book(library, "Minecraft")

# ~~~~~~~~RANDOM BOOK~~~~~~~~
random_book = random.choice(list(library.values()))
print("random book suggestion:", random_book)
