# Comparing Two Values

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} and {y} is equal")

# ------------------------------------------------

# Combining the Program Using Functions

def main():
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))
    compare(x, y)      # function calling


def compare(x, y):
    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} and {y} is Idk what it is")


main()  # function calling

# ------------------------------------------------

# Asking a New Question Every Single Time


def main():
    compare()
    compare()
    compare()


def compare():
    x = int(input("Enter the value of x: "))
    y = int(input("Enter the value of y: "))

    if x > y:
        print(f"{x} is greater than {y}")
    elif x < y:
        print(f"{x} is less than {y}")
    else:
        print(f"{x} and {y} is Idk what it is")


main()


# ------------------------------------------------

# Checking If Two Values Are Equal


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if (x > y) or (x < y):
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")


# ------------------------------------------------

# Checking Equality Using !=

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x != y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")


# ------------------------------------------------

# Checking Equality Using ==


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is not equal to {y}")


# ------------------------------------------------

# Using and With Comparison Operators


x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if (x > y) and (x >= y):
    print(f"{x} is more than {y}")
else:
    print(f"{x} is not equal to {y}")


# ------------------------------------------------

# Using the not Operator

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

if not (x > y):
    # x = 2 and y = 1 means the condition is True.
    # Because of not, it becomes False,
    # so the else statement will print.
    print(f"{x} is greater then {y}")
else:
    print(f"{x} is less than {y}")


# ------------------------------------------------

# Grade Checker


grade = int(input("Enter your grade student: "))
print(f"Your grade is {grade}")


# ------------------------------------------------


if grade > 100:
    print("INVALID INPUT")
elif (grade <= 100) and (grade > 90):
    print(f"You got an A+ grade with score {grade}%")
elif (grade <= 90) and (grade > 80):
    print(f"You got an A grade with score {grade}%")
elif (grade <= 80) and (grade > 70):
    print(f"You got an B grade with score {grade}%")
elif (grade <= 70) and (grade > 60):
    print(f"You got an C grade with score {grade}%")
elif (grade <= 60) and (grade > 50):
    print(f"You got an F grade with score {grade}%")
else:
    print("GO BACK TO STUDY YOU BRAT YOU FAILED IN EXAM")


# ------------------------------------------------

# Grade Checker Using Chained Comparisons

if grade > 100:
    print("INVALID INPUT")
elif 90 < grade <= 100:
    print(f"You got an A+ grade with score {grade}%")
elif 80 < grade <= 90:
    print(f"You got an A grade with score {grade}%")
elif 70 < grade <= 80:
    print(f"You got an B grade with score {grade}%")
elif 60 < grade <= 70:
    print(f"You got an C grade with score {grade}%")
elif 50 < grade <= 60:
    print(f"You got an F grade with score {grade}%")
else:
    print("GO BACK TO STUDY YOU BRAT YOU FAILED IN EXAM")


# ------------------------------------------------

# Parity Check


num1 = int(input("Enter the num: "))

if num1 % 2 == 0:
    print(f"{num1} is an even number")
else:
    print(f"{num1} is an odd number")


# ------------------------------------------------

# Converting the Same Code Into a Function


def main():
    num1 = int(input("Enter the num: "))
    check(num1)


def check(n):
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")


main()


# ------------------------------------------------

# Returning a Boolean Value


def main():
    num1 = int(input("Enter the num: "))

    if check(num1):
        print("Even")
    else:
        print("Odd")


def check(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()


# ------------------------------------------------

# Using a Conditional Expression


def main():
    num1 = int(input("Enter the num: "))

    if check(num1):
        print("Even")
    else:
        print("Odd")


def check(n):
    return True if n % 2 == 0 else False


main()


# ------------------------------------------------

# Returning the Condition Directly


def main():
    num1 = int(input("Enter the num: "))

    if check(num1):
        print("Even")
    else:
        print("Odd")


def check(n):
    return n % 2 == 0


main()


# ------------------------------------------------

# Harry Potter Code


name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Harmaini":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "draco":
    print("Slytherin")
else:
    print("WHO?")
    input("Are you searching for your home? ")


# ------------------------------------------------

# Collapsing the Same Code


name = input("What's your name? ")

if (name == "Harry") or (name == "Harmaini") or (name == "Ron"):
    print("Gryffindor")
elif name == "draco":
    print("Slytherin")
else:
    print("WHO?")
    input("Are you searching for your home? ")


# ------------------------------------------------

# Using match

# `match` works exactly like a switch-case statement.


name = input("Enter your name: ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Harmiani":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("WhO?")
        input("You wanna know your house?")


# ------------------------------------------------

# Combining Multiple Cases


name = input("Enter your name: ")

match name:
    case "Harry" | "Ron" | "Harmioni":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("WhO?")
        input("You wanna know your house? ")


# ------------------------------------------------

# Note
#Interesting thing is, in C we have to add a `break` statement, 
# but here we are not adding any `break` statement.

# ------------------------------------------------

# CS50P Lecture https://youtu.be/nLRL_NcnK-4

# ------------------------------------------------
