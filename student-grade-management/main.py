import json
from student import Student


students = {}


# =====================================
# SAVE STUDENT RECORDS
# =====================================

def save_students():

    data = {}

    for roll_number, student in students.items():

        data[roll_number] = {
            "name": student.name,
            "roll_number": student.roll_number,
            "marks": student.marks
        }

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Student records saved successfully.")


# =====================================
# LOAD STUDENT RECORDS
# =====================================

def load_students():

    global students

    try:

        with open("students.json", "r") as file:

            data = json.load(file)

            for roll_number, details in data.items():

                student = Student(
                    details["name"],
                    details["roll_number"]
                )

                student.marks = details["marks"]

                students[roll_number] = student

        print("Student records loaded successfully.")

    except FileNotFoundError:

        print("No existing student records found.")

    except (json.JSONDecodeError, KeyError, TypeError):

        print("Error: Student data is corrupted or invalid.")


# =====================================
# ADD STUDENT
# =====================================

def add_student():

    name = input("Enter student name: ").strip()

    roll_number = input("Enter roll number: ").strip()

    if not name or not roll_number:

        print("Name and roll number cannot be empty.")
        return

    if roll_number in students:

        print("A student with this roll number already exists.")
        return

    students[roll_number] = Student(name, roll_number)

    save_students()

    print("Student added successfully!")


# =====================================
# VIEW ALL STUDENTS
# =====================================

def view_students():

    if not students:

        print("No student records found.")
        return

    print("\n========== STUDENT LIST ==========")

    for student in students.values():

        print(
            f"Name: {student.name} | "
            f"Roll Number: {student.roll_number}"
        )

    print("==================================")


# =====================================
# ADD STUDENT MARKS
# =====================================

def add_student_marks():

    roll_number = input("Enter student roll number: ").strip()

    if roll_number not in students:

        print("Student not found.")
        return

    student = students[roll_number]

    subject = input("Enter subject name: ").strip()

    if not subject:

        print("Subject name cannot be empty.")
        return

    try:

        marks = float(input("Enter marks (0-100): "))

        if student.add_marks(subject, marks):

            save_students()

    except ValueError:

        print("Please enter valid numeric marks.")


# =====================================
# VIEW REPORT CARD
# =====================================

def view_report_card():

    roll_number = input("Enter student roll number: ").strip()

    if roll_number not in students:

        print("Student not found.")
        return

    students[roll_number].display_report_card()


# =====================================
# SEARCH STUDENT
# =====================================

def search_student():

    roll_number = input("Enter student roll number: ").strip()

    if roll_number in students:

        student = students[roll_number]

        print("\nStudent Found!")

        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")

    else:

        print("Student not found.")


# =====================================
# UPDATE STUDENT DETAILS
# =====================================

def update_student():

    roll_number = input("Enter current roll number: ").strip()

    if roll_number not in students:

        print("Student not found.")
        return

    student = students[roll_number]

    print("\n1. Update Name")
    print("2. Update Roll Number")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if not new_name:

            print("Name cannot be empty.")
            return

        student.name = new_name

        save_students()

        print("Student name updated successfully.")

    elif choice == "2":

        new_roll = input("Enter new roll number: ").strip()

        if not new_roll:

            print("Roll number cannot be empty.")
            return

        if new_roll in students:

            print("This roll number is already being used.")
            return

        student.roll_number = new_roll

        del students[roll_number]

        students[new_roll] = student

        save_students()

        print("Roll number updated successfully.")

    else:

        print("Invalid choice.")


# =====================================
# UPDATE STUDENT MARKS
# =====================================

def update_marks():

    roll_number = input("Enter student roll number: ").strip()

    if roll_number not in students:

        print("Student not found.")
        return

    student = students[roll_number]

    if not student.marks:

        print("No marks available to update.")
        return

    print("\nAvailable Subjects:")

    for subject in student.marks:

        print(f"- {subject}")

    subject = input("\nEnter subject name: ").strip()

    if subject not in student.marks:

        print("Subject not found.")
        return

    try:

        new_marks = float(input("Enter updated marks: "))

        if student.add_marks(subject, new_marks):

            save_students()

            print("Marks updated successfully.")

    except ValueError:

        print("Please enter valid numeric marks.")


# =====================================
# DELETE STUDENT
# =====================================

def delete_student():

    roll_number = input("Enter student roll number: ").strip()

    if roll_number not in students:

        print("Student not found.")
        return

    confirmation = input(
        "Are you sure you want to delete this student? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":

        del students[roll_number]

        save_students()

        print("Student deleted successfully.")

    else:

        print("Deletion cancelled.")


# =====================================
# SORT STUDENTS
# =====================================

def sort_students():

    if not students:

        print("No student records found.")
        return

    print("\n1. Sort by Name")
    print("2. Sort by Percentage")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        sorted_students = sorted(
            students.values(),
            key=lambda student: student.name.lower()
        )

    elif choice == "2":

        sorted_students = sorted(
            students.values(),
            key=lambda student: student.calculate_percentage(),
            reverse=True
        )

    else:

        print("Invalid choice.")
        return

    print("\n========== SORTED STUDENTS ==========")

    for student in sorted_students:

        print(
            f"Name: {student.name} | "
            f"Roll Number: {student.roll_number} | "
            f"Percentage: {student.calculate_percentage():.2f}%"
        )

    print("=====================================")


# =====================================
# CLASS PERFORMANCE
# =====================================

def class_performance():

    if not students:

        print("No student records found.")
        return

    students_with_marks = [
        student for student in students.values()
        if student.marks
    ]

    if not students_with_marks:

        print("No marks have been entered yet.")
        return

    percentages = [
        student.calculate_percentage()
        for student in students_with_marks
    ]

    class_average = sum(percentages) / len(percentages)

    highest_scorer = max(
        students_with_marks,
        key=lambda student: student.calculate_percentage()
    )

    print("\n========== CLASS PERFORMANCE ==========")

    print(f"Total Students: {len(students)}")

    print(f"Students with Marks: {len(students_with_marks)}")

    print(f"Class Average: {class_average:.2f}%")

    print(
        f"Highest Scorer: {highest_scorer.name}"
    )

    print(
        f"Highest Percentage: "
        f"{highest_scorer.calculate_percentage():.2f}%"
    )

    print("========================================")


# =====================================
# MAIN MENU
# =====================================

def main():

    load_students()

    while True:

        print("\n====== STUDENT GRADE MANAGEMENT ======")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Add Student Marks")
        print("4. View Report Card")
        print("5. Search Student")
        print("6. Update Student Details")
        print("7. Update Student Marks")
        print("8. Delete Student")
        print("9. Sort Students")
        print("10. Class Performance")
        print("11. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            add_student_marks()

        elif choice == "4":

            view_report_card()

        elif choice == "5":

            search_student()

        elif choice == "6":

            update_student()

        elif choice == "7":

            update_marks()

        elif choice == "8":

            delete_student()

        elif choice == "9":

            sort_students()

        elif choice == "10":

            class_performance()

        elif choice == "11":

            print("Exiting Student Grade Management System.")

            break

        else:

            print("Invalid choice. Please try again.")


# =====================================
# PROGRAM ENTRY POINT
# =====================================

if __name__ == "__main__":

    main()
