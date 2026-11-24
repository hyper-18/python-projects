import json
import os

from account import Account


class Bank:

    def __init__(self):
        self.accounts = {}
        self.filename = "accounts.json"

    # Save accounts
    def save_accounts(self):

        data = {}

        for account_number, account in self.accounts.items():

            data[account_number] = {
                "account_holder": account.account_holder,
                "account_number": account.account_number,
                "balance": account.balance,
                "transactions": account.transactions
            }

        try:

            with open(self.filename, "w") as file:

                json.dump(data, file, indent=4)

            print("Account records saved successfully!")

        except OSError:

            print("Error saving account records!")

    # Load accounts
    def load_accounts(self):

        if not os.path.exists(self.filename):

            print("No saved account records found.")
            return

        try:

            with open(self.filename, "r") as file:

                data = json.load(file)

            if not isinstance(data, dict):
                raise ValueError("Invalid account data format.")

            for account_number, details in data.items():

                if not isinstance(details, dict):
                    raise ValueError("Invalid account record.")

                account = Account(
                    details["account_holder"],
                    details["account_number"],
                    details["balance"],
                    details.get("transactions", [])
                )

                self.accounts[account_number] = account

            print("Account records loaded successfully!")

        except (json.JSONDecodeError, KeyError, TypeError,
                ValueError, OSError):

            print("Error: Account data is corrupted or invalid.")

            self.accounts.clear()
