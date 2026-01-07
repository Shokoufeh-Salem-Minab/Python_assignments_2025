import random

# Function to add a new book to the library
def add_book(library, book_id, book_tuple):
    """
    Add a new book to the library.
    
    Args:
        library (dict): The library dictionary
        book_id (int): Unique book ID
        book_tuple (tuple): Book information as (title, author, year)
    """
    if book_id in library:
        print(f"Book ID {book_id} already exists. Use a different ID.")
        return False
    
    library[book_id] = book_tuple
    print(f"Book '{book_tuple[0]}' added successfully!")
    return True


# Function to search for a book by title
def search_book(library, title):
    """
    Search for a book by title.
    
    Args:
        library (dict): The library dictionary
        title (str): Title of the book to search for
    
    Returns:
        tuple: Book information if found, None otherwise
    """
    for book_id, book_info in library.items():
        if book_info[0].lower() == title.lower():
            return book_id, book_info
    
    return None


# Function to list all books in the library
def list_books(library):
    """
    Print all books in the library.
    
    Args:
        library (dict): The library dictionary
    """
    if not library:
        print("The library is empty!")
        return
    
    print("\n" + "="*60)
    print("LIBRARY CATALOG")
    print("="*60)
    
    for book_id, (title, author, year) in library.items():
        print(f"ID: {book_id}")
        print(f"  Title:  {title}")
        print(f"  Author: {author}")
        print(f"  Year:   {year}")
        print("-"*60)
    
    print()


# Function to suggest a random book
def suggest_random_book(library):
    """
    Suggest a random book from the library.
    
    Args:
        library (dict): The library dictionary
    
    Returns:
        tuple: Random book information (book_id, book_info)
    """
    if not library:
        print("The library is empty! No book to suggest.")
        return None
    
    book_id = random.choice(list(library.keys()))
    book_info = library[book_id]
    
    print(f"\n📚 Random Book Suggestion: '{book_info[0]}' by {book_info[1]} ({book_info[2]})")
    return book_id, book_info


# Function to display book genres
def display_genres(genres):
    """
    Display all genres in the library.
    
    Args:
        genres (set): Set of genres
    """
    print("\nAvailable Genres:")
    for genre in sorted(genres):
        print(f"  • {genre}")
