import random
import time
import msvcrt

from quiz import questions


def timed_input(prompt, timeout):
    print(prompt, end="", flush=True)

    answer = ""
    start_time = time.time()

    while time.time() - start_time < timeout:

        if msvcrt.kbhit():
            char = msvcrt.getwch()

            if char == "\r":
                print()
                return answer.strip().upper()

            elif char == "\b":
                if answer:
                    answer = answer[:-1]
                    print("\b \b", end="", flush=True)

            elif char in ("\x00", "\xe0"):
                msvcrt.getwch()

            else:
                answer += char
                print(char, end="", flush=True)

        time.sleep(0.05)

    print("\nTime's up!")
    return None


while True:

    score = 0

    print("\n===== PYTHON QUIZ APPLICATION =====")

    print("\nSelect Difficulty:")
    print("1. Easy (5 questions)")
    print("2. Medium (10 questions)")
    print("3. Hard (15 questions)")

    difficulty = input("Enter choice: ").strip()

    if difficulty == "1":
        selected_questions = questions[:5]

    elif difficulty == "2":
        selected_questions = questions[:10]

    elif difficulty == "3":
        selected_questions = questions[:15]

    else:
        print("Invalid difficulty! Please try again.")
        continue

    random.shuffle(selected_questions)

    for index, question in enumerate(selected_questions, start=1):

        print(f"\nQuestion {index}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:

            answer = timed_input(
                "Enter your answer (A/B/C/D): ",
                15
            )

            if answer is None:
                print("Question skipped due to timeout!")
                print("Correct answer:", question["answer"])
                break

            if answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C, or D.")

        if answer is None:
            print("No points awarded.")

        elif answer == question["answer"]:
            print("Correct!")
            score += 1

        else:
            print("Incorrect!")
            print("Correct answer:", question["answer"])

    print("\n===== QUIZ RESULTS =====")

    total = len(selected_questions)
    percentage = (score / total) * 100

    print("Total Questions:", total)
    print("Correct Answers:", score)
    print("Wrong Answers:", total - score)
    print(f"Your Score: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent! Perfect score!")

    elif percentage >= 80:
        print("Great job! You performed very well.")

    elif percentage >= 60:
        print("Good effort! Keep practicing.")

    elif percentage >= 40:
        print("You need more practice.")

    else:
        print("Keep learning and try again!")

    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if replay not in ["yes", "y"]:
        print("\nThank you for playing!")
        break
