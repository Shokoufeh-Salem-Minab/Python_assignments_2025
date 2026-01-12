# -*- coding: utf-8 -*-
"""
Library Management Utilities Module
This module provides functions to manage a library system.
"""

def add_book(library, book_id, book):
    """
    Add a new book to the library.
    
    Args:
        library (dict): The library dictionary
        book_id (int): Unique ID for the book
        book (tuple): Book information (title, author, year)
    
    Returns:
        bool: True if book added successfully, False if ID already exists
    """
    if book_id in library:
        print "Error: Book ID {} already exists!".format(book_id)
        return False
    
    library[book_id] = book
    print "Book '{}' added successfully with ID {}".format(book[0], book_id)
    return True


def search_book(library, title):
    """
    Search for a book by title.
    
    Args:
        library (dict): The library dictionary
        title (str): The title to search for
    
    Returns:
        tuple or None: (book_id, book_info) if found, None otherwise
    """
    title_lower = title.lower()
    for book_id, book_info in library.items():
        if book_info[0].lower() == title_lower:
            return (book_id, book_info)
    return None


def list_books(library):
    """
    Print all books in the library.
    
    Args:
        library (dict): The library dictionary
    """
    if not library:
        print "The library is empty."
        return
    
    print "\n" + "=" * 70
    print "{:<5} {:<30} {:<20} {:<10}".format('ID', 'Title', 'Author', 'Year')
    print "=" * 70
    
    for book_id, (title, author, year) in library.items():
        print "{:<5} {:<30} {:<20} {:<10}".format(book_id, title, author, year)
    
    print "=" * 70
    print "Total books: {}\n".format(len(library))


def remove_book(library, book_id):
    """
    Remove a book from the library by ID.
    
    Args:
        library (dict): The library dictionary
        book_id (int): The ID of the book to remove
    
    Returns:
        bool: True if removed, False if not found
    """
    if book_id in library:
        book = library.pop(book_id)
        print "Book '{}' (ID: {}) has been removed.".format(book[0], book_id)
        return True
    else:
        print "Error: Book ID {} not found!".format(book_id)
        return False


def list_genres(genres):
    """
    Display all unique genres in the library.
    
    Args:
        genres (set): Set of unique genres
    """
    print "\nAvailable Genres:"
    print "-" * 30
    for genre in sorted(genres):
        print "  * {}".format(genre)
    print "-" * 30 + "\n"


def add_genre(genres, new_genre):
    """
    Add a new genre to the collection.
    
    Args:
        genres (set): Set of unique genres
        new_genre (str): Genre to add
    """
    if new_genre in genres:
        print "Genre '{}' already exists.".format(new_genre)
    else:
        genres.add(new_genre)
        print "Genre '{}' added successfully.".format(new_genre)
