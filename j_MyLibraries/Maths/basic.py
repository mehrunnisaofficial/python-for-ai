# BASIC MODULE FUNCTIONS


def add(a, b):
    return a + b


def diff(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def floor_div(a, b):
    return a // b


def remainder(a, b):
    return a % b


def is_even(a):
    if a % 2 == 0:
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


def power(a, b):
    return a ** b