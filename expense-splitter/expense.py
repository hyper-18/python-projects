class Expense:

    def __init__(self, description, amount, paid_by, participants):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants

    def display_expense(self):

        print("\n----------------------------")
        print("Description:", self.description)
        print(f"Amount: ₹{self.amount:.2f}")
        print("Paid By:", self.paid_by)
        print("Participants:", ", ".join(self.participants))
        print("----------------------------")
