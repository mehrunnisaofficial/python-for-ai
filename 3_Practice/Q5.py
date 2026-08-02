# Bill Splitter

bill = float(input("Enter the receipt amount: "))
friends = int(input("Enter the total number of friends: "))

my_contribution = bill / friends

print(f"The total amount you have to pay is: {my_contribution:,.2f} rupees")