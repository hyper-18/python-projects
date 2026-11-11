import json
import os
from expense import Expense


class ExpenseTracker:

    def __init__(self):
        self.expenses = []
        self.filename = "expenses.json"
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for index, expense in enumerate(self.expenses, start=1):
            print(f"\nExpense #{index}")
            expense.display_expense()
            print("--------------------")

    def calculate_total(self):
        total = sum(expense.amount for expense in self.expenses)
        return total

    def save_expenses(self):
        data = []

        for expense in self.expenses:
            data.append({
                "amount": expense.amount,
                "category": expense.category,
                "description": expense.description,
                "date": expense.date
            })

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_expenses(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                expense = Expense(
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["date"]
                )
                self.expenses.append(expense)

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Warning: Could not load expense data.")

    def delete_expense(self):
        self.view_expenses()

        if not self.expenses:
            return

        try:
            index = int(input("Enter expense number to delete: "))

            if 1 <= index <= len(self.expenses):
                removed = self.expenses.pop(index - 1)
                self.save_expenses()
                print(f"{removed.category} expense deleted successfully!")
            else:
                print("Invalid expense number.")

        except ValueError:
            print("Please enter a valid number.")
