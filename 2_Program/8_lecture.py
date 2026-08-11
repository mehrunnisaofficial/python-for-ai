# Libraries

# It's literally 11:08 pm, I badly wanna sleep but I don't wanna break my streak
# so let's start learning

import random


# Coin flipping game

coin = random.choice(["Heads", "Tails"])
print(coin)


# Or an easier way

from random import choice

gender = choice(["Boy", "Girl"])
print(gender)

# another way 

idk = random.choice(["You", "Me"])
print(idk)


# Random number

num_choose = random.randint(1, 100)
print(num_choose)


# Random cards

cards = [
    "Ace",
    "King",
    "Queen",
    "Jack",
    "10",
    "9",
    "8",
    "7",
    "6",
    "5"
]

random.shuffle(cards)

for card in cards:
    print(card)


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