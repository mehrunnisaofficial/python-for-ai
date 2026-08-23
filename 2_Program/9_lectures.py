# Packages
# third party library that we need to install in our pc and than we can use it
# Module: A single Python file (.py) containing code.
# Package: A directory that contains one or more modules (and optionally sub-packages).
# you can download package from PyPi - https://pypi.org/
# pip is Python's package installer and package manager.

# we are using module cowsay
# in terminal run this comman python -m pip install cowsay
# or u can run pip install cowsay both works fine 


# import cowsay
# import sys
# cowsay.cow("Hello!, My name is Cow and I am a duck")

# if len(sys.argv) == 2:
#     cowsay.cow(f"Hello, {sys.argv[1]}")           # or u can cowsay.cow("Hello, "+ sys.argv[1])


# cowsay.cow("Hello!")
# cowsay.trex("ROAAAAR!")
# cowsay.dragon("Hello, human!")
# cowsay.tux("Linux!")
# cowsay.kitty("Meow")
# cowsay.ghostbusters("HeLOO~~~~OO")
# cowsay.turkey("Hello I am from Turkey")

import requests
# import json

base_url = "https://pokeapi.co/api/v2"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    # print(response)

    if response.status_code == 200:
        print("Data retrieved")
        pokemon_data = response.json()
        # print(json.dumps(pokemon_data, indent = 2))  # print all data 
        return pokemon_data   # it is in the dictioanary form
    else:
        print(f"Failed to retrive data {response.status_code}")


pokemon_name = input("Please enter the name of the Pokemon you want: ")
pokemon_info = get_pokemon_info(pokemon_name)

print(f"Name : {pokemon_info["name"]}")
print(f"Height : {pokemon_info["height"]}")
print(f"Weight : {pokemon_info["weight"]}")
print(f"ID : {pokemon_info["id"]}")

# Studied Till : https://youtu.be/nLRL_NcnK-4?t=21289









































# I was kinda confused in library, packages, modules, API, server , request
# So I tried to make it little easier 
# but I am still kinda confused
# Library → A collection of reusable code that you can use in your programs.
# Module → A single .py file containing reusable Python code.
# Package → A collection of related Python modules.
# API → A way for one software/program to communicate with another software/system.
# Request → A message sent to another system asking for data or an action.
# Response → The answer/data sent back after a request.
# requests → A Python library used to send HTTP requests to APIs and web servers.
# HTTP → HTTP is a set of rules for how a program communicates with a web server/API.
# HTTP request → a request/message your program sends to a web server through HTTP rules.

# so what is .trex(), .turkey(), .cow() etc...?

# cowsay                 ← package
#  │
#  ├── cow()             ← function
#  ├── trex()            ← function
#  ├── dragon()          ← function
#  ├── tux()             ← function
#  ├── kitty()           ← function
#  ├── ghostbusters()    ← function
#  └── turkey()          ← function