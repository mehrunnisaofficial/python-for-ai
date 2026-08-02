# Personal Profile

print("Hello, let's build your personal profile")

name = input("Enter your name: ").title()
parts = name.split()

age = int(input("Enter your age: "))
city = input("Enter your favourite city: ")
lang = input("Enter your favourite programming language: ")
career = input("Enter your dream career: ")
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))

print("--- YOUR PUBLIC PROFILE ---")

print("Name     :", *parts)
print(f"Age      : {age} years")
print(f"City     : {city}")
print(f"Language : {lang}")
print(f"Career   : {career}")
print(f"Height   : {height} cm")
print(f"Weight   : {weight} kg")

print("\n")

print(f"Your name has {len(''.join(parts))} characters")
print(f"Your name has {len(name.replace(" ",""))} characters")


print("\n")

print(f"Your first name : {parts[0]}")
print(f"Your last name  : {parts[-1]}")

print("\n")

print("Thank you for using the program!")