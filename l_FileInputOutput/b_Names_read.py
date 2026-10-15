# Now I wanna see what data we stored in b_Names.txt

"""
for i in range(size):
    student = input("Enter user name: ").strip().capitalize()

    with open("b_Names.txt", "a") as file:
        file.write(f"{student}\n")
"""




# Multiple ways to read from a file 
# - using readlines
# - using read
# - using readline
# - using for loop          ( detail in notes )

# MEthod 1

print("\tMETHOD 1\n")

with open ("b_Names.txt") as file:
    content = file.read()

print(content)

# names.txt  ──read()──►  "Harry\nHermione\nRon\n"     (ONE big string)

print("--------------------------------------")

# Method 2
print("\tMETHOD 2\n")
with open ("b_Names.txt") as file:
    content1 = file.readline()
    content2 = file.readline()

print(content1)
print(content2)

# 'Harry\n'
# 'Hermione\n'

print("--------------------------------------")

# MEthod 3
print("\tMETHOD 3\n")
with open ("b_Names.txt") as file:
    Merifile = file.readlines()
print(content1)               # gives a list

# thats why we use for loop to print each name
for lines in Merifile:
    print(lines)
# gives a list with \n character in each name



# But the things is we had \n while storing names of the human and than 
# print by default gave extra lines
# so in total 2 lines

print("--------------------------------------")
print("\tMETHOD 3.1 Formatting\n")
# we can use format method end = ""
for lines in Merifile:
    print(lines, end = "")


print("--------------------------------------")

# # But there is another mehtod that is using rstrip() 
# # which means it remove unwanted stuff from the right side of the string.
print("\tMETHOD 3.2 Formatting\n")
for lines in Merifile:
    print(lines.rstrip())

print("--------------------------------------")



# But I want my name to be sorted manner
# Lets go little back
# but this is not actually sorting txt file rather it is showing us what names we saved
# in sorted manner

names = []
print("\tMETHOD 3.4 Formatting\n")
with open("b_Names.txt") as file:          # opening a file default mode is read
    for line in file:
        names.append(line)               # and here we are appending in a list on in Names.txt file


# Now using sorted method
# By default it is sorting A -> Z
for name in sorted(names):
    print(name.rstrip())

print("--------------------------------------")


# For doing Z -> A
print("\tMETHOD 3.5 Sorting\n")
for name in sorted(names ,reverse = True):
    print(name.rstrip())


print("--------------------------------------")

# How to find specific name in a file
print("\tFinding a specific name in the file\n")
with open("b_Names.txt", "r") as file:   # Open Names.txt in read ("r") mode and store the file object in file
    for line in file:                  # Loop through the file one line at a time
        if(line != "Pure"):
            print("Not found the name")
            break
        print("found")



print("--------------------------------------")
        

# more pythonic way to do the same stuff is 
print("\tMETHOD 4\n")
with open("b_Names.txt", "r") as file:   # Open Names.txt in read ("r") mode and store the file object in file
    for line in file:                  # Loop through the file one line at a time
        print(line.rstrip())           # Remove the newline/extra whitespace from the end and print the line


print("--------------------------------------")


print("\tAnother Method\n")

with open("b_Names.txt") as Names_File:
    for line in sorted(Names_File):                # file itself is sorted without using any list and another loop
        print(line.rstrip())



# Documentation - You can read more about sorted and open here
# https://docs.python.org/3/builtins/functions.html#sorted
# https://docs.python.org/3/builtins/functions.html#open