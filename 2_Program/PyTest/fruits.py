# Context-Sensitive Comaprison

def test_compare_fruits():
    set1 = set(['Apple', 'Mango', 'Banana', 'Watermelon'])
    set2 = set(['Apple', 'Banana', 'Mango', 'Watermelon'])
    set3 = set(['Apple', 'Hello', 'Mango', 'Annanas'])

    # Assertion
    assert set1 == set2
    assert set2 == set3






# NOTES
# to run the specific test in the test file we will write specific command
# python -m pytest 2_Program\Unit_test\fruits.py
# otherwise python will execute all test inside the folder
# The test_ filename tells pytest to inspect this file for tests, and test_ 
# functions tell pytest which functions inside that file are tests.

# Set1 == set2 
# does NOT give an error because sets ignore 
# the order of elements. Both sets contain the exact same fruits, 
# so the comparison is True.

# set2 == set3 
# DOES give an error because the sets contain different elements:
# set2 → Apple, Banana, Mango, Watermelon
# set3 → Apple, Hello, Mango, Annanas
# this will give Assertion Error 
# and if u need detail where to make changes 
# python -m pytest 2_Program\Unit_test\fruits.py
# write this code in the terminal and you will get in detial 
# what sets are different