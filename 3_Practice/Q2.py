# ==========================================================
# PRACTICE: Clean the user's name and display information
# ==========================================================

# Task:
# 1. Remove extra spaces from the beginning and end.
# 2. Correct the capitalization (e.g. noOr → Noor).
# 3. Convert the name to uppercase.
# 4. Display the name length.
# ==========================================================


# ----------------------------------------------------------
# Method 1: Step-by-step (Best for beginners)
# ----------------------------------------------------------

# name = input("Enter your name sir: ")

# clean_name = name.strip()              # Remove extra spaces
# formatted_name = clean_name.capitalize()   # noOr -> Noor
# uppercase_name = formatted_name.upper()    # Noor -> NOOR

# print(f"Your name has {len(clean_name)} characters.")
# print("Formatted name :", formatted_name)
# print("Uppercase name :", uppercase_name)


# ----------------------------------------------------------
# Method 2: Skip capitalize() if only uppercase is needed
# ----------------------------------------------------------

# name = input("Enter your name sir: ")

# clean_name = name.strip()
# uppercase_name = clean_name.upper()

# print(f"Your name has {len(clean_name)} characters.")
# print("Uppercase name :", uppercase_name)


# ----------------------------------------------------------
# Method 3: Method Chaining
# ----------------------------------------------------------

# name = input("Enter your name sir: ").strip().capitalize()

# print(f"Your name has {len(name)} characters.")
# print("Formatted name :", name)


# ----------------------------------------------------------
# Method 4: Method Chaining with Uppercase
# ----------------------------------------------------------

# name = input("Enter your name sir: ").strip().upper()

# print(f"Your name has {len(name)} characters.")
# print("Uppercase name :", name)


# ----------------------------------------------------------
# Method 5: Everything in One Output
# ----------------------------------------------------------

name = input("Enter your name sir: ").strip().upper()

print(f"Your name has {len(name)} characters and your name in uppercase is {name}.")