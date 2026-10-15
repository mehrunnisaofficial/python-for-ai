import re

email = input("Enter the email of the user: ")

if re.search("..+@..+", email):
    print("Valid")
else:
    print("Invalid")
    