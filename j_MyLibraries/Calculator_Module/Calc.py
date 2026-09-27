# Calculator Module

def main():
    a = 10
    b = 20
    result = sum(a,b)
    print(result)

def sum(a, b):
    return a + b

def diff(a , b):
    return a - b

def multiply(a , b):
    return a * b

def divide(a , b):
    return a / b

def float_div(a , b):
    return a // b

def remainder(a, b):
    return a % b

if __name__ == "__main__":
    main()


#In Python, the / operator always returns a float, even when the answer is a whole number.