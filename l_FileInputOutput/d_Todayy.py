import csv

# name = input("Enter your name: ")
# home = input("Enter your address: ")

# with open("d_Today.csv", "a") as Student_data:
#     writer = csv.writer(Student_data)
#     writer.writerow([name, home])


# using dictwriter

import csv

name = input("Enter your name: ")
home = input("Enter your address: ")

with open("d_Today.csv", "a") as Student_data:
    writer = csv.DictWriter(Student_data, fieldnames=["name", "address"])           # here it means give the column name where u wanna store data in your actual .csv file
    writer.writerow({"name" : name, "address" : home})
