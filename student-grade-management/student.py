class Student:

    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = {}

    # Add marks
    def add_marks(self, subject, marks):

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return False

        self.marks[subject] = marks
        print(f"Marks added for {subject}.")

        return True

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks.values())

    # Calculate percentage
    def calculate_percentage(self):

        if not self.marks:
            return 0

        total = self.calculate_total()

        return total / len(self.marks)

    # Calculate grade
    def calculate_grade(self):

        percentage = self.calculate_percentage()

        if percentage >= 90:
            return "A+"

        elif percentage >= 80:
            return "A"

        elif percentage >= 70:
            return "B"

        elif percentage >= 60:
            return "C"

        elif percentage >= 50:
            return "D"

        else:
            return "F"

    # Display report card
    def display_report_card(self):

        print("\n========== REPORT CARD ==========")

        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")

        print("\nSubject-wise Marks:")

        if not self.marks:
            print("No marks added yet.")

        else:

            for subject, marks in self.marks.items():
                print(f"{subject}: {marks}/100")

            print("--------------------------------")

            print(f"Total Marks: {self.calculate_total()}")

            print(
                f"Percentage: {self.calculate_percentage():.2f}%"
            )

            print(f"Grade: {self.calculate_grade()}")

        print("=================================")
