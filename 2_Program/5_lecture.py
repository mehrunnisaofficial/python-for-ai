# # # # WHILE LOOP

# # # i = 1
# # # while i <= 5:
# # #     print(i)
# # #     i += 1  # here i = 5

# # # # cat program
# # # while (i <= 10):  # so this code won't work until we change i value
# # #     print("Meow")
# # #     i += 1


# # # # another way to do the same code is 
# # # z = 4
# # # while z >= 1:
# # #     print("bark")
# # #     z -= 1

# # # # for loop and list
# # # for i in [0,1,2,3]:
# # #     print("Meow")

# # # # the fault is it does print but what if i have to print million times?
# # # # do i need to type all the numbers? no, we can use range function to do that
# # # for i in range(5):  # this will print 0,1,2,3,4
# # #     print("Meow")


# # # # another cool way in python is 
# # # print("Meow\n" * 5, end = "")  # this will print meow 5 times


# # # ask the user from positive number and print meow that many times
# # i = int(input("Enter a positive number: "))
# # while(i <= 0):
# #     if i <= 0:
# #         i = int(input("Enter a positive number: "))
# #             break;

# #if (i > 0):
# #    for j in range(i):
# #          print("Meow")



# # another way to do the same code is
# while True:
#     n = int(input("Enter the positive number: "))
#     if n < 0:
#         continue
#     else:
#         break
# for i in range(n):
#     print("Meow")

# # here what is happening is that the while loop run forever until the code break
# # and code will break when n > 0
# # if n < 0 it will continue 
# # because of continue the rest below statements is gonna left and than it code went back
# # to the starting of while loop block



# # anothe way to do the same code is
# while True:
#     num = int(input("Enter the positive number: "))
#     if num > 0:
#         break

# for i in range(num):
#     print("Meow")

# # here what is happening is while true means the code will run forever until
# # the code break happen
# # and code break will happen when the value of i > 0


# """
# while True:
#     n = int(input("Enter the positive number: "))
#     if n < 0:
#         pass
#     else:
#         break

# for i in range(n):
#     print("Meow")

# n < 0 → True
# pass executes. (It does nothing.)
# The if block ends.
# The while loop reaches its end.
# Since it's while True, it starts again automatically.

# So yes, this program still works! 🎉
# """



# making the same code using function

# def main():
#     number = get_number()
#     print_Meow(number)


# def get_number():
#     while True:
#         i = int(input("Enter the number: "))
#         if i > 0:
#             return i

# def print_Meow(n):
#     for i in range(n):
#         print("Meow")

# main()



# def main():
#     number = get_number()
#     print_Meow(number)


# def get_number():
#     while True:
#         i = int(input("Enter the number: "))
#         if i > 0:
#             return i

# def print_Meow(n):
#     for i in range(n):
#         print("Meow")

# main()


# harry porter

# student = ["Harmioni", "Harry", "Ron"]

# for i in range(3):
#     print(student[i])


# # another way to do it in python
# for stud in student:
#     print(stud)


# another way to do this code


# student = ["Harmioni", "Harry", "Ron"]

# for i in range(len(student)):
#     print(i+1,":",student[i], end = "\n")



# dictionary
#https://youtu.be/nLRL_NcnK-4?t=12773