# ==========================================================
# Username Generator Practice
# ==========================================================


# ----------------------------------------------------------
# Method 1: Username using first and last name
# Example: Noor Afshan → noor_afshan
# ----------------------------------------------------------

# first_name, last_name = input("Enter your full name (2 words): ").lower().split()

# print(f"Username: {first_name}_{last_name}")


# ----------------------------------------------------------
# Method 2: Username using first initial + last name
# Example: Noor Afshan → nafshan
# ----------------------------------------------------------

# first_name, last_name = input("Enter your full name (2 words): ").lower().split()

# print(f"Username: {first_name[0]}{last_name}")


# ----------------------------------------------------------
# Method 3: Username using first name + a character
# Example: Noor Afshan → noorh
# ----------------------------------------------------------

first_name, last_name = input("Enter your full name (2 words): ").lower().split()

print(f"Username: {first_name}{last_name[3]}")


# ----------------------------------------------------------
# Method 4: Name Initials
# Example: Noor Afshan → N.A
# ----------------------------------------------------------

# first_name, last_name = input("Enter your full name (2 words): ").split()

# print(f"Initials: {first_name[0]}.{last_name[0]}")