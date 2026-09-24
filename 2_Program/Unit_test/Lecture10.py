# UNIT TEST

# Program is something that u wrote to solve a problem
# Unit test is a part of code which u write to check whether
# the created solution is correct or not
# so u write a program to check your actual program is correct or not


# Creating Module

def main():
    x = int(input("Enter the value you wanna do square of: "))
    print(f"Square of {x} = {square(x)}")

def square(a):
    return a + a

if __name__ == "__main__":
    main()