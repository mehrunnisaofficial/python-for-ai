# 4. Shuffle the Cards
# Let's make a casino where every player will get 5 cards and than in the end 
# every player have to show all of its card
# ik ik thats not how cards work but I don't know how to play this game :|

# Create a 52-card deck, shuffle it, and distribute the cards
# as equally as possible among the players.
# Any cards left over will remain in storage.



from random import shuffle


def main():
    print("---- SHUFFLING ----\n")

    # Get the number of players and their names.
    player_number = get_player_number()
    players = get_players(player_number)

    # Calculate how many cards each player will receive.
    # // gives the whole-number result.
    # % gives the number of cards left over.
    cards_per_player = 52 // player_number
    storage = 52 % player_number

    # Create the deck and randomly shuffle all 52 cards.
    deck = cards()
    shuffle(deck)

    # Create a list to store each player's hand.
    hands = []

    # Deal the same number of cards to every player.
    for division in players:
        hand = []

        for card in range(cards_per_player):
            hand.append(deck.pop())

        hands.append(hand)

    # Any cards remaining in the deck are stored separately.
    storage_cards = deck

    # Pair each player with their hand using zip().
    for game_player, their_cards in zip(players, hands):
        print(f"\n{game_player} you got: ")

        # Display every card belonging to the player.
        for card in their_cards:
            print(f"    {card}")

    # Display the cards that were not distributed.
    print("---------------------------------")
    print("\n        STORAGE")

    for storage_card in storage_cards:
        print(f"    {storage_card}")


def cards():
    # A standard deck has 13 ranks and 4 suits.
    # 13 × 4 = 52 cards.
    ranks = [
        "Ace", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "Jack", "Queen", "King"
    ]

    suits = [
        "Hearts",
        "Diamonds",
        "Clubs",
        "Spades"
    ]

    cards = []

    # Combine every rank with every suit to create the deck.
    for suit in suits:
        for rank in ranks:
            cards.append(f"{suit} of {rank}")

    return cards


def get_player_number():
    # Keep asking until the user enters a valid number of players.
    while True:
        try:
            player_number = int(input("Enter the number of Players: "))

            # Allow between 5 and 10 players.
            if 5 <= player_number <= 10:
                return player_number

            print("Please enter a number between 5 and 10.")

        # Handle input that cannot be converted to an integer.
        except ValueError:
            print("Can you PLEASE enter a number? you dummmmmbbb😭")


def get_players(player_number):

    players = []

    # Ask for the name of each player.
    for i in range(player_number):
        while True:
            name = input(
                f"Enter the name of Players {i + 1}: "
            ).strip().title()

            # Remove spaces temporarily and check that
            # the remaining characters are alphabetic.
            if name.replace(" ", "").isalpha():
                players.append(name)
                break

            print("Please enter a name.")

    return players


main()



# ------- PSEUDOCODE -------

# START

#     Display "SHUFFLING"

#     Ask for number of players
#         Keep asking until the number is between 5 and 10

#     Ask for the name of each player
#         Keep asking until a valid name is entered
#         Store all player names

#     Calculate how many cards each player gets
#         cards per player = 52 // number of players
#         remaining cards = 52 % number of players

#     Create a standard deck of 52 cards
#         Create 13 ranks
#         Create 4 suits
#         Combine every rank with every suit

#     Shuffle the deck randomly

#     Create an empty list called hands

#     FOR each player:
#         Create an empty hand

#         REPEAT cards per player times:
#             Remove one card from the deck
#             Add the card to the player's hand

#         Add the player's hand to hands

#     Store the remaining cards as storage cards

#     FOR each player and their hand:
#         Display the player's name
#         Display all cards in their hand

#     Display the storage cards

# END