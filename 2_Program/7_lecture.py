# Exception Handling

# Syntax Error
# Example:
# print("Hello World!)


# ValueError
# A ValueError happens when the input cannot be converted
# to the expected data type.
# try-except
# Used to handle a ValueError.

try:
    number = int(input("Please enter your number: "))
    print(f"Number is {number}")

except ValueError:
    print("You entered an invalid number. Please try again.")


# Using a for loop
# I used a for loop to give the user 5 attempts.

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
    print(
        "You reached the time limit.\n"
        "Try again later.\n"
        "You dumbhead! Go study maths."
    )


# A more Pythonic way

time_limit = 5

for attempt in range(time_limit):
    try:
        number = int(input("Please enter your number: "))
        print(f"Number is {number}")
        break

    except ValueError:
        print("You are r")

else:
    print("You dumb head, you reached the time limit. Go and study numbers, STUPID!")

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

if True:
    x = 10

print(x)  # Output: 10



# NameError

# A NameError can happen after a try-except block.
# It happens when the variable was never assigned.

# Example:

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input")

# print(number)


# If the user enters "hello":
# int("hello") raises a ValueError.
# The assignment to 'number' never happens.
# So, print(number) raises a NameError.


# To solve this issue, we can use else.

try:
    number = int(input("Please enter the number: "))

except ValueError:
    print("Wrong, broo. You are really stupid.")

else:
    # If the except block runs,
    # this block will never execute.
    print(f"Number is {number}")

    # this block will only run when if is correct


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


# try-except with function


# Function without any argument


# Option 1

def main():
    while True:
        try:
            user_input = input("Enter the number: ")
            x = int(user_input)

        except ValueError:
            print(f"{user_input} is not an integer")

        else:
            return x


# Option 2

def main():
    while True:
        try:
            user_input = input("Enter the number: ")
            x = int(user_input)

        except ValueError:
            print(f"{user_input} is not an integer")

        else:
            break

    return x


# I mostly like Option 1 because it looks clean
# and has fewer steps than Option 2.

# Option 1 is more compact.


# Option 3

def main():
    while True:
        try:
            user_input = input("Enter the number: ")
            x = int(user_input)
            return x

        except ValueError:
            print(f"{user_input} is not an integer")


main()


# Remember: try and except are statements.
# People might get confused and think they are functions.
# Even I myself thought they were functions.


# A statement becomes a function when it holds ()
# in its syntax.


def main():
    number = get_num()
    print(f"{number} is an integer")


def get_num():
    while True:
        try:
            user_input = input("Enter the number: ")
            x = int(user_input)
            return x

        except ValueError:
            print(f"{user_input} is not an integer")


main()


# There is another keyword called pass.

# It literally means pass, so it just helps to move on.
# We can use it with except.


def main():
    number = get_num()
    print(f"{number} is an integer")


def get_num():
    while True:
        try:
            user_input = input("Enter the number: ")
            x = int(user_input)
            return x

        except ValueError:
            pass


main()


# Now, every time you write a wrong answer in the input,
# it will pass and then ask again and again.


# What is indentation?

# See, in C++, which I learned earlier,
# to make every block look clear and clean,
# we generally used {}.

# I think that is a clean way to separate
# loops, else, functions, etc.

# But here in Python, there is no such thing.

# That's why I think indentation is needed
# to make things look cleaner.

# Here, indentation now becomes part of the coding syntax.
            


def main():
    number = get_num("Write an integer: ")
    print(f"{number} is an integer")


def get_num(prompt):
    while True:
        try:
            user_input = input(prompt)
            x = int(user_input)
            return x

        except ValueError:
            pass


main()


# We can make it more general and more user- and coder-friendly.


# Now the chapter ends here:
# https://youtu.be/nLRL_NcnK-4?t=17478

# See you next time. Until then, bye-bye and take care!