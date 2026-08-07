# Exception Handling

# Syntax Error

# Example:
# print("Hello World!)

# ValueError

# A ValueError happens when the input cannot be converted
# to the expected data type.

# Example:

num = int(input("Enter your number: "))
print(f"Number is {num}")

# If you enter a positive (+ve) integer, it will print.
# If you enter a negative (-ve) integer, it will also print.
# But if you enter something other than an integer, such as:
# - float
# - string
# a ValueError will occur.

# To handle a ValueError, we can use try-except.
# It works somewhat like if-else.

try:
    number = int(input("Please enter your number: "))
    print(f"Number is {number}")
except:
    print("You entered the wrong input. Please try again.")

# Let's try the same thing using a for loop.

time_limit = 5
count = 0

for _ in range(time_limit):
    try:
        number = int(input("Please enter your number: "))
        print(f"Number is {number}")
        break
    except ValueError:
        print("You entered an invalid number. Please try again.")
        count += 1

if count >= 5:
    print("You reached the time limit.\nTry again later.\nYou dumbhead Go study maths.")

# A more Pythonic way

time_limit = 5

for attempt in range(time_limit):
    try:
        number = int(input("Please enter your number: "))
        print(f"Number is {number}")
        break
    except ValueError:
        print("You are r")
# else:
    # print("You dumb head, you reached the time limit. Go and study numbers, STUPID!")

print(f"Number is {number}")

# One cool thing in Python is that we can use else with
# for and while loops. That's pretty amazing!

# Scope in Python

# In Python, try, except, if, else, for, and while
# DO NOT create a new local scope.

# Variables created inside these blocks can still be
# accessed outside the block, as long as they were
# successfully assigned a value.

# Only functions (def), classes (class), and modules (.py files)
# create a new local scope.

# Example:

if True:
    x = 10

print(x)  # Output: 10

# NameError

# Sometimes you may get a NameError after a try-except block.

# This does NOT happen because the variable is out of scope.

# It happens because the variable was NEVER assigned.

# Example:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")

print(number)

# If the user enters "hello":

# 1. int("hello") raises a ValueError.
# 2. Python immediately jumps to the except block.
# 3. The assignment to 'number' never happens.
# 4. Later, print(number) raises:
#    NameError: name 'number' is not defined
# 5. This happens because 'number' was never created,
#    NOT because it is out of scope.


# To solve this issue, we can use else.

try:
    number = int(input("Please enter the number: "))
except ValueError:
    print("Wrong, broo. You are really stupid.")
else:
    # If the except block runs,
    # this block will never execute.
    print(f"Number is {number}")

# Another way

while True:
    try:
        number = int(input("Please enter your number: "))
        print(f"Number is {number}")
        break
    except ValueError:
        print("You entered an invalid number. Please try again.")

# Another way

while True:
    try:
        number = int(input("Please enter your number: "))
    except ValueError:
        print("You entered an invalid number. Please try again.")
    else:
        break

print(f"Number is {number}")

# Another way

while True:
    try:
        number = int(input("Please enter your number: "))
        break
    except ValueError:
        print("You entered an invalid number. Please try again.")

print(f"Number is {number}")

# Another way

while True:
    try:
        number = int(input("Please enter your number: "))
    except ValueError:
        print("You entered an invalid number. Please try again.")
    else:
        print(f"Number is {number}")
        break

# Lecture Reference:
# https://youtu.be/nLRL_NcnK-4?t=16649

# Is not completed yet