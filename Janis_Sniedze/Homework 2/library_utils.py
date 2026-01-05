import random  # select a random (id, book) pair for suggestions
from typing import Dict, Tuple, List, Optional  # type helpers for clarity

booksList: List[str] = ["Python 101", "Data Science", "Machine Learning"]  # example titles used elsewhere

genres = {"Programming", "AI", "Math"}  # sample genre set for illustrative purposes

# mapping from id -> (title, author, year) stored as a simple dict
libraryData: Dict[int, Tuple[str, str, int]] = {
    1: ("Python 101", "John Smith", 2020),  # id 1 stores a tuple with title, author, year
    2: ("Data Science", "Alice Brown", 2021),  # id 2 stores another example entry
}


def addBook(libraryDict: Dict[int, Tuple[str, str, int]], bookId: int, book: Tuple[str, str, int]) -> bool:  # add book at id when free, return success flag
    if bookId in libraryDict:  # check if the requested id already holds a book
        return False  # return False to indicate the id was already used and no insertion happened
    libraryDict[bookId] = book  # place the provided book tuple at the given id key
    return True  # return True to indicate the book was successfully added


def searchBook(libraryDict: Dict[int, Tuple[str, str, int]], title: str) -> List[Tuple[int, Tuple[str, str, int]]]:  # find entries that exactly match title (case-insensitive)
    titleLower = title.strip().lower()  # normalize the incoming title for robust comparison
    results: List[Tuple[int, Tuple[str, str, int]]] = []  # prepare collection for matches
    for bid, book in libraryDict.items():  # iterate through stored pairs to compare titles
        if book[0].lower() == titleLower:  # match when stored title equals normalized search term
            results.append((bid, book))  # append the id and book tuple for each match
    return results  # return all matches found (possibly empty)


def listBooks(libraryDict: Dict[int, Tuple[str, str, int]]) -> List[Tuple[int, str, str, int]]:  # return a simple list of readable book tuples
    return [(bid, b[0], b[1], b[2]) for bid, b in libraryDict.items()]  # each item is (id, title, author, year)


def suggestRandomBook(libraryDict: Dict[int, Tuple[str, str, int]]) -> Optional[Tuple[int, Tuple[str, str, int]]]:  # return a random library entry or None
    if not libraryDict:  # when dictionary empty there is nothing to suggest
        return None  # explicit None signals no suggestion
    return random.choice(list(libraryDict.items()))  # choose a random (id, book) pair and return it


__all__ = ["booksList", "genres", "libraryData", "addBook", "searchBook", "listBooks", "suggestRandomBook"]  # public API for imports
