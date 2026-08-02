# ==========================================================
# PRACTICE 1: Print the user's name without spaces
# ==========================================================

name = input("Enter your name please: ")

# Remove all spaces from the name
joined_name = name.replace(" ", "")

print("Hello", joined_name, sep="")


# ==========================================================
# PRACTICE 2: Using the end parameter
# ==========================================================

name = input("Enter your name please: ")

print("Loading your name...", end="")
print("\nHello", name, end="\nDone...")