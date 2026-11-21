from student import Student


students = {}


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

    print("Student added successfully!")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\n========== STUDENT LIST ==========")

    for student in students.values():
        print(f"Name: {student.name} | Roll Number: {student.roll_number}")

    print("==================================")


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

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            return

        student.add_marks(subject, marks)

    except ValueError:
        print("Please enter valid numeric marks.")


def view_report_card():
    roll_number = input("Enter student roll number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    students[roll_number].display_report_card()


def search_student():
    roll_number = input("Enter student roll number: ").strip()

    if roll_number in students:
        student = students[roll_number]

        print("\nStudent Found!")
        print(f"Name: {student.name}")
        print(f"Roll Number: {student.roll_number}")
    else:
        print("Student not found.")


def main():
    while True:
        print("\n====== STUDENT GRADE MANAGEMENT ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Add Student Marks")
        print("4. View Report Card")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

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
            print("Exiting Student Grade Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
