# =====================================================
#                   WHILE LOOP
# =====================================================

# i = 1
# while i <= 5:
#     print(i)
#     i += 1  # here i = 5


# Cat Program
# while i <= 10:  # This code won't work until we change the value of i
#     print("Meow")
#     i += 1


# Another way to do the same code
# z = 4
# while z >= 1:
#     print("bark")
#     z -= 1


# =====================================================
#              FOR LOOP WITH A LIST
# =====================================================

# for i in [0, 1, 2, 3]:
#     print("Meow")

# The problem is that it works, but what if I have to print
# something a million times?
# Do I need to type all the numbers?
# No! We can use the range() function.

# for i in range(5):  # This will iterate over 0, 1, 2, 3, 4
#     print("Meow")


# Another cool way in Python
# print("Meow\n" * 5, end="")  # Prints Meow 5 times


# =====================================================
#        ASK THE USER FOR A POSITIVE NUMBER
# =====================================================

# i = int(input("Enter a positive number: "))
#
# while i <= 0:
#     if i <= 0:
#         i = int(input("Enter a positive number: "))
#         break
#
# if i > 0:
#     for j in range(i):
#         print("Meow")


# =====================================================
#                 METHOD 1
# =====================================================

# while True:
#     n = int(input("Enter the positive number: "))
#
#     if n < 0:
#         continue
#     else:
#         break
#
# for i in range(n):
#     print("Meow")

# What is happening here?
#
# while True means the loop will run forever until break is reached.
#
# If n < 0:
#     continue skips the remaining statements inside the loop
#     and immediately goes back to the beginning.
#
# If n >= 0:
#     break stops the loop, and the for loop starts.


# =====================================================
#                 METHOD 2
# =====================================================

# while True:
#     num = int(input("Enter the positive number: "))
#
#     if num > 0:
#         break
#
# for i in range(num):
#     print("Meow")

# What is happening here?
#
# while True means the code will keep running forever.
# The loop only stops when break executes.
# break happens only if num > 0.


# =====================================================
#                  USING pass
# =====================================================

"""
while True:
    n = int(input("Enter the positive number: "))

    if n < 0:
        pass
    else:
        break

for i in range(n):
    print("Meow")

Explanation:

n < 0 → True

pass executes.
(It literally does nothing.)

The if block ends.
The while loop reaches its end.

Since the condition is while True,
the loop automatically starts again.

So yes, this program still works! 🎉
"""


# =====================================================
#          MAKING THE SAME PROGRAM USING FUNCTIONS
# =====================================================

# def main():
#     number = get_number()
#     print_Meow(number)
#
#
# def get_number():
#     while True:
#         i = int(input("Enter the number: "))
#
#         if i > 0:
#             return i
#
#
# def print_Meow(n):
#     for i in range(n):
#         print("Meow")
#
#
# main()


# =====================================================
#                  SAME CODE AGAIN
# =====================================================

# def main():
#     number = get_number()
#     print_Meow(number)
#
#
# def get_number():
#     while True:
#         i = int(input("Enter the number: "))
#
#         if i > 0:
#             return i
#
#
# def print_Meow(n):
#     for i in range(n):
#         print("Meow")
#
#
# main()


# =====================================================
#                  HARRY POTTER
# =====================================================

# student = ["Harmioni", "Harry", "Ron"]

# for i in range(3):
#     print(student[i])


# Another Pythonic way

# for stud in student:
#     print(stud)


# =====================================================
#                ANOTHER WAY
# =====================================================

# student = ["Harmioni", "Harry", "Ron"]
#
# for i in range(len(student)):
#     print(i + 1, ":", student[i], end="\n")


# =====================================================
#                  DICTIONARY
# =====================================================

# https://youtu.be/nLRL_NcnK-4?t=12773

i = 10
while(i >= 1):
    print(i)
    i -= 1