# print first and second name of the user

# ==========================================================
# Method 1: Unpacking
# ==========================================================

name = input("Enter your name: ")

first_name, last_name = name.split()

print(f"First name: {first_name}")
print(f"Last name: {last_name}")


#or 


# ==========================================================
# Method 2: Indexing
# ==========================================================

name = input("Enter your name: ")

parts = name.split()

first_name = parts[0]
last_name = parts[1]

print(f"First name: {first_name}")
print(f"Last name: {last_name}")
