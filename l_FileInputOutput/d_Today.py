import csv

students = []

with open("d_Today.csv") as student_file:
    reader = csv.DictReader(student_file)            # iterate over the file top to botton and loading each line of the file not as a list but as a dictionary

    for row in reader:
        students.append(row)

for showing in sorted(students, key = lambda student : student["name"]):
    print(f"{showing["name"]} lives in {showing["address"]}")