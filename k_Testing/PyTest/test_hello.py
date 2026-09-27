from k_Testing.PyTest.stringg import hello

def test_helloo():
    assert hello("Noor") == "Hello, Noor"

# Why does this test fail?
# Because assert checks the value returned by the function.
# Our hello() function uses print() instead of return().
# print() only displays "Hello, Noor" on the screen; it does not
# give that value back to the caller.
# Therefore, hello("Noor") returns None.
# So the test is effectively checking:
#
#     assert None == "Hello, Noor"
#
# which is False.