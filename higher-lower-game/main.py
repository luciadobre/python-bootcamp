from art import logo, vs
from game_data import data
import random

running = True


def pick(choice):
    """Make a random choice, print the choice and assign the follower_count value"""
    random_value = dict(random.choice(list(data)))
    follower_count = random_value['follower_count']
    print(follower_count)
    print(f"Compare {choice}: {random_value['name']}, a {random_value['description']}, from {random_value['country']}.")
    return follower_count


def compare(player_answer, other_answer):
    """Compare answers"""
    if player_answer > other_answer:
        return True
    else:
        return False


def set_score(score):
    """Add 1 to score if answer is right"""
    score += 1
    print(f"You got it right! Score is {score}")
    return score


def main():
    score = 0

    got_it_wrong = False

    while not got_it_wrong:

        follower_count1 = pick('A')
        print(vs)
        follower_count2 = pick('B')
        # If duplicate, pick again
        while follower_count2 == follower_count1:
            follower_count2 = pick('B')

        answer = input("Who has more followers? Type 'A' or 'B':").lower()

        # Assign follower count to answer
        if answer == 'a':
            player_answer = follower_count1
            other_answer = follower_count2
        elif answer == 'b':
            player_answer = follower_count2
            other_answer = follower_count1
        else:
            print('Not a valid answer!')

        if compare(player_answer, other_answer):
            score = set_score(score)
        else:
            print(f"Incorrect! Game over! Final score: {score}")
            got_it_wrong = True

    print(score)


while running:
    main()
    if input("Would you like to keep playing? Press 'y' for yes, 'n' for no.") != 'y':
        running = False
