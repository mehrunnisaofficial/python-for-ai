with open("a_Data.csv") as file:           # By default read mode
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")

print("\n-----------------------------------------\n")

# better way is to unpacking suing split
with open("a_Data.csv") as file:           # By default read mode
    for line in file:
        name, place = line.rstrip().split(",")
        print(f"{name} lives in {place}")


# But now I want in sorted manner lets do the same manner as we done in names.txt

employee = []

with open("a_Data.csv") as file:
    for line in file:
        names, place = line.rstrip().split(",")

        employee.append(f"{names} lives in {place}")


for employee_names in sorted(employee, reverse = True):
    print(employee_names)


print("\n-----------------------------------------\n")

students = []

with open("a_Data.csv") as file:
    for line in file:
        names, place = line.rstrip().split(",")
        student = {"name"  : names,                        # this is global right now not local
                   "place" : place}

        students.append(student)

def get_name(student):
    return student["name"]

def get_place(student):
    return student["place"]

for student in sorted(students, key=get_place):
    print(f"{student["name"]} lives in {student["place"]}")



print("\n-----------------------------------------\n")


# but uk instead of writing the long code like get place and get name block 
# we can simply use lambda fucntion
for student in sorted(students, key = lambda student: student["name"]):
    print(f"{student["name"]} lives in {student["place"]}")


# lambda student: student["name"] this single line is equivalent to get_name(student) function



# students = [
#     {"name": "Harry", "Place": "London"},
#     {"name": "Ron", "Place": "London"},
#     {"name": "Hermione", "Place": "London"}
# ]


students = []

with open("c_ManagingIDK.csv") as file:
    for line in file:
        row = line.strip().split(",")

        students.append({
            "Name": row[0],
            "Full Address": " ".join(row[1:])
        })

for student in sorted(students, key=lambda student: student["Name"]):
    print(f"{student['Name']} lives at {student['Full Address']}")