# using sys.argv[1:] 

import sys

def main():
    students_database = {}

    for i in range(len(sys.argv[1:])):
        student = get_student_data(sys.argv[i+1])
        students_database[i] = student 

    for i in students_database:
        student = students_database[i]

        print("=============================")
        print(f"    STUDENT DATA - {i+1}    ")
        print("-----------------------------")
        print(f"Name  : {student['tname']}")
        print(f"Age   : {student['tage']}")
        print(f"Marks : {student['tmarks']}")
        print("=============================\n")


def get_student_data(student_name):

    name = student_name.strip().capitalize()
    age = int(input(f"Enter {name}'s age: "))
    marks = int(input(f"Enter {name}'s total marks obtained in last sem: "))

    return {
        "tname" : name,
        "tage": age,
        "tmarks" : marks
    }

main()




# What I want:
# I want user give just name
# than it will store in student name
# like a dictionary
# {
#     {
#         student_name :"Mehru"
#         age = 23
#         marks = 25
#     },
#     {
#         student_name = "Hz"
#         age = 23
#         marks = 25
#     },
#     {
#         student_name = "merhu"
#         age = 23
#         marks = 25
#     },
#     {
#         student_name = "Mehrunnisa"
#         age = 23
#         marks = 25
#     }
# }

# def main():
#     n = 1
#     student_name = sys.argv[n]
#     name, age, marks = {get_students(student_name)}

#     database = {}

#     for _ in range(5):
        
#         print(f"============================\n")
#         print(f"        STUDENT DATA        \n")
#         print(f"----------------------------\n")
#         print(f"Name  : {name}")
#         print(f"Age   : {age}")
        
#         print(f"Marks : {marks}")
#         print(f"============================\n")


# def get_students(student_name):
#     name = student_name.strip().capitalize()
#     print(f"Are you sure your name is: {name}")
#     age = int(input("Enter your age: "))
#     total_marks = int(input("Enter your marks: "))
#     return name, age, total_marks

# def get_database(name, age, marks)