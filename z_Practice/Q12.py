# ============================================
# PROBLEM 24: Name Analyzer
# ============================================

# Ask for the user's full name
name = input("Enter your full name: ").title()

# Split the name into separate words
parts = name.split()

# Print the full name
print("Hello", *parts)

# --------------------------------------------
# Method 1: Using join()
# --------------------------------------------

print(f"Total characters: {len(''.join(parts))}")
print(f"First name: {parts[0]}")
print(f"Last name : {parts[-1]}")

# --------------------------------------------
# Method 2: Using replace()
# --------------------------------------------

print(f"Total characters: {len(name.replace(' ', ''))}")
print(f"First name: {parts[0]}")
print(f"Last name : {parts[-1]}")


# ============================================
# NOTES
# ============================================

# * is called the unpacking operator.
# It takes every item from a list and passes them separately.

# Example:
# parts = ["Noor", "Afshan", "Khan"]
#
# print(parts)
# Output:
# ['Noor', 'Afshan', 'Khan']
#
# print(*parts)
# Output:
# Noor Afshan Khan

# split() : Converts a string into a list.
# join()  : Converts a list into a string.
# replace(): Replaces part of a string with another string.

# Examples:

# " ".join(parts)
# Output:
# Noor Afshan Khan

# "".join(parts)
# Output:
# NoorAfshanKhan

# "-".join(parts)
# Output:
# Noor-Afshan-Khan

# "*".join(parts)
# Output:
# Noor*Afshan*Khan

# name.replace(" ", "")
# Output:
# NoorAfshanKhan