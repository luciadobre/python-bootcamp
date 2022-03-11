import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

game_on = 'y'


def guessing_game():
    EASY_TRIES = 10
    HARD_TRIES = 5
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

    def set_difficulty(diff=difficulty):
        """Set the number of tries"""
        if diff == 'easy':
            return EASY_TRIES
        else:
            return HARD_TRIES

    nr_of_tries = set_difficulty()

    print(f"You have {nr_of_tries} attempts to guess the number.")
    guess = int(input("Make a guess:"))

    def user_guess(users_guess, user_answer, turns):
        """Check guess against random number"""
        if users_guess > user_answer:
            print("Too high!")
        elif users_guess < user_answer:
            print("Too low!")
        return turns - 1

    while nr_of_tries > 0:
        nr_of_tries = user_guess(guess, number, nr_of_tries)
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
