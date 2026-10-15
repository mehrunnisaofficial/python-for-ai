for i in range(5):
    name = input("Enter your name: ")
    place = input("Enter your country: ")

    with open("a_Data.csv", "a") as file:
        file.write(f"{name},{place}\n")


        