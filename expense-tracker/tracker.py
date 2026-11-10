from expense import Expense


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)
        print("Expense added successfully")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found")
        else:
            for expense in self.expenses:
                expense.display_expense()
                print("----------------------")

    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense.amount
        return total
