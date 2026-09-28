# Now I wanna see what data we stored in Names.txt

"""
for i in range(size):
    student = input("Enter user name: ").strip().capitalize()

    with open("Names.txt", "a") as file:
        file.write(f"{student}\n")
"""

with open("Names.txt", "r") as file:
    line = file.readlines()         # means reading all the lines from a file than store it in a list from in a variable named line

for lines in line:
    print(lines)

# But the things is we had \n while storing names of the human and than 
# print by default gave extra lines
# so in total 2 lines

print("--------------------------------------")

# we can use format method end = ""
for lines in line:
    print(lines, end = "")


print("--------------------------------------")

# But there is another mehtod that is using rstrip() 
# which means it remove unwanted stuff from the right side of the string.
for lines in line:
    print(lines.rstrip())

print("--------------------------------------")

# more pythonic way to do the same stuff is 

with open("Names.txt", "r") as file:   # Open Names.txt in read ("r") mode and store the file object in file
    for line in file:                  # Loop through the file one line at a time
        print(line.rstrip())           # Remove the newline/extra whitespace from the end and print the line


print("--------------------------------------")

# But I want my name to be sorted manner
# Lets go little back
# but this is not actually sorting txt file rather it is showing us what names we saved
# in sorted manner

names = []

with open("Names.txt") as file:          # opening a file default mode is read
    for line in file:
        names.append(line)               # and here we are appending in a list on in Names.txt file


# Now using sorted method
# By default it is sorting A -> Z
for name in sorted(names):
    print(name.rstrip())

print("--------------------------------------")


# For doing Z -> A
for name in sorted(names, key= str.lower ,reverse = True):
    print(name.rstrip())


print("--------------------------------------")

# How to find specific name in a file
with open("Names.txt", "r") as file:   # Open Names.txt in read ("r") mode and store the file object in file
    for line in file:                  # Loop through the file one line at a time
        if(line != "Pure"):
            print("Not found the name")
            break
        print("found")
        





# Documentation - You can read more about sorted and open here
# https://docs.python.org/3/builtins/functions.html#sorted
# https://docs.python.org/3/builtins/functions.html#open