from bank import Bank
from account import Account


bank = Bank()


# =====================================
# CREATE ACCOUNT
# =====================================

def create_account():

    account_holder = input("Enter account holder name: ").strip()

    account_number = input("Enter account number: ").strip()

    if not account_holder or not account_number:

        print("Name and account number cannot be empty!")
        return

    if account_number in bank.accounts:

        print("Account number already exists!")
        return

    try:

        initial_balance = float(input("Enter initial balance: "))

        if initial_balance < 0:

            print("Initial balance cannot be negative!")
            return

        if not initial_balance < float("inf"):

            print("Invalid balance!")
            return

        account = Account(
            account_holder,
            account_number,
            initial_balance
        )

        bank.accounts[account_number] = account

        bank.save_accounts()

        print("Account created successfully!")

    except ValueError:

        print("Please enter a valid amount!")


# =====================================
# VIEW ALL ACCOUNTS
# =====================================

def view_accounts():

    if not bank.accounts:

        print("No accounts found!")
        return

    print("\n========== REGISTERED ACCOUNTS ==========")

    for account in bank.accounts.values():

        print(f"Account Holder: {account.account_holder}")
        print(f"Account Number: {account.account_number}")
        print(f"Balance: ₹{account.balance:.2f}")

        print("-----------------------------------------")

    print("=========================================")


# =====================================
# SEARCH ACCOUNT
# =====================================

def search_account():

    account_number = input("Enter account number: ").strip()

    if account_number in bank.accounts:

        account = bank.accounts[account_number]

        print("\nAccount Found!")

        account.check_balance()

    else:

        print("Account not found!")


# =====================================
# DEPOSIT MONEY
# =====================================

def deposit_money():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    try:

        amount = float(input("Enter deposit amount: "))

        account = bank.accounts[account_number]

        if account.deposit(amount):

            bank.save_accounts()

    except ValueError:

        print("Please enter a valid amount!")


# =====================================
# WITHDRAW MONEY
# =====================================

def withdraw_money():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    try:

        amount = float(input("Enter withdrawal amount: "))

        account = bank.accounts[account_number]

        if account.withdraw(amount):

            bank.save_accounts()

    except ValueError:

        print("Please enter a valid amount!")


# =====================================
# TRANSFER MONEY
# =====================================

def transfer_money():

    sender_number = input("Enter sender account number: ").strip()

    receiver_number = input("Enter receiver account number: ").strip()

    if sender_number not in bank.accounts:

        print("Sender account not found!")
        return

    if receiver_number not in bank.accounts:

        print("Receiver account not found!")
        return

    if sender_number == receiver_number:

        print("Cannot transfer money to the same account!")
        return

    try:

        amount = float(input("Enter transfer amount: "))

        sender = bank.accounts[sender_number]

        receiver = bank.accounts[receiver_number]

        if sender.transfer(receiver, amount):

            bank.save_accounts()

    except ValueError:

        print("Please enter a valid amount!")


# =====================================
# TRANSACTION HISTORY
# =====================================

def transaction_history():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    account = bank.accounts[account_number]

    account.display_transactions()


# =====================================
# ACCOUNT STATEMENT
# =====================================

def account_statement():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    account = bank.accounts[account_number]

    print("\n========== ACCOUNT STATEMENT ==========")

    print(f"Account Holder: {account.account_holder}")
    print(f"Account Number: {account.account_number}")

    print(f"Current Balance: ₹{account.balance:.2f}")

    print(f"Total Transactions: {len(account.transactions)}")

    print("\nTransaction Details:")

    account.display_transactions()

    print("=======================================")


# =====================================
# UPDATE ACCOUNT
# =====================================

def update_account():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    account = bank.accounts[account_number]

    new_name = input("Enter new account holder name: ").strip()

    if not new_name:

        print("Name cannot be empty!")
        return

    account.account_holder = new_name

    bank.save_accounts()

    print("Account details updated successfully!")


# =====================================
# DELETE ACCOUNT
# =====================================

def delete_account():

    account_number = input("Enter account number: ").strip()

    if account_number not in bank.accounts:

        print("Account not found!")
        return

    confirmation = input(
        "Are you sure you want to delete this account? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        del bank.accounts[account_number]

        bank.save_accounts()

        print("Account deleted successfully!")

    else:

        print("Account deletion cancelled.")


# =====================================
# MAIN MENU
# =====================================

def main():

    bank.load_accounts()

    while True:

        print("\n========== BANKING MANAGEMENT SYSTEM ==========")

        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Transaction History")
        print("8. Account Statement")
        print("9. Update Account Details")
        print("10. Delete Account")
        print("11. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            create_account()

        elif choice == "2":

            view_accounts()

        elif choice == "3":

            search_account()

        elif choice == "4":

            deposit_money()

        elif choice == "5":

            withdraw_money()

        elif choice == "6":

            transfer_money()

        elif choice == "7":

            transaction_history()

        elif choice == "8":

            account_statement()

        elif choice == "9":

            update_account()

        elif choice == "10":

            delete_account()

        elif choice == "11":

            print("Thank you for using our banking system!")
            break

        else:

            print("Invalid choice! Please try again.")


# =====================================
# PROGRAM ENTRY POINT
# =====================================

if __name__ == "__main__":

    main()
