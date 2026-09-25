# Lecture link: https://youtu.be/nLRL_NcnK-4?t=22172

from Lecture10 import square

def main():
    test_square1()
    test_square2()
    test_square3()

# 1st way to check is: using if else
def test_square1():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    if square(4) != 16:
        print("4 squared was not 16")

# 2nd way to check is: using assert   - this gives assertion error
def test_square2():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

# Now to handle the error we learn try-except
# # 3rd way to check is: using assert with try except
def test_square3():
    try:
        assert square(2) == 4       # it is stating a fact that square of 2 must be 4
    except AssertionError:          # if not it will give assertion error
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")


# Lets understand assert more

x = "Hello"
assert x == "Goodbye", "X Should be \"Hello\""
# This will raise an assertion error 



if __name__ == "__main__":
    main()



# Now what is assert?
# Assert - means a statements that assert or states a fact and present it 
# confindetally in your code
# three most used teating frameworks exist in python is :
# -> pytest   (Third party library)
# -> unittest ( python inbuilt library)
# -> nose     (third party library)
# But isn't it so weird
# we have to write so much lines of code just to check our two lines of code
# means for 3 line of main solution
# we wrote more than 10 lines to check whether the code is correct or not
# thats why to solve this we will use pytest
# a third party library which is used to check whether our code is correct or not
