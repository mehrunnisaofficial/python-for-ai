# Lecture Link: https://youtu.be/NA4pd7Gg7vQ
# Now lets use our third party library which we downloaded - pytest
# To install pytest we need to write this line in terminal
# python -m pip install pytest

from Lecture10 import square

def test_square4():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# Now our code gives the assertion error but this is so much easy right
# Easier than our previous codes
# rather than writing 10s of lines of code just to get that our code works or not
# this third party library do the same thing for us