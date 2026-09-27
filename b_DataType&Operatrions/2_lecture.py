# # ============================================================
# # Lecture 2 - Type Conversion, float(), round() & Formatting
# # ============================================================

# # ============================================================
# # Problem:
# # input() always returns a string.
# #
# # Example:

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

num = num1 + num2

print("RESULT:", num)

# #
# # This happens because Python joins two strings instead of
# # adding two numbers.
# # ============================================================

# # ------------------------------------------------------------
# # Method 1
# # Convert the input into integers immediately.
# # ------------------------------------------------------------

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# result = num1 + num2

# print("The sum of", num1, "and", num2, "is:", result)


# # ------------------------------------------------------------
# # Method 2
# # Store the values as strings first and convert them later.
# # ------------------------------------------------------------

# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")

# result = int(num1) + int(num2)

# print("The sum of", num1, "and", num2, "is:", result)


# # ------------------------------------------------------------
# # Method 3
# # Perform the calculation directly inside print().
# #
# # Advantage:
# # - Short and simple.
# #
# # Disadvantage:
# # - The result is not stored in a variable, so it cannot be
# #   used later in the program.
# # ------------------------------------------------------------

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))

# print("The sum of", num1, "and", num2, "is:", num1 + num2)


# # ------------------------------------------------------------
# # Method 4
# # Everything in a single line.
# #
# # This works, but it is not beginner-friendly and is harder
# # to read.
# # ------------------------------------------------------------

# print(
#     int(input("Enter the first number: "))
#     + int(input("Enter the second number: "))
# )


# # ============================================================
# # Float Data Type
# # ============================================================
# # float is used to store decimal numbers.
# #
# # Examples:
# # 3.14
# # 99.99
# # 15.5
# # ============================================================

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = num1 + num2

# print("The sum of", num1, "and", num2, "is:", result)

# # int() removes everything after the decimal point.
# # It DOES NOT round the number.

# print("Integer value:", int(result))


# # ============================================================
# # round() Function
# # ============================================================
# #
# # round(number)
# # → Rounds to the nearest whole number.
# #
# # round(number, decimal_places)
# # → Keeps the specified number of digits after
# #   the decimal point.
# #
# # Examples:
# #
# # round(4.6)
# # Output: 5
# #
# # round(3.14159, 2)
# # Output: 3.14
# #
# # round(3.14159, 3)
# # Output: 3.142
# # ============================================================

# print(round(result))
# print(round(result, 3))


# # ============================================================
# # Number Formatting using f-strings
# # ============================================================

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = num1 + num2

# # Prints the number normally.
# print(f"{result}")

# # Adds commas for better readability.
# print(f"{result:,}")

# # Shows exactly two decimal places.
# print(f"{result:.2f}")

# # Shows exactly three decimal places.
# print(f"{result:.3f}")


# # ============================================================
# # Division Example
# # ============================================================

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = num1 / num2

# print("Original:", result)

# print("Rounded:", round(result))

# print("Rounded to 2 decimal places:", round(result, 2))

# print("Formatted to 2 decimal places:", f"{result:.2f}")

# # ============================================================
# # Another way to do it
# # ============================================================


# this is just formatting in the string so its not permanent
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = num1 / num2
# print(f"The Result is ( after round off ): {result:.2f}")
# print(f"The Result is ( after round off ): {result}")

# # but this one is permanent

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# result = round(num1 / num2, 2)
# print("The Result is ( after round off ): ", result)


# # ============================================================
# # Important Note
# # ============================================================
# #
# # There is no single "correct" way to solve a problem.
# #
# # Different situations require different approaches.
# #
# # Choose the method that makes your code:
# # • Easy to read
# # • Easy to understand
# # • Easy to maintain
# #
# # As you gain experience, you'll naturally learn which
# # approach is best for a given situation.
# # ============================================================

# # Lecture Reference:
# # https://youtu.be/nLRL_NcnK-4?t=5409








