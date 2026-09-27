# ============================================================
# FUNCTIONS IN PYTHON
# ============================================================

# A function is a reusable block of code that performs a specific task.
# We define a function using the 'def' keyword and call it whenever
# we want to execute its code.

# ============================================================
# EXAMPLE 1: A function that asks for the user's name every time
# ============================================================

# Every time the function is called, it asks for a new name.

# def greeting():
#     name = input("Enter your name: ")
#     print(f"Hello, {name}")

# greeting()
# greeting()
# greeting()


# ============================================================
# EXAMPLE 2: Passing an argument to a function
# ============================================================

# Here, the user enters their name only once.
# The same name is passed to the function each time it is called.

# def hello(user):
#     print(f"Hello, {user}")

# name = input("Enter your name: ")

# hello(name)
# hello(name)
# hello(name)
# hello(name)


# ============================================================
# DEFAULT PARAMETERS
# ============================================================

# A parameter can have a default value.
# If no argument is passed, Python uses the default value.

# def hello(user="World"):
#     print(f"Hello, {user}")

# hello()                     # Uses the default value
# name = input("Enter your name: ")
# hello(name)                 # Uses the user's input


# ============================================================
# VARIABLE SCOPE
# ============================================================

# There are mainly two types of scope:
#
# 1. Global Scope
#    Variables created outside every function.
#
# 2. Local Scope
#    Variables created inside a function.
#    They only exist inside that function.

# name1 = input("Enter your name: ")      # Global variable

# def main():
#     name = input("Enter your name: ")   # Local variable
#     hello(name)

# def hello(user="World"):
#     print(f"Hello, {user}")             # Uses parameter
#     print("Hello,", name1)              # Uses global variable

# main()


# ============================================================
# WHY main()?
# ============================================================

# We usually write a main() function so the program runs
# from top to bottom in a clean and organized way.
#
# Functions must be defined before they are called.
# Variables should also be created before they are used.


# ============================================================
# SIDE EFFECT VS RETURN VALUE
# ============================================================

# A function like print() only displays something on the screen.
# It performs a side effect because it doesn't give a useful value back.

# Example:
#
# def hello():
#     print("Hello")
#
# hello()


# ============================================================
# RETURNING A VALUE
# ============================================================

# A function can return a value using the return keyword.
# The returned value can be stored, printed, or used in calculations.


def main():
    number = int(input("Enter a number: "))
    print(f"The square of {number} is {square(number)}")


def square(n):
    return n * n

    # Other ways to write the same thing:
    # return n ** 2
    # return pow(n, 2)


main()


#https://youtu.be/nLRL_NcnK-4