from splitter import ExpenseSplitter


splitter = ExpenseSplitter()


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
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        # Add Participant
        if choice == "1":

            name = input("Enter participant name: ").strip()

            if not name:
                print("Name cannot be empty!")
                continue

            splitter.add_participant(name)

        # View Participants
        elif choice == "2":

            splitter.view_participants()

        # Add Expense
        elif choice == "3":

            if not splitter.participants:
                print("Add participants before recording expenses!")
                continue

            description = input("Enter expense description: ").strip()

            try:
                amount = float(input("Enter total amount: "))

            except ValueError:
                print("Please enter a valid amount!")
                continue

            paid_by = input("Who paid? ").strip()

            splitter.view_participants()

            names = input(
                "Enter participant names separated by commas: "
            )

            participants = [
                name.strip()
                for name in names.split(",")
                if name.strip()
            ]

            if not description or not paid_by:
                print("Description and payer are required!")
                continue

            splitter.add_expense(
                description,
                amount,
                paid_by,
                participants
            )

        # View Expenses
        elif choice == "4":

            splitter.view_expenses()

        # View Balances
        elif choice == "5":

            splitter.view_balances()

        # Settle Expenses
        elif choice == "6":

            splitter.settle_expenses()

        # Exit
        elif choice == "7":

            print("Thank you for using Expense Splitter!")
            break

        else:

            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
