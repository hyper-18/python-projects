from expense import Expense
from tracker import ExpenseTracker


tracker = ExpenseTracker()

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be greater than zero!")
                continue

        except ValueError:
            print("Invalid amount!")
            continue

        category = input("Enter category: ").strip()

        if not category:
            print("Category cannot be empty!")
            continue

        description = input("Enter description: ").strip()

        if not description:
            print("Description cannot be empty!")
            continue

        expense = Expense(amount, category, description)
        tracker.add_expense(expense)

    elif choice == "2":
        tracker.view_expenses()

    elif choice == "3":
        total = tracker.calculate_total()
        print(f"Total Expenses: ₹{total:,.2f}")

    elif choice == "4":
        tracker.delete_expense()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice! Please try again.")
