#Marks Idermans
#mi24027


import random

def add_new(lib, book_id, book):
    #add a book
    if book_id in lib:
        print(f"ID {book_id} already used.")
    else:
        lib[book_id] = book
        print(f"Added '{book[0]}' by {book[1]} ({book[2]}).")

def find_book(lib, title):
    #search by title
    ok = False
    for bid, bk in lib.items():
        if bk[0].lower() == title.lower():
            print(f"Found: ID={bid} '{bk[0]}' by {bk[1]} ({bk[2]})")
            ok = True
    if not ok:
        print(f"Nothing found for '{title}'.")

def show_all(lib):
    #show everything
    if not lib:
        print("Library is empty.")
        return
    print("Books:")
    print("-" * 30)
    for bid, bk in lib.items():
        print(f"ID={bid} '{bk[0]}' by {bk[1]} ({bk[2]})")
    print("-" * 30)

def random_pick(lib):
    #pick one randomly
    if not lib:
        print("Empty library. No suggestion.")
        return
    bk = random.choice(list(lib.values()))
    print(f"Try reading '{bk[0]}' by {bk[1]} ({bk[2]}).")
