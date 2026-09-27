from k_Testing.PyTest.stringg import goodbye

def test_goodbye():
    assert goodbye("Noor") == "Goodbye, Noor"

    # check with no arguments
    assert goodbye() == "Goodbye, World"

    # lest check multiple items together
    for name in ["Bablu", "Rohan", "Carla", "Pearl", "Roohi"]:
        assert goodbye(name) == f"Goodbye, {name}"


# When we run this test, a green dot means the test passed successfully.
# It means the assertion was True, so no AssertionError occurred.
# However, a passed test does not prove that the code is completely correct.
# It only tells us that the specific behavior checked by this test worked
# successfully and no unexpected error occurred during the test.