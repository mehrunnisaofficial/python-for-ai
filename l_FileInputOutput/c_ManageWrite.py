for i in range(5):
    name = input("Enter your name: ")
    place = input("Enter your country: ")

    with open("c_ManagingIDK.csv", "a") as file:
        file.write(f"{name},{place}\n")


















# Documentation
# https://docs.python.org/3/library/csv.html