import csv

students = []

with open("c_ManagingIDK.csv") as file:
    reader = csv.reader(file)

    for row in reader:
        students.append(
            {
            "Name": row[0],
            "Full Address": f"{row[1]} {row[2]}"
            }
        )

for student in sorted(students, key = lambda student : student["Name"]):
    print(f"{student['Name']} lives in {student['Full Address']}")