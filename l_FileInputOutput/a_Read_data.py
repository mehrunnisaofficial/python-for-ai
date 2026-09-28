with open("a_Data.csv") as file:           # By default read mode
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} lives in {row[1]}")

print("\n-----------------------------------------\n")

# better way is to unpacking suing split
with open("a_Data.csv") as file:           # By default read mode
    for line in file:
        name, place = line.rstrip().split(",")
        print(f"{name} lives in {place}")