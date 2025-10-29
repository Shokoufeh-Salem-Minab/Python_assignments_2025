#Library management utility functions
def add_book(library, book_id, book_tuple):
    if book_id in library:
        print(f"Book ID {book_id} already exists!")
        return False
    library[book_id] = book_tuple
    print(f"Book '{book_tuple[0]}' added successfully!")
    return True

def search_book(library, title):
    results = []
    for book_id, book in library.items():
        if title.lower() in book[0].lower():
            results.append((book_id, book))
    return results

def list_books(library):
    if not library:
        print("The library is empty!")
        return
    
    print("\n" + "="*50)
    print("LIBRARY COLLECTION")
    print("="*50)
    for book_id, book in library.items():
        print(f"ID: {book_id} | Title: {book[0]} | Author: {book[1]} | Year: {book[2]}")

def suggest_random_book(library):
    import random
    
    if not library:
        print("No books available for suggestion!")
        return None
    
    book_id = random.choice(list(library.keys()))
    return book_id, library[book_id]

def get_book_statistics(library, genres):
    print("\n" + "="*50)
    print("LIBRARY STATISTICS")
    print("="*50)
    print(f"Total books: {len(library)}")
    print(f"Available genres: {', '.join(genres)}")
    
    # Find oldest and newest book
    if library:
        years = [book[2] for book in library.values()]
        print(f"Oldest book: {min(years)}")
        print(f"Newest book: {max(years)}")