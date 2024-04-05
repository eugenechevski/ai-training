import pickle

class Book:
    def __init__(self, title, author, ISBN, status="available"):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status

class BookCollection:
    def __init__(self):
        self.books = []
        self.file_path = "book_collection.pkl"

        # Load existing data from file
        self.load_data()

    def add_book(self, title, author, ISBN):
        # Create a new book and add it to the collection
        book = Book(title, author, ISBN)
        self.books.append(book)
        self.save_data()

    def remove_book(self, ISBN):
        # Find the book with the given ISBN and remove it from the collection
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                self.save_data()
                return

    def find_book(self, ISBN):
        # Find and return the book with the given ISBN (if it exists)
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None

    def list_books(self):
        # List all books in the collection with their details
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.ISBN}, Status: {book.status}")

    def check_out_book(self, ISBN):
        # Find the book with the given ISBN and set its status to "checked out"
        book = self.find_book(ISBN)
        if book:
            book.status = "checked out"
            self.save_data()

    def return_book(self, ISBN):
        # Find the book with the given ISBN and set its status to "available"
        book = self.find_book(ISBN)
        if book:
            book.status = "available"
            self.save_data()

    def save_data(self):
        # Save the current book collection state to a file
        with open(self.file_path, "wb") as f:
            pickle.dump(self.books, f)

    def load_data(self):
        # Load existing data from the file (if any)
        try:
            with open(self.file_path, "rb") as f:
                self.books = pickle.load(f)
        except FileNotFoundError:
            pass  # No data to load
        
if __name__ == "__main__":
    collection = BookCollection()

    # Add some books
    collection.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    collection.add_book("To Kill a Mockingbird", "Harper Lee", "9780060935467")

    # List all books
    collection.list_books()

    # Check out a book
    collection.check_out_book("9780743273565")

    # List all books (again)
    collection.list_books()

    # Return a book
    collection.return_book("9780060935467")

    # Find a book
    book = collection.find_book("9780743273565")
    if book:
        print(f"Book found: {book.title}")
    else:
        print("Book not found.")