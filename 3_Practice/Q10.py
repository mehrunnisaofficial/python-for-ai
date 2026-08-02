# Shopping Receipt

print("Welcome User Hope you like shopping at V-Mart")

name = input("May I know your name? ")
phone_no = int(input("Enter your number: "))
product = input("What you purchased? ")
bill = float(input("Your total bill is: "))

print("\nShopping Receipt")
print(f"Customer  : {name}")
print(f"Phone N0. : {phone_no}")
print(f"Product   : {product}")
print(f"Price     : £{bill:,.2f}")