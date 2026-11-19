from expense import Expense


class ExpenseSplitter:

    def __init__(self):
        self.participants = []
        self.expenses = []
        self.balances = {}

    # Add participants
    def add_participant(self, name):

        if name in self.participants:
            print("Participant already exists!")
            return

        self.participants.append(name)
        self.balances[name] = 0

        print(f"{name} added successfully!")

    # View participants
    def view_participants(self):

        if not self.participants:
            print("No participants found!")
            return

        print("\nParticipants:")

        for index, name in enumerate(self.participants, start=1):
            print(f"{index}. {name}")

    # Add expense
    def add_expense(self, description, amount, paid_by, participants):

        if paid_by not in self.participants:
            print("Person who paid is not registered!")
            return

        if amount <= 0:
            print("Amount must be greater than zero!")
            return

        if not participants:
            print("At least one participant is required!")
            return

        for person in participants:
            if person not in self.participants:
                print(f"{person} is not registered!")
                return

        if len(set(participants)) != len(participants):
            print("Duplicate participants are not allowed!")
            return

        expense = Expense(
            description,
            amount,
            paid_by,
            participants
        )

        self.expenses.append(expense)

        share = amount / len(participants)

        self.balances[paid_by] += amount

        for person in participants:
            self.balances[person] -= share

        print("Expense added successfully!")

    # View expenses
    def view_expenses(self):

        if not self.expenses:
            print("No expenses recorded!")
            return

        for index, expense in enumerate(self.expenses, start=1):

            print(f"\nExpense #{index}")
            expense.display_expense()

    # View balances
    def view_balances(self):

        if not self.participants:
            print("No participants found!")
            return

        print("\n===== BALANCE SUMMARY =====")

        for person, balance in self.balances.items():

            if balance > 0:
                print(f"{person} should receive ₹{balance:.2f}")

            elif balance < 0:
                print(f"{person} owes ₹{abs(balance):.2f}")

            else:
                print(f"{person} is settled!")

    # Calculate settlements
    def settle_expenses(self):

        creditors = []
        debtors = []

        for person, balance in self.balances.items():

            if balance > 0:
                creditors.append([person, balance])

            elif balance < 0:
                debtors.append([person, abs(balance)])

        print("\n===== SETTLEMENT SUMMARY =====")

        i = 0
        j = 0

        while i < len(debtors) and j < len(creditors):

            amount = min(debtors[i][1], creditors[j][1])

            print(
                f"{debtors[i][0]} pays "
                f"{creditors[j][0]} ₹{amount:.2f}"
            )

            debtors[i][1] -= amount
            creditors[j][1] -= amount

            if debtors[i][1] < 0.01:
                i += 1

            if creditors[j][1] < 0.01:
                j += 1

        if not debtors and not creditors:
            print("All expenses are settled!")
