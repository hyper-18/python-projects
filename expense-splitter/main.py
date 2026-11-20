from splitter import ExpenseSplitter


splitter = ExpenseSplitter()


def get_expense_details():

    description = input("Enter expense description: ").strip()

    try:
        amount = float(input("Enter amount: "))

    except ValueError:
        print("Please enter a valid amount!")
        return None

    paid_by = input("Who paid? ").strip()

    splitter.view_participants()

    names = input(
        "Enter participants separated by commas: "
    )

    participants = [
        name.strip()
        for name in names.split(",")
        if name.strip()
    ]

    return description, amount, paid_by, participants


def main():

    while True:

        print("\n================================")
        print("       EXPENSE SPLITTER")
        print("================================")

        print("1. Add Participant")
        print("2. View Participants")
        print("3. Add Expense")
        print("4. View Expenses")
        print("5. View Balances")
        print("6. Settle Expenses")
        print("7. Edit Expense")
        print("8. Delete Expense")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        # Add participant
        if choice == "1":

            name = input("Enter participant name: ")

            splitter.add_participant(name)

        # View participants
        elif choice == "2":

            splitter.view_participants()

        # Add expense
        elif choice == "3":

            if not splitter.participants:
                print("Add participants first!")
                continue

            details = get_expense_details()

            if details is None:
                continue

            description, amount, paid_by, participants = details

            splitter.add_expense(
                description,
                amount,
                paid_by,
                participants
            )

        # View expenses
        elif choice == "4":

            splitter.view_expenses()

        # View balances
        elif choice == "5":

            splitter.view_balances()

        # Settle expenses
        elif choice == "6":

            splitter.settle_expenses()

        # Edit expense
        elif choice == "7":

            splitter.view_expenses()

            if not splitter.expenses:
                continue

            try:
                index = int(input("Enter expense number to edit: "))

            except ValueError:
                print("Invalid expense number!")
                continue

            details = get_expense_details()

            if details is None:
                continue

            description, amount, paid_by, participants = details

            splitter.edit_expense(
                index,
                description,
                amount,
                paid_by,
                participants
            )

        # Delete expense
        elif choice == "8":

            splitter.view_expenses()

            if not splitter.expenses:
                continue

            try:
                index = int(input("Enter expense number to delete: "))

            except ValueError:
                print("Invalid expense number!")
                continue

            splitter.delete_expense(index)

        # Exit
        elif choice == "9":

            print("Thank you for using Expense Splitter!")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
