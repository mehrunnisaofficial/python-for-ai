from traingle import tri  #ik triangle spelling is wrong


# This is called Entity Comparison

def test_draw_traingle():
    expected = "@"
    actual = '\n'.join(tri(1))   # "@\n@@\n@@@" if we gave 3 input
    # why we use .join here?
    # cause yield gave multiple values
    # and these values gets join  (means multiple string joins and become 1)
    assert expected == actual


# Now open terminal and write python -m pytest if it give F means failes
# and if u want more detial: python -m pytest -v write this in terminal
# pytest needs an exception to 
# escape the test function for it to mark that test as failed

# we wrote another version of tri and change something in for loop 
# now if we re-run the python -m pytest -v in terminal
# we will get the passed output in terminal
