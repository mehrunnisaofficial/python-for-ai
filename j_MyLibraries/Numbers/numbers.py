"""
4. Number Utility Module
Create number_utils.py.
Functions:
is_even(number)
is_prime(number)
square(number)
cube(number)

"""

def is_even(a):
    if (a % 2) == 0:
        return "Even"
    else:
        return "Odd"

def is_prime(a):
    if a <= 1:
        return "Neither Prime nor Composite"
    
    for i in range(2, a):
        if a % i == 0:
            return "Composite Number"
    return "Prime Number"

def square(a):
    return a ** 2

def cube(a):
    return a ** 3
            

