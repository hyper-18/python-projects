from datetime import date


class Expense:
    def __init__(self, amount, category, description):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date.today()

    def display_expense(self):
        print(f"Amount: ${self.amount:,.2f}")
        print("Category:", self.category)
        print("Description:", self.description)
        print("Date:", self.date)
