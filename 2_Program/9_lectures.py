# Packages
# third party library that we need to install in our pc and than we can use it
# Module: A single Python file (.py) containing code.
# Package: A directory that contains one or more modules (and optionally sub-packages).
# you can download package from PyPi - https://pypi.org/
# pip is Python's package installer and package manager.

# we are using module cowsay
# in terminal run this comman python -m pip install cowsay
# or u can run pip install cowsay both works fine 


import cowsay
import sys
# cowsay.cow("Hello!, My name is Cow and I am a duck")

# if len(sys.argv) == 2:
#     #cowsay.cow(f"Hello, {sys.argv[1]}")           # or u can cowsay.cow("Hello, "+ sys.argv[1])
#     cowsay.trex("Broo I am Bestttt")
#     # import cowsay

cowsay.cow("Hello!")
cowsay.trex("ROAAAAR!")
cowsay.dragon("Hello, human!")
cowsay.tux("Linux!")
cowsay.kitty("Meow")
cowsay.ghostbusters("HeLOO~~~~OO")
cowsay.turkey("Hello I am from Turkey")




