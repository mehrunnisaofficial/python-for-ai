# # using request packages


# import requests

# def main():
#     base_url = "https://v2.jokeapi.dev"
#     selected_category = category()

#     print(f"You choose {selected_category} joke")

#     joke_info = get_data(base_url, selected_category)    # here result will be store after accessing

#     if joke_info["type"] == "twopart":
#         print(f"{joke_info["setup"]}")
#         print(f"{joke_info["delivery"]}")
#     else:
#         print(joke_info["joke"])


# def get_data(base_url, selected_category):
#     url = f"{base_url}/joke/{selected_category}"
#     response = requests.get(url)

#     if response.status_code == 200:
#         print("Data accessed 200")
#         result = response.json()
#         return result
#     else:
#         print(f"Data can't retrieve {response.status_code}")


# def category():
#     print("        CATEGORY        ")
#     list = ["Programming", "Misc", "Dark","Pun", "Spooky", "Christmas"]

#     for i in range(6):
#         print(f"{i+1}. {list[i]}")

#     while True:
#         try:
#             choice = int(input("Choose category you want: "))

#             if ((choice < 7) and (choice > 0)):
#                 break
#             else:
#                 print("404 Please Re-enter")

#         except ValueError:
#             print("Please enter an Integer")

#     return list[choice-1]

# main()




