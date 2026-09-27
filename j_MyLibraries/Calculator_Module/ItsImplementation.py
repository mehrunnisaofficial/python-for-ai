import Calc

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

result1 = Calc.sum(num1, num2)
result2 = Calc.float_div(num1, num2)              
result3 = Calc.divide(num1, num2)              # see here it take 2 number divide it and than store in result3 which becomes float
result4 = Calc.remainder(num1, num2)

print(f"{num1} + {num2} = {result1}")
print(f"{num1} // {num2} = {result2}")
print(f"{num1} / {num2} = {result3}")
print(f"{num1} % {num2} = {result4}")


print(type(result1))
print(type(result2))
print(type(result3))
print(type(result4))


