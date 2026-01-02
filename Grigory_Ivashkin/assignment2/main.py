# here we import the random library
# also we import the functions that we made in library_utils
import random
from library_utils import add_book, search_book, list_books


#---------------------------------------------------------------------------------------------------------------------------------------------
# List of book titles (simple list)
# here we create a list books and store ("Python 101", "Data Science", "Machine Learning") in it
books = ["Python 101", "Data Science", "Machine Learning"]


#---------------------------------------------------------------------------------------------------------------------------------------------
# Set of unique genres
# here we create a set of genres and store {"Programming", "AI", "Math"} in it.
# we use set, because it will automaticaly delete the copies. ( there can't be copies for genres)
# sets dont have order like list have, but we dont need it. we just need an "array" of genres.
genres = {"Programming", "AI", "Math"}


#---------------------------------------------------------------------------------------------------------------------------------------------
# Dictionary: 
# key = book ID, 
# value = book tuple (title, author, year)

# here we create a dictionary for libraries. we need it, so, we will have an unique ID for every book tuple.
#

library = {
    1: ("Python 101", "John Smith", 2020),
    2: ("Data Science", "Alice Brown", 2021),
    3: ("Machine Learning", "Bob White", 2019),
}


#---------------------------------------------------------------------------------------------------------------------------------------------
# this function is made here, not in library_utils.py because we need random library to make it work. We could move this function there, but, 
# I guess it will make program work slower 

# 1. we create a function suggest_random_book and set it to work with our library dictionary.
# 2. if the dictionary is empty, we print that we have nothing to suggest.
# 3. .keys() is used so we will get only the keys from our dictionary (1, 2, 3). it is made, so random library functions could be used.
# 4. after we received the keys, we turn them into list using list(), so random function could work with it. this function won't work with the dictionary.
# 5. after we turned content into a list, we user random.choice() to chose a random key. 
# so, random_id is an ID (key from the library dictionary) of the tuple, chosed by random library function.
# 6. then we create 3 variables (title, author, year) and ""unpack" in them content from the tuple of the ID from the library dictionary chosed by random.
# 7. we print the suggestion result. f is used so, we could use our contetn inside {} even inside the "".
def suggest_random_book(library_dict):
    if len(library_dict) == 0:
        print("No books to suggest. Library is empty.")
        return
    random_id = random.choice(list(library_dict.keys()))
    title, author, year = library_dict[random_id]
    print(f"Random suggestion -> ID: {random_id} | {title} by {author} ({year})")


print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


#---------------------------------------------------------------------------------------------------------------------------------------------
# here we print our books list, our genres set and our library dictionary.
print("Book titles list:", books)
print("Genres set:", genres)
# here we call for the list_books functions to make it work with our dictionary. ( it prints the tuples).
print("\nAll books in library:")
list_books(library)


#---------------------------------------------------------------------------------------------------------------------------------------------
# here we call for add_book function from library_utils.py to make it work
# with our dictionary (library), with our new variables new_id and new_book.
print("\n\nAdd a new book")
new_id = 4
new_book = ("Deep Learning", "Ian Goodfellow", 2016)
add_book(library, new_id, new_book)


#---------------------------------------------------------------------------------------------------------------------------------------------
# here we search a book by title.
# we create 2 variables. search_title stores the search request.
# found stores the result of the search_book function result.
# if we didn't find anything. the function will return nothing and we print that we didn't find anything.
# If we did, we print the search result.
print("\n\nSearch a book by title")
search_title = "Python 101"
found = search_book(library, search_title)
if len(found) == 0:
    print("No book found with that title.")
else:
    for book_id, book in found: # we receive a tuple from the function (e.g. (1: ("Python 101", "John Smith", 2020)) )
        title, author, year = book # we create new variables and set them to the values of the tuple we get
        print(f"Found -> ID: {book_id} | {title} by {author} ({year})") # and we print them. f, is used, so i dont spend time on commas and quotation marks


#---------------------------------------------------------------------------------------------------------------------------------------------
# we print our new dictionary after we added new book.
print("\n\n Updated library")
list_books(library)


#---------------------------------------------------------------------------------------------------------------------------------------------
# using function that chosing random book to suggest, we print the suggestion
print("\n\n Random book suggestion")
suggest_random_book(library)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
