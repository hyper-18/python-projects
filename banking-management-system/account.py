from datetime import datetime
from uuid import uuid4


class Account:

    def __init__(self, account_holder, account_number, balance=0,
                 transactions=None):

        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    # Generate transaction ID
    def generate_transaction_id(self):
        return uuid4().hex[:10].upper()

    # Record transaction
    def record_transaction(self, transaction_type, amount,
                           description, transaction_id=None,
                           related_account=None):

        if transaction_id is None:
            transaction_id = self.generate_transaction_id()

        transaction = {
            "transaction_id": transaction_id,
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "timestamp": datetime.now().astimezone().isoformat(
                timespec="seconds"
            ),
            "related_account": related_account
        }

        self.transactions.append(transaction)

        return transaction_id

    # Deposit money
    def deposit(self, amount):

        if amount <= 0:
            print("Invalid deposit amount!")
            return False

        self.balance += amount

        self.record_transaction(
            "DEPOSIT",
            amount,
            "Money deposited"
        )

        print("Deposit successful!")
        print(f"Updated balance: ₹{self.balance:.2f}")

        return True

    # Withdraw money
    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount!")
            return False

        if amount > self.balance:
            print("Insufficient balance!")
            return False

        self.balance -= amount

        self.record_transaction(
            "WITHDRAWAL",
            amount,
            "Money withdrawn"
        )

        print("Withdrawal successful!")
        print(f"Updated balance: ₹{self.balance:.2f}")

        return True

    # Transfer money
    def transfer(self, receiver, amount):

        if self is receiver:
            print("Cannot transfer money to the same account!")
            return False

        if amount <= 0:
            print("Invalid transfer amount!")
            return False

        if amount > self.balance:
            print("Insufficient balance!")
            return False

        transaction_id = self.generate_transaction_id()

        self.balance -= amount
        receiver.balance += amount

        self.record_transaction(
            "TRANSFER_OUT",
            amount,
            f"Money transferred to {receiver.account_number}",
            transaction_id,
            receiver.account_number
        )

        receiver.record_transaction(
            "TRANSFER_IN",
            amount,
            f"Money received from {self.account_number}",
            transaction_id,
            self.account_number
        )

        print("Transfer successful!")
        print(f"Your updated balance: ₹{self.balance:.2f}")
        print(f"Receiver's updated balance: ₹{receiver.balance:.2f}")

        return True

    # Check balance
    def check_balance(self):

        print("\n========== ACCOUNT DETAILS ==========")

        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance:.2f}")

        print("=====================================")

    # Display transaction history
    def display_transactions(self):

        if not self.transactions:
            print("No transactions found!")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for transaction in self.transactions:

            print(f"Transaction ID: {transaction['transaction_id']}")
            print(f"Type: {transaction['type']}")
            print(f"Amount: ₹{transaction['amount']:.2f}")
            print(f"Description: {transaction['description']}")
            print(f"Date: {transaction['timestamp']}")

            if transaction.get("related_account"):
                print(
                    f"Related Account: "
                    f"{transaction['related_account']}"
                )

            print("-----------------------------------------")

        print("=========================================")
