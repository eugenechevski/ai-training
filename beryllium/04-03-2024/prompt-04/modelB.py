import json

class Book:
    def __init__(self, title, author, ISBN, status="available"):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.status = status

class BookCollection:
    def __init__(self):
        self.books = []
        self.load_books()

    def add_book(self, title, author, ISBN):
        book = Book(title, author, ISBN)
        self.books.append(book)
        self.save_books()

    def remove_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                self.books.remove(book)
                self.save_books()
                return
        print(f"Book with ISBN {ISBN} not found.")

    def find_book(self, ISBN):
        for book in self.books:
            if book.ISBN == ISBN:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author} (ISBN: {book.ISBN}, Status: {book.status})")

    def check_out_book(self, ISBN):
        book = self.find_book(ISBN)
        if book:
            if book.status == "available":
                book.status = "checked out"
                self.save_books()
                print(f"Book '{book.title}' by {book.author} has been checked out.")
            else:
                print(f"Book '{book.title}' by {book.author} is already checked out.")
        else:
            print(f"Book with ISBN {ISBN} not found.")

    def return_book(self, ISBN):
        book = self.find_book(ISBN)
        if book:
            if book.status == "checked out":
                book.status = "available"
                self.save_books()
                print(f"Book '{book.title}' by {book.author} has been returned.")
            else:
                print(f"Book '{book.title}' by {book.author} is already available.")
        else:
            print(f"Book with ISBN {ISBN} not found.")

    def load_books(self):
        try:
            with open("book_collection.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            pass

    def save_books(self):
        with open("book_collection.json", "w") as file:
            json.dump(self.books, file, indent=4)

if __name__ == "__main__":
    collection = BookCollection()

    # Adding books
    collection.add_book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
    collection.add_book("To Kill a Mockingbird", "Harper Lee", "9780060935467")
    collection.add_book("1984", "George Orwell", "9780451524935")

    # Listing books
    collection.list_books()

    # Checking out a book
    collection.check_out_book("9780451524935")

    # Returning a book
    collection.return_book("9780743273565")

    # Finding a book
    book = collection.find_book("9780060935467")
    if book:
        print(f"Book '{book.title}' by {book.author} is currently {book.status}.")
    else:
        print("Book not found.")

    # Removing a book
    collection.remove_book("9780451524935")