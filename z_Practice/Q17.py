from random import randint
import sys


def main():
    print("---- LET'S START A GAME ----\n")

    print("---------- RULES ----------")
    print("* You will get only 3 chances.")
    print("* If you win, you will get a TOFFEE.")
    print("* If you lose, you have to SMILE.")
    print("* Don't curse DUDEEEE.\n")

    player_name = input("Enter your name: ").strip().capitalize()
    computer_number = generate_number()

    for chance in range(3):
        player_guess = get_player_guess()

        if player_guess == computer_number:
            print(f"\nGuess what, {player_name}! You won the game!")
            print("Here is your toffee 🍭")
            break

        print(f"\nWRONG GUESS, {player_name}!")

        if chance < 2:
            print("GUESS AGAIN!\n")

    else:
        print("\nYOU LOSE 😭")
        print(f"The computer's number was: {computer_number}")
        print("But hey... you still have to SMILE 😌")


def generate_number():
    """Generate a random number between 1 and 100."""
    return randint(1, 100)


def get_player_guess():
    """Get and validate the player's guess."""
    invalid_attempts = 0

    while True:
        try:
            guess = int(input("Guess a number (1 to 100): "))

            if 1 <= guess <= 100:
                return guess

            invalid_attempts += 1
            print("\nPlease enter a NUMBER between 1 and 100.")

        except ValueError:
            invalid_attempts += 1
            print("\nPlease enter a NUMBER.")

        if invalid_attempts == 3:
            sys.exit(
                "\nYou have entered 3 invalid inputs.\n"
                "BYEEEEEEEE 👋"
            )



main()



# Things i need to add in this 
# -> If user give answer which is greater (or less) than computer guess 
#    it should return too high ( or too low )
