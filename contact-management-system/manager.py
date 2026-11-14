from contact import Contact


class ContactManager:

    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully!")

    def view_contacts(self):

        if not self.contacts:
            print("No contacts found.")
            return

        for index, contact in enumerate(self.contacts, start=1):

            print(f"\nContact #{index}")
            contact.display_contact()
            print("--------------------")

    def search_contact(self, name):

        found = False

        for contact in self.contacts:

            if name.lower() in contact.name.lower():

                contact.display_contact()
                print("--------------------")
                found = True

        if not found:
            print("Contact not found!")

    def update_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                print("\nEnter new details:")

            new_name = input("Enter new name: ").strip()
            new_phone = input("Enter new phone: ").strip()
            new_email = input("Enter new email: ").strip()

            if not new_name or not new_phone or not new_email:
                print("All fields are required!")
                return

            contact.name = new_name
            contact.phone = new_phone
            contact.email = new_email

            print("Contact updated successfully!")
            return

    print("Contact not found!")

    def delete_contact(self, name):

        for contact in self.contacts:

            if contact.name.lower() == name.lower():

                self.contacts.remove(contact)

                print("Contact deleted successfully!")
                return

        print("Contact not found!")
