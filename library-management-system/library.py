import json
import os
from book import Book


class Library:

    def __init__(self):
        self.books = []
        self.filename = "books.json"
        self.load_books()

    # Add a book
    def add_book(self, book):

        for existing_book in self.books:
            if existing_book.isbn == book.isbn:
                print("A book with this ISBN already exists!")
                return

        self.books.append(book)
        self.save_books()
        print("Book added successfully!")

    # View all books
    def view_books(self):

        if not self.books:
            print("No books found!")
            return

        for index, book in enumerate(self.books, start=1):
            print(f"\nBook #{index}")
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            print("Available:", book.available)
            print("--------------------")

    # Search books
    def search_book(self, search_term):

        found = False

        for book in self.books:

            if (search_term.lower() in book.title.lower()
                    or search_term.lower() in book.author.lower()):

                print("\nBook Found!")
                print("Title:", book.title)
                print("Author:", book.author)
                print("ISBN:", book.isbn)
                print("Available:", book.available)

                found = True

        if not found:
            print("Book not found!")

    # Issue a book
    def issue_book(self, isbn):

        for book in self.books:

            if book.isbn == isbn:

                if book.available:
                    book.available = False
                    self.save_books()
                    print("Book issued successfully!")

                else:
                    print("This book is already issued!")

                return

        print("Book not found!")

    # Return a book
    def return_book(self, isbn):

        for book in self.books:

            if book.isbn == isbn:

                if not book.available:
                    book.available = True
                    self.save_books()
                    print("Book returned successfully!")

                else:
                    print("This book was not issued!")

                return

        print("Book not found!")

    # Delete a book
    def delete_book(self, isbn):

        for book in self.books:

            if book.isbn == isbn:

                if not book.available:
                    print("Cannot delete an issued book!")
                    return

                self.books.remove(book)
                self.save_books()
                print("Book deleted successfully!")
                return

        print("Book not found!")

    # Save books to JSON
    def save_books(self):

        books_data = []

        for book in self.books:

            book_data = {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "available": book.available
            }

            books_data.append(book_data)

        with open(self.filename, "w") as file:
            json.dump(books_data, file, indent=4)

    # Load books from JSON
    def load_books(self):

        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                books_data = json.load(file)

            for book_data in books_data:

                book = Book(
                    book_data["title"],
                    book_data["author"],
                    book_data["isbn"],
                    book_data["available"]
                )

                self.books.append(book)

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Error: Unable to load library data!")
            self.books = []
