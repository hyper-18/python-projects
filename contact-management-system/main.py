from contact import Contact
from manager import ContactManager


manager = ContactManager()

while True:

    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()

        if not name or not phone or not email:
            print("All fields are required!")
            continue

        contact = Contact(name, phone, email)
        manager.add_contact(contact)

    elif choice == "2":

        manager.view_contacts()

    elif choice == "3":

        name = input("Enter name to search: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        manager.search_contact(name)

    elif choice == "4":

        name = input("Enter contact name to update: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        manager.update_contact(name)

    elif choice == "5":

        name = input("Enter contact name to delete: ").strip()

        if not name:
            print("Name cannot be empty!")
            continue

        manager.delete_contact(name)

    elif choice == "6":

        print("Thank you for using Contact Management System!")
        break

    else:

        print("Invalid choice! Please try again.")
