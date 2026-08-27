# Pick a Student
# Teacher randomly chooses a student to give a speech

from random import choice


def main():
    print("---- SPEECH DAY ----\n")

    student_number = get_student_number()
    students = get_students(student_number)

    speaker = choice(students)

    print("\nSo, which student is going to give a speech today?")
    print(f"Today, {speaker} gives the speech! ")


def get_student_number():
    while True:
        try:
            student_number = int(input("Enter the number of students: "))

            if 5 <= student_number <= 50:
                return student_number

            print("Please enter a number between 5 and 50.")

        except ValueError:
            print("Can you PLEASE enter a number? you dummmmmbbb😭")


def get_students(student_number):
    students = []

    for i in range(student_number):
        while True:
            name = input(f"Enter the name of Student {i + 1}: ").strip().title()

            if name:
                students.append(name)
                break

            print("Please enter a name.")

    return students



main()