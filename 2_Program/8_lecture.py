# Libraries

# heads and tails game

import random
print("\nHead and Tails Game")
coin = ["Heads", "Tails"]
chance = random.choice(coin)

print(chance)


# who will become the theif

print("\nWho is the theif Game")
theif = random.choice(["Iram", "Iqra", "Huzaifa", "Afshan"])

print(theif)

# using shuffle to actually shuffle
# making card shuffling game

print("\nCards Shuffling Game")
cards = ["Jack", "King", "Queen", "3", "7"]
random.shuffle(cards)

for card in cards:
    print(card)


# rather than using "import random" we can use from keyword too

from random import choice
print("\nNew way to Import and show")
who = ["Noor", "Afshan", "Huzaifa"]
print(f"{choice(who)}")

# taking out mean

import statistics

print("\nUsing Statistics")
my_list = [1,12,345,1,1,3,1,3,3,3]
average = statistics.mean([1,12,345,1,1,3,1,3,3,3,4,555])

print(f"Mean = {average:,.2f}")
print(f"Median = {statistics.median([1,12,345,1,1,3,1,3,3,3,567]):,.2f}")

print(my_list)
print(f"Mode = {statistics.mode(my_list)}")
print(
    f"Multiple Mode = "
    f"{statistics.multimode(my_list)}"
)


# # choose between 1 - n number game

print("\nChoose Random Number Game")
number = random.randint(1,1000)
print(f"Random Number = {number}")
    


# studied till https://youtu.be/nLRL_NcnK-4?t=18766
















































# That's it for today.
# I am really tired.
#
# Meet you next day.
# Bye bye 👋

# Short Notes
# Libraries are simply, you can say, like real libraries.
# Have you ever seen real libraries?
# Books are written by you or someone else, and you can use that book's data
# again and again for your notes and studies.
#
# Same with Python libraries.
# They are made by someone else or by you, and you can use them in the same
# program or in other programs again and again.

# Library - a collection of reusable code that you can use in your programs.
# Module - a reusable unit of Python code, usually a single .py file.
# random - a Python module that provides functions for generating random
# values and making random selections.

# Bro, you don't have to install it.
# It already comes with Python. You just have to import it.

# I don't know, but I like the first version better because
# it looks more aesthetic, cleaner, and readable.
#
# `from random import choice` imports `choice` directly,
# so we don't need to use the module name `random`.
#
# Therefore, an identifier named `random` won't conflict
# with the imported `choice` function.
#
# But `choice` itself can still be overwritten by another
# identifier with the same name.







