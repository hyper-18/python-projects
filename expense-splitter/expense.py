class Expense:

    def __init__(self, description, amount, paid_by, participants):
        self.description = description
        self.amount = amount
        self.paid_by = paid_by
        self.participants = participants

    def display_expense(self):

        print("\nExpense Details")
        print("--------------------")
        print("Description:", self.description)
        print("Amount: ₹", self.amount)
        print("Paid By:", self.paid_by)
        print("Participants:", ", ".join(self.participants))
        print("--------------------")
