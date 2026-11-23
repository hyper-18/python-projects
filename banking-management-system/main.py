from account import Account
accounts = {}


def create_account():
    account_holder = input("Enter account holder name:").strip()
    account_number = input("Enter account number:").strip()
    initial_balance = float(input("Enter initial balance:"))

    if account_number in accounts:
        print("Account number already exists!")
        return
    if initial_balance < 0:
        print("Initial balance cannot be negative!")
        return
    account = Account(account_holder, account_number, initial_balance)
    accounts[account_number] = account
    print("Account created sucessfully!")


def view_accounts():
    if not accounts:
        print("No accounts found!")
        return
    print("\n===== REGISTERED ACCOUNT =====")
    for account in accounts.values():
        print(f"Account Holder:{account.account_holder}")
        print(f"Account Number:{account.account_number}")
        print(f"Balance:${account.balance}")
        print("----------------------------------------")
    print("=========================================")


def search_account():

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:

        account = accounts[account_number]

        print("\nAccount Found!")
        print(f"Account Holder: {account.account_holder}")
        print(f"Account Number: {account.account_number}")
        print(f"Balance: ₹{account.balance}")

    else:

        print("Account not found!")


def deposit_money():

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:

        account = accounts[account_number]

        amount = float(input("Enter deposit amount: "))

        account.deposit(amount)

    else:

        print("Account not found!")


def withdraw_money():

    account_number = input("Enter account number: ").strip()

    if account_number in accounts:

        account = accounts[account_number]

        amount = float(input("Enter withdrawal amount: "))

        account.withdraw(amount)

    else:

        print("Account not found!")


def transfer_money():

    sender_number = input("Enter sender account number: ").strip()

    receiver_number = input("Enter receiver account number: ").strip()

    if sender_number in accounts and receiver_number in accounts:

        sender = accounts[sender_number]
        receiver = accounts[receiver_number]

        amount = float(input("Enter transfer amount: "))

        sender.transfer(receiver, amount)

    else:

        print("One or both accounts not found!")


def main():

    while True:

        print("\n========== BANKING MANAGEMENT SYSTEM ==========")

        print("1. Create Account")
        print("2. View All Accounts")
        print("3. Search Account")
        print("4. Deposit Money")
        print("5. Withdraw Money")
        print("6. Transfer Money")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

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
            print("Thank you for using our banking system!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
