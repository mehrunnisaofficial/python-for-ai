# DICTIONARY

student = {
    "Noor": "Banaras",
    "Iqra": "Goa",
    "Iram": "Lucknow",
    "Huzaifa": "Mumbai"
}

# One way to print values

# print(student["Noor"])
# print(student["Iqra"])
# print(student["Iram"])
# print(student["Huzaifa"])


# Using a for loop

# for key in student:
#     print(key)

# A dictionary automatically loops through its keys.

# Output:
# Noor
# Iqra
# Iram
# Huzaifa


# Printing both keys and values

for key in student:
    print(key, student[key], sep=" = ")

# Output:
# Noor = Banaras
# Iqra = Goa
# Iram = Lucknow
# Huzaifa = Mumbai


# How dictionaries work

# Dictionaries do not use numeric indexes like lists.

# List
# fruits = ["Apple", "Banana", "Orange"]
# fruits[0] -> Apple

# Dictionary
# student = {
#     "Noor": "Banaras",
#     "Iqra": "Goa"
# }

# student["Noor"] -> Banaras

# The key is used to access the value.

# for key in student:
#     print(key)

# Python loops through every key in the dictionary.

# Iteration 1
# key = "Noor"

# Iteration 2
# key = "Iqra"

# Iteration 3
# key = "Iram"

# Iteration 4
# key = "Huzaifa"

# Therefore, print(key) prints every key one by one.


# Why "for student in student" is a bad idea

student = {
    "Noor": "Banaras",
    "Iqra": "Goa"
}

# for student in student:
#     print(student)

# This works, but it is confusing.

# Before the loop
# student is the dictionary.

# During the first iteration
# student = "Noor"

# During the second iteration
# student = "Iqra"

# After the loop finishes,
# student is no longer the dictionary.

# It now stores the last key.

# Because of this, always use a different variable name.

# Good examples

# for key in student:
#     print(key)

# for name in student:
#     print(name)


# Dictionary Example

students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# Instead of repeating the same code,
# we can use a loop.

for name in students:
    print(name, ":", students[name])

# Output
# Hermione : Gryffindor
# Harry : Gryffindor
# Ron : Gryffindor
# Draco : Slytherin


# List of Dictionaries

# Sometimes one dictionary is not enough.

# If we have multiple students,
# each student can have multiple pieces of information.

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=" : ")


# Understanding List of Dictionaries

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}
]

# students is a list.

# Index 0
# {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}

# Index 1
# {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}

# During the loop

for student in students:
    print(student["name"])

# First iteration

# student =
# {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"}

# student["name"]
# means:
# Give me the value stored with the key "name".

# Output
# Hermione

# Second iteration

# student =
# {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"}

# student["name"]

# Output
# Harry



# Why students["name"] gives an error

students = [
    {"name": "Hermione"},
    {"name": "Harry"}
]

# This is incorrect.

# students["name"]

# Why?

# Because students is a list.

# Lists only accept integer indexes.

# Correct examples

# students[0]
# Gives the first dictionary.

# students[0]["name"]
# Gives "Hermione"

# When using a loop

for student in students:
    print(student["name"])

# Here, student is a dictionary,
# so student["name"] is perfectly valid.

# Remember

# List
# Uses numeric indexes.
# Example:
# students[0]

# Dictionary
# Uses keys.
# Example:
# student["name"]

# Since students is a list,
# Python expects a number like 0, 1, 2...

# Since student is a dictionary,
# Python expects a key like "name", "house", or "patronus".



# STUDIED TILL
#https://youtu.be/nLRL_NcnK-4?t=13855
