# # take input - name from the user

name = []   # it is an empty list
size = int(input("Enter how many students name you wanna store: "))

print("\nEnter names")
for i in range(size):
    namee = input(f"Student {i + 1}:").strip().capitalize()
    name.append(namee)

    # another way to append without any additional variable
    # name.append(input("Enter your name: "))


print("\nAll students name is:")
for i in name:
    print(i)

print("\nSorted Name is:")
for i in sorted(name):
    print(i)


size = int(input("Enter how many user data you wanna store: "))
student = input("Enter user name: ").strip().capitalize()
file = open("Names.txt", "w")               # But this overwrites means erase previous data and enter new data
file.write(student)
file.close()


# I also wanna store multiple names at once

for i in range(size):
    student = input("Enter user name: ").strip().capitalize()
    file = open("Names.txt", "w")               # But this operwrites means erase previous data and enter new data
    file.write(student)
    file.close()

# But still it overwrites and we only see the last input
# To solve this we need to append the file 


for i in range(size):
    student = input("Enter user name: ").strip().capitalize()
    file = open("Names.txt", "a")               # This doesnt overwrite instead it append
    file.write(f"{i + 1}) {student}\n")
    file.close()


# these is a chance where many times you forgot to close the file
# more pythonic way to do it 

for i in range(size):
    student = input("Enter user name: ").strip().capitalize()

    with open("Names.txt", "a") as file:
        file.write(f"{student}\n")
    























# But I think till now you all wil get litle suspicious that
# till now we write code enter data and the moment we kill terminal
# all data lost
# now here comes our topic - FILE I/O





# Documentation - read all this if u want better knowledge
# https://docs.python.org/3/builtins/functions.html#open
