# Calculate Statistics
# find out mean median mode and multimode of each students
# will make list of list

import statistics

def main():
    total_students = total_num_students()
    students = get_students(total_students)

    total_subjects = total_num_subjects()
    subjects = get_subjects(total_subjects)

    complete_database = []

    # Get marks and statistics for each student
    for student in students:

        print(f"\n--- Enter marks for {student} ---")

        subjects_marks = get_subjects_marks(subjects)

        stats = get_statistics(subjects_marks)

        # Combine marks and statistics for this student
        student_data = [subjects_marks, stats]

        complete_database.append(student_data)

    # Combine student names with their data
    for human, data in zip(students, complete_database):

        print(f"\n{human}:")

        print("   Marks:")
        for subject, marks in data[0].items():
            print(f"      {subject}: {marks}")

        print("   Statistics:")
        for statistic, value in data[1].items():
            print(f"      {statistic}: {value}")


def total_num_students():
    while True:
        try:
            num = int(input("Enter total number of students: "))

            if 1 <= num <= 50:
                return num

            print("Invalid Quantity")

        except ValueError:
            print("Please Enter a number")


def get_students(number):
    students = []

    for i in range(number):
        while True:
            name = input(f"Enter Student {i + 1} Name: ").strip().title()
            if name.replace(" ", "").isalpha():
                students.append(name)
                break

            print("Please enter correct name")

    return students


def total_num_subjects():
    while True:
        try:
            num = int(input("Enter total number of subjects: "))

            if 1 <= num <= 10:
                return num

            print("Invalid Quantity")

        except ValueError:
            print("Please Enter a number")


def get_subjects(number):
    subjects = []

    for i in range(number):
        while True:
            name = input(f"Enter Subject {i + 1} Name: ").strip().title()

            if name.replace(" ", "").isalpha():
                subjects.append(name)
                break

            print("Please enter correct name")

    return subjects

    
def get_subjects_marks(subjects):
    # is a list

    marks_database = {}

    for sub in subjects:
        while True:
            try:
                marks = int(input(f"Enter Marks of {sub}: "))
            
                if 1 <= marks <= 100:
                    marks_database[sub] = marks
                    break
                
                print("Invalid Marks!!!\nRE-ENTER")

            except ValueError:
                print("Please Enter a number")

    return marks_database        


def get_statistics(marks_database):

    mark_values = list(marks_database.values())

    mean = statistics.mean(mark_values)
    median = statistics.median(mark_values)
    mode = statistics.mode(mark_values)
    multimode = statistics.multimode(mark_values)

    stats = {
        "Mean" : mean,
        "Median" : median,
        "Mode" : mode,
        "Multimode" : multimode
    }

    return stats
        

main()

"""

stuedent name = [student 1, student 2...]

using zip

students_database = [{subject marks}, {subject stats}]
stduents = 
[
student 1 -> [{subject 1 = 100, subject 2 = 99}, {mode = 23, mean, 34, median, 45}]
student 2 -> [{subject 1 = 100, subject 2 = 99}, {mode = 23, mean, 34, median, 45}]
student 3 -> [{subject 1 = 100, subject 2 = 99}, {mode = 23, mean, 34, median, 45}]
]


students
│
├── "student 1"
│   ├── [0] → {"subject 1": 100, "subject 2": 99}
│   └── [1] → {"mode": 23, "mean": 34, "median": 45}
│
├── "student 2"
│   ├── [0] → {"subject 1": 100, "subject 2": 99}
│   └── [1] → {"mode": 23, "mean": 34, "median": 45}
│
├── "student 3"
│   ├── [0] → {"subject 1": 100, "subject 2": 99}
│   └── [1] → {"mode": 23, "mean": 34, "median": 45}

and so on...
"""