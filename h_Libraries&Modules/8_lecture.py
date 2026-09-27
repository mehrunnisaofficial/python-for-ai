# Libraries - Modules

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


# choose between 1 - n number game

print("\nChoose Random Number Game")
number = random.randint(1,1000)
print(f"Random Number = {number}")
    


# command line argument

import sys

# sys.argv[0] = python file_name.py
# if u dont give any extra string here than u will get IndexError


print(f"Hello, My name is {sys.argv[1]}")
print(f"Hello, My name is {sys.argv[1:]}")    # print all string after 0th index
print(f"Hello, My name is {sys.argv[1:3]}")   # print all string after 0th index to 3rd index


# To not get index error we can use 
import sys
try:
    print(f"Hello, My name is {sys.argv[1]}")
except IndexError:
    print("\nBroo write your name atleast\n")


# we can handle the error in another way
import sys
if len(sys.argv) < 2:
    print("Too few argument")
elif len(sys.argv) > 2:                  # we can skip elif if u don't want the user will give too many argumnets
    print("Too many argument")
else:
    print(f"Hello, My name is {sys.argv[1]}")



# using for loop to print print(f"Hello, My name is {sys.argv[1:3]}") 
import sys
for argument in sys.argv[1:]:
    print(argument, end = " ")
    print(f"{argument}", end = " ")


# another way
# we will give in command line 
# python 8_lecture.py "Mehrunnisa Baby"

import sys
print(f"Hello, My name is {sys.argv[1]}")

# output : Identify yourself (๑ᵔ⤙ᵔ๑)

# another funciton in sys
# sys.exit() = “Aight, I’m out 🫡” → immediately stops the Python program.

import sys
print("Hello")
sys.exit()
print("This will never print")

# won't give any error check out by yourself

import sys
if len(sys.argv) < 2:
    sys.exit("Too few argument")
elif len(sys.argv) > 2:                  
    sys.exit("Too many argument")


print(f"Hello, My name is {sys.argv[1:-1]}")



# studied till https://youtu.be/nLRL_NcnK-4?t=20200

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
  
 
# A command-line argument is extra information you provide 
# when running the program in the terminal.

# sys is a Python module that provides access to 
# various things related to the Python interpreter and system.

# Python receives the command-line arguments, 
# and the sys module gives your Python program access to them.

"""
Command-line arguments are the extra arguments we 
give when running a program through the terminal.

sys is a Python module through which the Python 
program can access those command-line arguments.

Those arguments are available in a list called argv, 
which we access as sys.argv

So:

Terminal
   │
   │  python program.py hello 123
   ↓
Python receives the arguments
   │
   ↓
sys.argv
   │
   ↓
['program.py', 'hello', '123']
"""


