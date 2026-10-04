import random


def add_book(library, book_id, book):
    # first check if the id is already used, because we don't want to overwrite a book
    if book_id in library:
        print("Sorry, ID", book_id, "is already taken!")
    else:
        library[book_id] = book   # add the tuple to the dictionary
        print("Added book:", book[0])


def search_book(library, title):
    # loop through every book in the dictionary
    # I used .lower() so it doesn't matter if you type capital letters or not
    found_books = []
    for book_id in library:
        book = library[book_id]
        if title.lower() in book[0].lower():
            found_books.append(book)   # save the matching book
    return found_books


def list_books(library):
    # if the dictionary is empty there's nothing to print
    if len(library) == 0:
        print("The library is empty.")
        return

    # go through the dictionary and print each book
    for book_id in library:
        book = library[book_id]
        # book[0] is title, book[1] is author, book[2] is year
        print("ID", book_id, "-", book[0], "by", book[1], "(" + str(book[2]) + ")")


def suggest_book(library):
    # random.choice picks a random item, but it doesn't work on a dictionary directly
    # so I turned the keys into a list first
    all_ids = list(library.keys())
    random_id = random.choice(all_ids)
    return library[random_id]