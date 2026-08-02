# ============================================
# PROBLEM 1: Ask the user for their name
# ============================================

print("Hello, welcome to the program!")

# Taking input from the user
print("Enter your name:")
name = input("Enter your name: ")


# ============================================
# PROBLEM 2: Print the user's name
# Different ways to display output
# ============================================

print("So your name is", name)                     # Using comma
print("So your name is " + name)                  # Concatenation
print("So your name is {}".format(name))          # format()
print(f"So your name is {name}")                  # f-string (Recommended)
print("So your name is %s" % name)                # Old style formatting

# Printing additional information

print(
    "So your name is "
    + name
    + " and your name has "
    + str(len(name))
    + " characters."
)

print(
    "So your name is {} and your name has {} characters."
    .format(name, len(name))
)

print(
    f"So your name is {name} and your name has {len(name)} characters."
)

print(
    "So your name is %s and your name has %d characters."
    % (name, len(name))
)

# NOTE:
# You don't need to memorise every method.
# For now, using commas and f-strings is enough.


# ============================================
# PROBLEM 3: What whitespace is added by print()?
# ============================================

# By default, print() separates multiple values with one space.

print("Hello", name)
# Output:
# Hello David

# Internally it behaves like:
# "Hello" + " " + name

# We can change or remove that space using sep=


# ============================================
# PROBLEM 4: Using sep=
# ============================================

name = input("Enter your name: ")

print("Hello", name)
print("Hello", name, sep="")
print("Hello", name, sep="❤️")
print("Hello", name, sep="(˶˃ ᵕ ˂˶)")

# Default:
# sep=" "


# ============================================
# PROBLEM 5: Using end=
# ============================================

age = input("Enter your age: ")

print("Hello,", name, end=". ")
print("Your age is", age)

# Normally print() ends with:
# end="\n"

# Changing end allows us to continue printing
# on the same line.


# ============================================
# PROBLEM 6: Using sep= and end= together
# ============================================

marks = input("Enter your marks: ")

print(
    "Hello",
    name,
    "So you are a student.",
    sep=" * ",
    end=" END OF LINE.\n"
)

# or one line

print("Hello", name, "So you are a student.", sep=" * ", end=" END OF LINE.\n")


# ============================================
# PROBLEM 7: Quotes inside quotes
# ============================================

print("Hello, \"Friend\"")

# OR

print('Hello, "Friend"')


# ============================================
# PROBLEM 8: f-Strings
# ============================================

print(f"Hello, {name}")


# ============================================
# PROBLEM 9: What if the user enters extra spaces?
# ============================================

# Example input:
#        john

# We don't want those extra spaces.

name = input("Enter your name: ")

name = name.strip()

print(f"Hello, {name}")

# strip() removes whitespace from both ends.


# ============================================
# PROBLEM 10: Capitalising the first letter
# ============================================

name = input("Enter your name: ")

name = name.capitalize()

print(f"Hello, {name}")

# john
# ↓
# John

# But:

# john doe
# ↓
# John doe

# Only the first letter of the entire string changes.


# ============================================
# PROBLEM 11: Capitalising every word
# ============================================

name = input("Enter your name: ")

name = name.title()

print(f"Hello, {name}")

# john doe
# ↓
# John Doe


# ============================================
# PROBLEM 12: Chaining methods
# ============================================

name = input("Enter your name: ")

name = name.strip().title()

print(f"Hello, {name}")

# We can even do it in one line.

name = input("Enter your name: ").strip().title()

print(f"Hello, {name}")


# ============================================
# PROBLEM 13: Using split()
# ============================================

name = input("Enter your full name: ")

# split() breaks a string into multiple words
# and returns them as a list.

parts = name.split()
print(parts)

# Example:
# Input:
# John Doe
#
# parts becomes:
# ["John", "Doe"]


# ============================================
# PROBLEM 14: Accessing words using indexing
# ============================================

# Lists start indexing from 0.

first = parts[0]
last = parts[1]

# or we can do it in one line:
first, last = parts[0], parts[1]

print(f"First name: {first}")
print(f"Last name: {last}")

# NOTE:
# This will give an IndexError if the user enters only one name.


# ============================================
# PROBLEM 15: Unpacking
# ============================================

# Instead of writing:
#
# first = parts[0]
# last = parts[1]
#
# Python lets us unpack the list.

first, last = parts

print(first)
print(last)

# NOTE:
# This only works when the list contains exactly two items.
#
# "John Doe"          ✅ Works
# "John"              ❌ ValueError
# "John Michael Doe"  ❌ ValueError


#https://youtu.be/nLRL_NcnK-4?t=3843