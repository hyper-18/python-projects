from datetime import date


class Expense:
    def __init__(self, amount, category, description, expense_date=None):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = expense_date or str(date.today())

    def display_expense(self):
        print(f"Amount: ₹{self.amount:,.2f}")
        print(f"Category: {self.category}")
        print(f"Description: {self.description}")
        print(f"Date: {self.date}")
