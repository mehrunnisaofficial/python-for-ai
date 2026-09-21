# factorial



def factorial(a):
    fact = 1
    for i in range(1, a+1):
        fact = fact * i

    return fact

def gcd(a , b):
    gcd = [1]

    for i in range(1, min(a, b)+1):
        if (((a % i) == 0) and ((b % i) == 0)):
            gcd.append(i)

    return max(gcd)

def lcm(a, b):
    for i in range(1, (a * b) + 1):
        if i % a == 0 and i % b == 0:
            return i

def fibonacci(a):   
    fib = [0, 1]                   
    for i in range(1, a + 1):     
        fibbon = fib[-2] + fib[-1]     
        fib.append(fibbon)

    return fib[a]

def is_palindrome(text):
    for i in range(1, len(text) // 2 + 1):
        if text[i-1] != text[-i]:
            return False

    return True
