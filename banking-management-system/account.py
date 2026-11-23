class Account:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited sucessfully!")
            print(f"updated balance:${self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal sucessdful!")
            print(f"updated balance:${self.balance}")
        else:
            print("Invalid withdrawal amount!")

    def check_balance(self):
        print("\n===== ACCOUNT DETAILS =====")
        print(f"Account holder:{self.account_holder}")
        print(f"Account number:{self.account_number}")
        print(f"Current balance:{self.balance}")
        print("=============================")

    def transfer(self, receiver, amount):
        if amount > 0 and amount <= self.blance:
            self.balance -= amount
            receiver.balance += amount
            print("Transfer sucessful!")
            print(f"Your updated balance:${self.balance}")
            print(f"Receiver's updated balance:${receiver.balance}")
        else:
            print("inalid transfer amount or insufficient balance!")
