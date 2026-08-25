# Heads or Tails
# Create a program that randomly chooses either "Heads" or "Tails" using the random module.

from random import choice                                      # Import choice() from random module


def main():
    print("Welcome to the mini heads and tails game\n")

    player1, player1_need, player2, player2_need = player()    # Get player details and choices

    print("\n Let's start a GAME\n")

    value = flip_coin()                                        # Randomly flip the coin

    if player1_need == value:                                  # Check if Player 1 guessed correctly
        print(f"COIN = {value}")
        print(f"You won {player1} !!!")
        print(f"You lose {player2} !!!")
    else:                                                      # Otherwise, Player 2 wins
        print(f"COIN = {value}")
        print(f"You won {player2} !!!")
        print(f"You lose {player1} !!!")


def player():
    player1 = input("Enter the first player name: ").strip().capitalize()            # Get Player 1 name
    player1_need = input("Heads or Tails? ").strip().capitalize()                    # Get Player 1 choice

    while player1_need not in ["Heads", "Tails"]:                                    # Validate Player 1 choice
        print(f"Please re-enter your choice, {player1}")
        player1_need = input("Heads or Tails? ").strip().capitalize()

    player2 = input("Enter the second player name: ").strip().capitalize()           # Get Player 2 name
    player2_need = input("Heads or Tails? ").strip().capitalize()                    # Get Player 2 choice

    while player2_need not in ["Heads", "Tails"]:                                    # Validate Player 2 choice
        print(f"Please re-enter your choice, {player2}")
        player2_need = input("Heads or Tails? ").strip().capitalize()

    while player1_need == player2_need:                                              # Make sure choices are different
        print("Both players cannot choose the same thing.")

        player1_need = input(f"{player1}, Heads or Tails? ").strip().capitalize()    # Re-enter Player 1 choice

        while player1_need not in ["Heads", "Tails"]:                                # Validate new Player 1 choice
            print(f"Please re-enter your choice, {player1}")
            player1_need = input(f"{player1}, Heads or Tails? ").strip().capitalize()

        player2_need = input(f"{player2}, Heads or Tails? ").strip().capitalize()    # Re-enter Player 2 choice

        while player2_need not in ["Heads", "Tails"]:                                # Validate new Player 2 choice
            print(f"Please re-enter your choice, {player2}")
            player2_need = input(f"{player2}, Heads or Tails? ").strip().capitalize()

    return player1, player1_need, player2, player2_need                              # Return all player information


def flip_coin():
    choices = ["Heads", "Tails"]                                                     # Store possible coin results
    return choice(choices)                                                           # Randomly choose Heads or Tails


main()                                                                              # Start the program