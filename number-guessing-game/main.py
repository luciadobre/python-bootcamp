import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

game_on = 'y'


def guessing_game():
    number = random.randrange(0, 100)
    print(f"The number is: {number}")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard':").lower()
    difficulties = ['easy', 'hard']

    # In case the player doesn't type the correct input for difficulty
    while difficulty not in difficulties:
        difficulty = input(
            "That is not a valid difficulty! Please type 'easy' or 'hard'. Type 'quit' to exit the game.").lower()
        if difficulty == "quit":
            exit()
        if difficulty in difficulties:
            break

    if difficulty == 'easy':
        nr_of_tries = 10
    else:
        nr_of_tries = 5

    print(f"You have {nr_of_tries} attempts to guess the number.")
    guess = int(input("Make a guess:"))

    def user_guess():
        """User guessed wrong"""
        if guess > number:
            print("Too high!")
        elif guess < number:
            print("Too low!")
        else:
            print("Default answer")
        return nr_of_tries - 1

    while nr_of_tries > 0:
        nr_of_tries = user_guess()
        guess = int(input("Make a guess:"))
        if guess == number:
            break

    if nr_of_tries == 0:
        print(f"You lose! The answer was {number}")
    else:
        print(f"You guessed right! The answer was {number}")


while game_on == 'y':
    guessing_game()
    game_on = input("Would you like to play again? Type 'y' for yes, 'n' for no.")
