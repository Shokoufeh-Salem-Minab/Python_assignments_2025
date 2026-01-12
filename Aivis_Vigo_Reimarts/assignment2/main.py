# -*- coding: utf-8 -*-
"""
Library Management System - Main Program
Demonstrates: list, tuple, set, dictionary, functions, modules, and standard library
"""

import library_utils
import random


def suggest_random_book(library):
    """
    Suggest a random book from the library using the random module.
    
    Args:
        library (dict): The library dictionary
    """
    if not library:
        print "No books available to suggest."
        return
    
    book_id = random.choice(list(library.keys()))
    book = library[book_id]
    print "\n** Random Book Suggestion:"
    print "   '{}' by {} ({})".format(book[0], book[1], book[2])
    print "   Book ID: {}\n".format(book_id)


def main():
    """Main function to demonstrate the library management system."""
    
    print "=" * 70
    print " LIBRARY MANAGEMENT SYSTEM ".center(70)
    print "=" * 70
    
    book_titles = ["Python 101", "Data Science", "Machine Learning"]
    print "\n[*] Initial Book Titles (List):"
    print "   {}".format(book_titles)
    
    book1 = ("Python 101", "John Smith", 2020)
    book2 = ("Data Science", "Alice Brown", 2021)
    book3 = ("Machine Learning", "Bob Johnson", 2022)
    
    genres = {"Programming", "AI", "Math"}
    library_utils.list_genres(genres)
    
    library = {
        1: book1,
        2: book2,
        3: book3
    }
    
    print "\nInitial Library:"
    library_utils.list_books(library)
    
    print "\n--- Adding a new book ---"
    new_book = ("Deep Learning", "Carol White", 2023)
    library_utils.add_book(library, 4, new_book)
    
    library_utils.add_book(library, 4, ("Another Book", "Someone", 2024))
    
    library_utils.list_books(library)
    
    print "--- Searching for a book ---"
    search_title = "Data Science"
    result = library_utils.search_book(library, search_title)
    if result:
        book_id, book_info = result
        print "Found: '{}' by {} ({}) - ID: {}".format(book_info[0], book_info[1], book_info[2], book_id)
    else:
        print "Book '{}' not found.".format(search_title)
    
    print
    search_title = "JavaScript 101"
    result = library_utils.search_book(library, search_title)
    if result:
        book_id, book_info = result
        print "Found: '{}' by {} ({}) - ID: {}".format(book_info[0], book_info[1], book_info[2], book_id)
    else:
        print "Book '{}' not found.".format(search_title)
    
    print "\n--- Adding a new genre ---"
    library_utils.add_genre(genres, "Data Science")
    library_utils.list_genres(genres)
    
    print "--- Random Book Suggestions ---"
    for i in range(3):
        suggest_random_book(library)
    
    print "--- Removing a book ---"
    library_utils.remove_book(library, 2)
    library_utils.list_books(library)
    
    print "\n" + "=" * 70
    print " DEMO COMPLETE ".center(70)
    print "=" * 70


if __name__ == "__main__":
    main()
