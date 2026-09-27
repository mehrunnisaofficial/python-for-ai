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
cowsay.cow("Hello!, My name is Cow and I am a duck")

if len(sys.argv) == 2:
    cowsay.cow(f"Hello, {sys.argv[1]}")           # or u can cowsay.cow("Hello, "+ sys.argv[1])


cowsay.cow("Hello!")
cowsay.trex("ROAAAAR!")
cowsay.dragon("Hello, human!")
cowsay.tux("Linux!")
cowsay.kitty("Meow")
cowsay.ghostbusters("HeLOO~~~~OO")
cowsay.turkey("Hello I am from Turkey")



# #---------------------------------------------------------

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

#---------------------------------------------------------------

import requests
# import json

base_url = "https://v2.jokeapi.dev"


def get_joke(joke_id, category):
    url = f"{base_url}/joke/{category}?idRange={joke_id}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Accessed {response.status_code}")
        joke_data = response.json()
        #print(json.dumps(joke_data, indent = 2))
        return joke_data
    else:
        print(f"Failed to access {response.status_code}")

joke_id = int(input("Please enter joke id: "))
category = input("Category of joke: ")
joke_info = get_joke(joke_id, category)

print(f"\nJOKE\n")

if joke_info["type"] == "twopart":
    print(joke_info["setup"])
    print(joke_info["delivery"])
else:
    print(joke_info["joke"])

#-----------------------------------


# import request to use it and this code only ask category rather than ID 
import requests

base_url = "https://v2.jokeapi.dev"


def get_joke(category):
    url = f"{base_url}/joke/{category}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Accessed {response.status_code}")
        joke_data = response.json()
        return joke_data
    else:
        print(f"Failed to access {response.status_code}")


category = input("Category of joke: ")
joke_info = get_joke(category)

print(f"\nJOKE\n")

if joke_info["type"] == "twopart":
    print(joke_info["setup"])
    print(joke_info["delivery"])
else:
    print(joke_info["joke"])

#---------------------------------------

# using nasa API to get random data

import requests

base_url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY"

# Send the request and store the server's response inside response.
response = requests.get(base_url)            # here response is a variable which holds the response objects

# status_code is an attribute of the Response object that tells you whether the request worked and what happened.
print(response.status_code)

data = response.json()

print(data["title"])
print(data["date"])
print(data["explanation"])
print(data["url"])


# check out more status code here : https://en.wikipedia.org/wiki/List_of_HTTP_status_codes







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


# now what is json 

# JSON (JavaScript Object Notation) → A common format used 
# to store and exchange structured data between programs.
# APIs commonly use JSON to send and receive data.
# response.json() → Converts the JSON 
# response into Python data, usually a dictionary or list.
"""
Remember this difference
response.json()
Converts the JSON response into a Python dictionary/list 
that you can work with.

json.dumps(data, indent=2)
Converts a Python dictionary/list into a formatted 
JSON string, mainly useful when you want to display it nicely.
"""