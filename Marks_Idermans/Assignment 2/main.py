#Marks Idermans
#mi24027

from library_utils import show_all, find_book, add_new, random_pick

#sample book tuples
bk1 = ("1984", "George Orwell", 1949)
bk2 = ("To Kill a Mockingbird", "Harper Lee", 1960)
bk3 = ("The Great Gatsby", "F. Scott Fitzgerald", 1925)

#set of genres
genres = {"Fiction", "Classic", "Literature"}

#dictionary of books
library = {
    10: bk1,
    20: bk2,
    30: bk3
}

attempts = 0
print("\nWelcome to the Library!")

def menu():
    print("1. Show all books")
    print("2. Search for a book")
    print("3. Add a book")
    print("4. Random book pick")
    print("5. Exit")

while True:
    menu()
    pick = input("Choose 1-5: ").strip()

    if pick == "1":
        show_all(library)
        attempts = 0
    elif pick == "2":
        name = input("Title to search: ").strip()
        find_book(library, name)
        attempts = 0
    elif pick == "3":
        try:
            new_id = int(input("New ID: ").strip())
            t = input("Title: ").strip()
            a = input("Author: ").strip()
            y = int(input("Year: ").strip())
            new = (t, a, y)
            add_new(library, new_id, new)
        except ValueError:
            print("Bad input! Try again.")
        attempts = 0
    elif pick == "4":
        random_pick(library)
        attempts = 0
    elif pick == "5":
        print("Goodbye!")
        break
    else:
        print("Not valid. Choose 1-5.")
        attempts += 1
        if attempts >= 5:
            print("Too many errors! Closing program.")
            break
