def main():
    student = actual_details()
    print(student)


def actual_details():          # Printing one
    Student_class, Student_section, Roll_choice = get_basic_details()
    iteration = how_many()

    if Roll_choice == 1:
        all_students = []

        for i in range(iteration):
            student_details = {
                "Name": sname(),
                "Class": Student_class,
                "Section": Student_section,
                "Age": sage(),
                "Gender": sgender(),
                "Roll Number": i + 1
            }

            all_students.append(student_details)

        return all_students
    else:
        all_students = []
        for i in range(iteration):
            student_details = {
                "Name" : sname(),
                "Class" : Student_class,
                "Section" : Student_section,
                "Age" : sage(),
                "Gender" : sgender(),
                "Roll Number" : without_roll()
            }
            all_students.append(student_details)
        return all_students

def how_many():                   # how many students data you wanna store
    while True:
        try:
            data = int(input("How many students details data you want to store: "))

            if data <= 0:
                print("Please Enter proper Details")
                continue
            return data
        except ValueError:
            print("Please Enter Valid Number")

def get_basic_details():          # get basic details
    while True:                         # class
        try:
            classs = int(input("Enter which class data you are storing: "))

            if classs < 1 or classs > 12:
                print("Please Re-Enter valid Class")
                continue
            break
        except ValueError:
            print("Please Enter only class number Teacher")

    while True:                         # Section
        section = input("Enter which section detail you are entering: ").strip().title()

        if section  not in {"A", "B", "C", "D", "E"}:
            print("Please Re-Enter Valid Section")
            continue
        break

    print("\nDETAILS REGARDING ROLL NUMBER\n")     # Roll Number

    options = ["Filling details with Roll Number", 
               "Filling details without Roll Number"]

    print("Options are: ")
    for i, option in enumerate(options, start=1):
        print(f"{i}) {option}\n")

    while True:
        try:
            choose = int(input("Choose Options: "))

            if choose == 1 or choose == 2:
                print(f"You choose options {choose}")
                break

            print("Please Enter Valid Choice")

        except ValueError:
            print("Invalid Number")

    return classs, section, choose

def sname():                      # name
    while True:
        print()                    
        name = input("Enter the name of the student: ").strip().capitalize()
        if not name.isalpha():
            print("Please Re-enter the name of the student")
            continue

        return name

def sage():                   # age
    while True:                   
        try:
            age = int(input(f"Enter Age: "))

            if (age < 4) or (age > 40):
                print("Please Enter the valid age")
                continue
            return age
        except ValueError:
            print("Please enter only Numbers")

def sgender():            # gender choose
    print("Choose gender")

    gender = ["Male", "Female", "Other"]

    for i, option in enumerate(gender, start=1):
        print(f"{i}) {option}")

    while True:
        choice = input(f"Enter Gender: ").strip().capitalize()

        if choice not in gender:
            print("Please write the gender from the given option")
            continue

        return choice

def without_roll():               # Without Roll Number
    while True:
        try:
            rno = int(input("Roll Number = "))

            if rno <= 0:
                print("Please Re-Enter")
                continue
            return rno
        except ValueError:
            print("Please Enter The Valid Details")

main()



# def choice_roll():                # Choice for Roll Number
#     print("\nDETAILS REGARDING ROLL NUMBER\n")

#     options = ["Filling details with Roll Number", 
#                "Filling details without Roll Number"]

#     print("Options are: ")
#     for i, option in enumerate(options, start=1):
#         print(f"{i}) {option}\n")

#     while True:
#         try:
#             choose = int(input("Choose Options: "))

#             if choose == 1 or choose == 2:
#                 print(f"You choose options {choose}")
#                 return choose

#             print("Please Enter Valid Choice")

#         except ValueError:
#             print("Invalid Number")