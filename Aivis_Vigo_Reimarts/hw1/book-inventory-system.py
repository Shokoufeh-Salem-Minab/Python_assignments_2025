import json


class Book:
    def __init__(self, isbn, title, author, price, quantity):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.quantity = quantity
    
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "price": self.price,
            "quantity": self.quantity
        }
    
    @staticmethod
    def from_dict(isbn, data):
        return Book(isbn, data["title"], data["author"], data["price"], data["quantity"])
    
    def display(self):
        print(f"ISBN:     {self.isbn}")
        print(f"Title:    {self.title}")
        print(f"Author:   {self.author}")
        print(f"Price:    ${self.price:.2f}")
        print(f"Quantity: {self.quantity}")


class Inventory:
    def __init__(self, filename="inventory.json"):
        self.filename = filename
        self.books = {}
        self.load()
    
    def load(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.books = {isbn: Book.from_dict(isbn, book_data) 
                             for isbn, book_data in data.items()}
        except FileNotFoundError:
            self.books = {
                "978-0-544-83970-8": Book("978-0-544-83970-8", "Wool", "Hugh Howey", 16.99, 12),
                "978-0-544-83971-5": Book("978-0-544-83971-5", "Shift", "Hugh Howey", 16.99, 10),
                "978-0-544-83972-2": Book("978-0-544-83972-2", "Dust", "Hugh Howey", 16.99, 8)
            }
    
    def save(self):
        data = {isbn: book.to_dict() for isbn, book in self.books.items()}
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_book(self, book):
        if book.isbn in self.books:
            return False
        self.books[book.isbn] = book
        self.save()
        return True
    
    def find_by_isbn(self, isbn):
        return self.books.get(isbn)
    
    def search_by_keyword(self, keyword):
        keyword_lower = keyword.lower()
        results = []
        for book in self.books.values():
            if (keyword_lower in book.title.lower() or 
                keyword_lower in book.author.lower()):
                results.append(book)
        return results
    
    def delete_book(self, isbn):
        if isbn in self.books:
            book = self.books[isbn]
            del self.books[isbn]
            self.save()
            return book
        return None
    
    def get_all_books(self):
        return list(self.books.values())
    
    def is_empty(self):
        return len(self.books) == 0
    
    def get_statistics(self):
        if self.is_empty():
            return None
        
        total_books = len(self.books)
        total_quantity = sum(book.quantity for book in self.books.values())
        total_value = sum(book.price * book.quantity for book in self.books.values())
        
        prices = [book.price for book in self.books.values()]
        avg_price = sum(prices) / len(prices)
        min_price = min(prices)
        max_price = max(prices)
        
        quantities = [book.quantity for book in self.books.values()]
        avg_quantity = sum(quantities) / len(quantities)
        
        authors = {}
        for book in self.books.values():
            authors[book.author] = authors.get(book.author, 0) + 1
        
        most_common_author = max(authors, key=authors.get)
        
        most_expensive = max(self.books.values(), key=lambda b: b.price)
        least_expensive = min(self.books.values(), key=lambda b: b.price)
        most_stock = max(self.books.values(), key=lambda b: b.quantity)
        least_stock = min(self.books.values(), key=lambda b: b.quantity)
        
        return {
            "total_books": total_books,
            "total_quantity": total_quantity,
            "total_value": total_value,
            "avg_price": avg_price,
            "min_price": min_price,
            "max_price": max_price,
            "avg_quantity": avg_quantity,
            "most_common_author": most_common_author,
            "author_count": len(authors),
            "most_expensive": most_expensive,
            "least_expensive": least_expensive,
            "most_stock": most_stock,
            "least_stock": least_stock
        }


class BookstoreUI:
    def __init__(self, inventory):
        self.inventory = inventory
    
    def display_menu(self):
        print("\n" + "="*50)
        print("BOOKSTORE INVENTORY MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Add a new book")
        print("2. Search by ISBN")
        print("3. Search by title or author")
        print("4. List all books")
        print("5. Delete a book")
        print("6. Display statistics")
        print("7. Exit")
        print("="*50)
    
    def add_book(self):
        print("\n--- ADD NEW BOOK ---")
        
        isbn = input("Enter ISBN: ").strip()
        
        if self.inventory.find_by_isbn(isbn):
            print(f"\nERROR: Book with ISBN '{isbn}' already exists in inventory!")
            return
        
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()
        
        while True:
            try:
                price = float(input("Enter price: $"))
                if price < 0:
                    print("Price cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid price. Please enter a number.")
        
        while True:
            try:
                quantity = int(input("Enter quantity in stock: "))
                if quantity < 0:
                    print("Quantity cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid quantity. Please enter a whole number.")
        
        book = Book(isbn, title, author, price, quantity)
        self.inventory.add_book(book)
        print(f"\nBook '{title}' successfully added to inventory!")
    
    def search_by_isbn(self):
        print("\n--- SEARCH BY ISBN ---")
        
        isbn = input("Enter ISBN to search: ").strip()
        
        book = self.inventory.find_by_isbn(isbn)
        if book:
            print("\n" + "="*50)
            print("BOOK FOUND:")
            print("="*50)
            book.display()
            print("="*50)
        else:
            print(f"\nERROR: No book found with ISBN '{isbn}'")
    
    def search_by_title_or_author(self):
        print("\n--- SEARCH BY TITLE OR AUTHOR ---")
        
        keyword = input("Enter search keyword: ").strip()
        
        if not keyword:
            print("\nERROR: Search keyword cannot be empty!")
            return
        
        results = self.inventory.search_by_keyword(keyword)
        
        if results:
            print(f"\n{len(results)} book(s) found:")
            print("="*80)
            for book in results:
                book.display()
                print("-"*80)
        else:
            print(f"\nNo books found matching '{keyword}'")
    
    def list_all_books(self):
        print("\n--- ALL BOOKS IN INVENTORY ---")
        
        if self.inventory.is_empty():
            print("\nInventory is empty!")
            return
        
        books = self.inventory.get_all_books()
        print(f"\nTotal books in inventory: {len(books)}")
        print("="*80)
        
        for book in books:
            book.display()
            print("-"*80)
    
    def delete_book(self):
        print("\n--- DELETE BOOK ---")
        
        isbn = input("Enter ISBN of book to delete: ").strip()
        
        book = self.inventory.delete_book(isbn)
        if book:
            print(f"\nBook '{book.title}' (ISBN: {isbn}) successfully deleted from inventory!")
        else:
            print(f"\nERROR: No book found with ISBN '{isbn}'")
    
    def display_statistics(self):
        print("\n--- INVENTORY STATISTICS ---")
        
        stats = self.inventory.get_statistics()
        
        if stats is None:
            print("\nInventory is empty! No statistics available.")
            return
        
        print("\n" + "="*60)
        print("GENERAL STATISTICS")
        print("="*60)
        print(f"Total unique books:        {stats['total_books']}")
        print(f"Total items in stock:      {stats['total_quantity']}")
        print(f"Total inventory value:     ${stats['total_value']:.2f}")
        print(f"Number of authors:         {stats['author_count']}")
        print(f"Most common author:        {stats['most_common_author']}")
        
        print("\n" + "="*60)
        print("PRICE STATISTICS")
        print("="*60)
        print(f"Average book price:        ${stats['avg_price']:.2f}")
        print(f"Minimum price:             ${stats['min_price']:.2f}")
        print(f"Maximum price:             ${stats['max_price']:.2f}")
        
        print("\n" + "="*60)
        print("QUANTITY STATISTICS")
        print("="*60)
        print(f"Average stock per book:    {stats['avg_quantity']:.2f}")
        
        print("\n" + "="*60)
        print("EXTREMES")
        print("="*60)
        print(f"Most expensive book:       {stats['most_expensive'].title} (${stats['most_expensive'].price:.2f})")
        print(f"Least expensive book:      {stats['least_expensive'].title} (${stats['least_expensive'].price:.2f})")
        print(f"Highest stock:             {stats['most_stock'].title} ({stats['most_stock'].quantity} units)")
        print(f"Lowest stock:              {stats['least_stock'].title} ({stats['least_stock'].quantity} units)")
        print("="*60)
    
    def run(self):
        while True:
            self.display_menu()
            
            choice = input("\nEnter your choice (1-7): ").strip()
            
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.search_by_isbn()
            elif choice == '3':
                self.search_by_title_or_author()
            elif choice == '4':
                self.list_all_books()
            elif choice == '5':
                self.delete_book()
            elif choice == '6':
                self.display_statistics()
            elif choice == '7':
                self.inventory.save()
                print("\nThank you for using the Bookstore Inventory Management System!")
                print("Goodbye!")
                break
            else:
                print("\nInvalid choice! Please enter a number between 1 and 7.")
            
            input("\nPress Enter to continue...")


def main():
    inventory = Inventory()
    ui = BookstoreUI(inventory)
    ui.run()


if __name__ == "__main__":
    main()
