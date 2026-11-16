from book import Book
from library import Library

library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        title = input("Enter book title: ").strip()
        author = input("Enter author: ").strip()
        isbn = input("Enter ISBN: ").strip()

        if not title or not author or not isbn:
            print("All fields are required!")
            continue

        book = Book(title, author, isbn)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        search_term = input("Enter title or author: ").strip()

        if not search_term:
            print("Search term cannot be empty!")
            continue

        library.search_book(search_term)

    elif choice == "4":
        isbn = input("Enter ISBN to issue: ").strip()

        if not isbn:
            print("ISBN cannot be empty!")
            continue

        library.issue_book(isbn)

    elif choice == "5":
        isbn = input("Enter ISBN to return: ").strip()

        if not isbn:
            print("ISBN cannot be empty!")
            continue

        library.return_book(isbn)

    elif choice == "6":
        isbn = input("Enter ISBN to delete: ").strip()

        if not isbn:
            print("ISBN cannot be empty!")
            continue

        library.delete_book(isbn)

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
