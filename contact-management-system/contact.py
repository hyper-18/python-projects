class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display_contact(self):
        print("Name:", self.name)
        print("Phone:", self.phone)
        print("Email:", self.email)
