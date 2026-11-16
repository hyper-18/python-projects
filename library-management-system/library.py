from book import Book


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added sucessfully")

    def view_books(self):
        if not self.books:
            print("No books found")
            return
        for index, book in enumerate(self.books, start=1):
            print(f"\nBook #{index}")
            print("Title:", book.title)
            print("Author:", book.author)
            print("ISBN:", book.isbn)
            print("Available:", book.available)
            print("--------------------")

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

    def issue_books(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print("Book issues sucessfully")
                else:
                    print("this book is already issuesd")
                return
            print("Book not found")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print("Book returned sucessfully")
                else:
                    print("this book was not issued")
                return
        print("Book not found")

    def delete_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    print("Cannot delete an issued book")
                    return
                self.book.remove(book)
                print("Book deleted successfully")
                return
        print("Book not found")
