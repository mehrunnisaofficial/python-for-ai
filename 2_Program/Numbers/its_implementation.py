import numbers
while True:
    try:
        num = int(input("Enter the number: "))

        if num <= 0:
            print("Re-Enter")
            continue

        break

    except ValueError:
        print("It's not a number duffer")


even_odd = numbers.is_even(num)
print(f"{num} is {even_odd}")

poc = numbers.is_prime(num)
print(f"{num} is {poc}")

square = numbers.square(num)
print(f"The square of {num} is {square}")

cube = numbers.cube(num)
print(f"The square of {num} is {cube}")