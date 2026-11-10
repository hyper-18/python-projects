from expense import Expense
from tracker import ExpenseTracker
tracker = ExpenseTracker()
while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Calculate Total")
    print("4. Exit")
    choice = input("Enter your choice:")
    if choice == "1":

        try:
            amount = float(input("Entyer amount:"))
            if amount <= 0:
                print("Invalid amount")
                continue
        except ValueError:
            print("Invalid amount")
            continue
        category = input("Enter category: ").strip()
        if not category:
            print("Category cannot be empty")
            continue
        description = input("Enter description: ").strip()
        if not description:
            print("description cannot be empty")
            continue

        expense = Expense(amount, category, description)
        tracker.add_expense(expense)
    elif choice == "2":
        tracker.view_expenses()
    elif choice == "3":
        print(f"Total Expenses: ₹{tracker.calculate_total():,.2f}")
    elif choice == "4":
        print("Thnx for using...")
        break
    else:
        print("Invalid actions")
