#                  DICTIONARY
# ----------------------------------------------

student = {
    "Noor": "Banaras",
    "Iqra": "Goa",
    "Iram": "Lucknow",
    "Huzaifa": "Mumbai"
}

# # one way to print the code is as
# print(student["Noor"])
# print(student["Iqra"])
# print(student["Iram"])
# print(student["Huzaifa"])

# # using for loop
# for i in student:
#     print(i)


# now according to teacher
# using for loop
# for student in student:
#     print(student)


# but we want keys will values
# using for loop
for names in student:
    print(names, student[names], sep = " = ")


















# Here, when we print(i), Python prints the current key.
# Dictionaries do not have numeric indexing like lists.
# Instead, they use keys to access values.

# for i in student:
# means "loop through every key in the student dictionary."

# Since the dictionary has 4 keys, the loop runs 4 times.

# During each iteration, i becomes the current key:
# 1st iteration -> i = "Noor"
# 2nd iteration -> i = "Iqra"
# 3rd iteration -> i = "Iram"
# 4th iteration -> i = "Huzaifa"

# So, print(i) prints:
# Noor
# Iqra
# Iram
# Huzaifa

# If we write print(student), Python prints the entire dictionary
# on every iteration because 'student' is the dictionary itself.

# Remember:
# Lists use indexes (0, 1, 2, ...)
# Dictionaries use keys ("Noor", "Iqra", ...)

# for student in student:
#     print(student)

# Here, 'student' is the dictionary at first.

# During each iteration, Python stores the current key
# in the variable 'student'.

# 1st iteration:
# student = "Noor"

# 2nd iteration:
# student = "Iqra"

# 3rd iteration:
# student = "Iram"

# 4th iteration:
# student = "Huzaifa"

# After the loop ends, 'student' is no longer the dictionary.
# It now stores the last key ("Huzaifa").

# That's why we should always use a different variable name
# for the loop, such as:
# for key in student:
# or
# for name in student: