import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

answer = 'y'


def blackjack():
    player_cards = []
    dealer_cards = []
    player_score = 0
    dealer_score = 0

    def player_deal(score):
        """Deal a random player card. Return score. Add score of the card to player score."""
        player_cards.append(random.choice(cards))
        score += player_cards[-1]
        while score > 21 and 11 in player_cards:
            for i in range(len(player_cards)):
                if player_cards[i] == 11:
                    player_cards[i] = 1
                    score -= 10
        return score

    def dealer_deal(score):
        """Deal a random dealer card. Return score. Add score of the card to dealer score."""
        dealer_cards.append(random.choice(cards))
        score += dealer_cards[-1]
        while score > 21 and 11 in dealer_cards:
            for i in range(len(player_cards)):
                if dealer_cards[i] == 11:
                    dealer_cards[i] = 1
                    score -= 10
        return score

    player_score = player_deal(player_score)
    dealer_score = dealer_deal(dealer_score)
    player_score = player_deal(player_score)
    dealer_score = dealer_deal(dealer_score)

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if player_score == 21:
        print(f"Dealer score: {dealer_score}, player score: {player_score}. You got BLACKJACK")
    else:
        next_move = 'y'
        while next_move == 'y':
            if player_score >= 21:
                break
            next_move = input("Type 'y' to get another card, type  'n' to pass: \n").lower()
            if next_move == 'n':
                break
            player_score = player_deal(player_score)
            print(f"Your cards are: {player_cards}, your score is: {player_score}")

        print(player_cards)
        print(f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}")
        while dealer_score < 17:
            dealer_score = dealer_deal(dealer_score)

    if player_score == 21:
        print(f"Dealer score: {dealer_score}, player score: {player_score}. You got BLACKJACK")

    if player_score > 21:
        print(
            f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}, player score: {player_score}, player cards: {player_cards}. You lose :(")
    elif dealer_score > 21:
        print(
            f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}, player score: {player_score}, player cards: {player_cards}. You win!")
    elif player_score > dealer_score:
        print(
            f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}, player score: {player_score}, player cards: {player_cards}. You win!")
    elif dealer_score > player_score:
        print(
            f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}, player score: {player_score}, player cards: {player_cards}. You lose :(")
    elif dealer_score == player_score:
        print(
            f"Dealer score: {dealer_score}, dealer cards: {dealer_cards}, player score: {player_score}, player cards: {player_cards}. Push")


while answer == 'y':
    blackjack()
    answer = input("Would you like to play another game? Press 'y' for yes, 'n' for no.")
    if answer != 'y':
        exit()
