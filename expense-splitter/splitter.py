import json
import os

from expense import Expense


class ExpenseSplitter:

    def __init__(self):

        self.participants = []
        self.expenses = []
        self.filename = "data.json"

        self.load_data()

    # Add participant
    def add_participant(self, name):

        name = name.strip()

        if not name:
            print("Name cannot be empty!")
            return

        if name.lower() in [p.lower() for p in self.participants]:
            print("Participant already exists!")
            return

        self.participants.append(name)

        self.save_data()

        print(f"{name} added successfully!")

    # View participants
    def view_participants(self):

        if not self.participants:
            print("No participants found!")
            return

        print("\n===== PARTICIPANTS =====")

        for index, name in enumerate(self.participants, start=1):
            print(f"{index}. {name}")

    # Add expense
    def add_expense(self, description, amount, paid_by, participants):

        description = description.strip()
        paid_by = paid_by.strip()

        if not description:
            print("Description cannot be empty!")
            return

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            print("Invalid amount!")
            return

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        if not paid_by:
            print("Payer cannot be empty!")
            return

        if paid_by.lower() not in [p.lower() for p in self.participants]:
            print("Payer is not registered!")
            return

        if not participants:
            print("At least one participant is required!")
            return

        if len(set(p.lower() for p in participants)) != len(participants):
            print("Duplicate participants are not allowed!")
            return

        if not all(p in self.participants for p in participants):
            print("One or more participants are not registered!")
            return

        expense = Expense(
            description,
            round(amount, 2),
            paid_by,
            participants
        )

        self.expenses.append(expense)

        self.save_data()

        print("Expense added successfully!")

    # View expenses
    def view_expenses(self):

        if not self.expenses:
            print("No expenses recorded!")
            return

        print("\n===== EXPENSE HISTORY =====")

        for index, expense in enumerate(self.expenses, start=1):

            print(f"\nExpense #{index}")

            expense.display_expense()

    # Calculate balances
    def calculate_balances(self):

        balances = {
            person: 0.0
            for person in self.participants
        }

        for expense in self.expenses:

            share = expense.amount / len(expense.participants)

            payer = next(
                p for p in self.participants
                if p.lower() == expense.paid_by.lower()
            )

            balances[payer] += expense.amount

            for person in expense.participants:

                actual_person = next(
                    p for p in self.participants
                    if p.lower() == person.lower()
                )

                balances[actual_person] -= share

        return balances

    # View balances
    def view_balances(self):

        if not self.participants:
            print("No participants found!")
            return

        balances = self.calculate_balances()

        print("\n===== BALANCE SUMMARY =====")

        for person, balance in balances.items():

            balance = round(balance, 2)

            if balance > 0.01:
                print(f"{person} should receive ₹{balance:.2f}")

            elif balance < -0.01:
                print(f"{person} owes ₹{abs(balance):.2f}")

            else:
                print(f"{person} is settled!")

    # Generate settlements
    def settle_expenses(self):

        balances = self.calculate_balances()

        creditors = []
        debtors = []

        for person, balance in balances.items():

            balance = round(balance, 2)

            if balance > 0.01:
                creditors.append([person, balance])

            elif balance < -0.01:
                debtors.append([person, abs(balance)])

        print("\n===== SETTLEMENT SUMMARY =====")

        if not creditors and not debtors:
            print("All expenses are settled!")
            return

        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):

            amount = min(
                debtors[i][1],
                creditors[j][1]
            )

            amount = round(amount, 2)

            print(
                f"{debtors[i][0]} pays "
                f"{creditors[j][0]} ₹{amount:.2f}"
            )

            debtors[i][1] = round(debtors[i][1] - amount, 2)
            creditors[j][1] = round(creditors[j][1] - amount, 2)

            if debtors[i][1] <= 0.01:
                i += 1

            if creditors[j][1] <= 0.01:
                j += 1

    # Delete expense
    def delete_expense(self, index):

        if index < 1 or index > len(self.expenses):
            print("Invalid expense number!")
            return

        deleted_expense = self.expenses.pop(index - 1)

        self.save_data()

        print(
            f"Expense '{deleted_expense.description}' "
            "deleted successfully!"
        )

    # Edit expense
    def edit_expense(self, index, description, amount, paid_by, participants):

        if index < 1 or index > len(self.expenses):
            print("Invalid expense number!")
            return

        description = description.strip()
        paid_by = paid_by.strip()

        if not description:
            print("Description cannot be empty!")
            return

        if not isinstance(amount, (int, float)) or isinstance(amount, bool):
            print("Invalid amount!")
            return

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        if paid_by.lower() not in [p.lower() for p in self.participants]:
            print("Payer is not registered!")
            return

        if not participants:
            print("At least one participant is required!")
            return

        if len(set(p.lower() for p in participants)) != len(participants):
            print("Duplicate participants are not allowed!")
            return

        if not all(p in self.participants for p in participants):
            print("One or more participants are not registered!")
            return

        updated_expense = Expense(
            description,
            round(amount, 2),
            paid_by,
            participants
        )

        self.expenses[index - 1] = updated_expense

        self.save_data()

        print("Expense updated successfully!")

    # Save data to JSON
    def save_data(self):

        data = {
            "participants": self.participants,
            "expenses": []
        }

        for expense in self.expenses:

            data["expenses"].append({
                "description": expense.description,
                "amount": expense.amount,
                "paid_by": expense.paid_by,
                "participants": expense.participants
            })

        try:

            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except OSError as error:
            print("Unable to save data:", error)

    # Load data from JSON
    def load_data(self):

        if not os.path.exists(self.filename):
            self.save_data()
            return

        try:

            with open(self.filename, "r") as file:
                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Invalid data format!")

            participants = data.get("participants", [])
            expenses = data.get("expenses", [])

            if not isinstance(participants, list) or not isinstance(expenses, list):
                raise ValueError("Invalid data structure!")

            self.participants = participants

            for item in expenses:

                expense = Expense(
                    item["description"],
                    item["amount"],
                    item["paid_by"],
                    item["participants"]
                )

                self.expenses.append(expense)

            print("Previous data loaded successfully!")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Error: Library data is corrupted or invalid!")
            self.participants = []
            self.expenses = []

        except OSError as error:
            print("Unable to read data:", error)
