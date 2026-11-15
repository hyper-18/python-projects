import json
import os
import re

from contact import Contact


class ContactManager:

    def __init__(self):
        self.contacts = []
        self.filename = "contacts.json"
        self.load_contacts()

    # Add Contact
    def add_contact(self, contact):

        for existing in self.contacts:
            if existing.name.lower() == contact.name.lower():
                print("Contact with this name already exists!")
                return

            if existing.phone == contact.phone:
                print("This phone number is already registered!")
                return

        if not self.validate_phone(contact.phone):
            print("Invalid phone number!")
            return

        if not self.validate_email(contact.email):
            print("Invalid email address!")
            return

        self.contacts.append(contact)
        self.save_contacts()

        print("Contact added successfully!")

    # View Contacts
    def view_contacts(self):

        if not self.contacts:
            print("No contacts found.")
            return

        for index, contact in enumerate(self.contacts, start=1):
            print(f"\nContact #{index}")
            contact.display_contact()
            print("--------------------")

    # Search Contact
    def search_contact(self, name):

        found = False

        for contact in self.contacts:

            if name.lower() in contact.name.lower():
                contact.display_contact()
                print("--------------------")
                found = True

        if not found:
            print("Contact not found!")

    # Update Contact
    def update_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                new_name = input("Enter new name: ").strip()
                new_phone = input("Enter new phone: ").strip()
                new_email = input("Enter new email: ").strip()

                if not new_name or not new_phone or not new_email:
                    print("All fields are required!")
                    return

                for existing in self.contacts:
                    if existing is not contact:
                        if existing.name.lower() == new_name.lower():
                            print("Another contact already uses this name!")
                            return

                        if existing.phone == new_phone:
                            print("This phone number is already registered!")
                            return

                if not self.validate_phone(new_phone):
                    print("Invalid phone number!")
                    return

                if not self.validate_email(new_email):
                    print("Invalid email address!")
                    return

                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email

                self.save_contacts()

                print("Contact updated successfully!")
                return

        print("Contact not found!")

    # Delete Contact
    def delete_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)
                self.save_contacts()

                print("Contact deleted successfully!")
                return

        print("Contact not found!")

    # Validate Phone Number
    def validate_phone(self, phone):

        return re.fullmatch(r"[6-9]\d{9}", phone) is not None

    # Validate Email
    def validate_email(self, email):

        pattern = r"^[\w.+-]+@[\w-]+\.[A-Za-z]{2,}$"

        return re.fullmatch(pattern, email) is not None

    # Save Contacts
    def save_contacts(self):

        data = []

        for contact in self.contacts:
            data.append({
                "name": contact.name,
                "phone": contact.phone,
                "email": contact.email
            })

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    # Load Contacts
    def load_contacts(self):

        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                contact = Contact(
                    item["name"],
                    item["phone"],
                    item["email"]
                )

                self.contacts.append(contact)

        except (json.JSONDecodeError, KeyError, TypeError):
            print("Warning: Could not load contact data.")
