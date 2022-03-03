import random

cards = {
    "2_of_clubs": 2,
    "2_of_diamonds": 2,
    "2_of_hearts": 2,
    "2_of_spades": 2,
}
whole_deck = []


def build_deck(decks):
    for i in range(decks):
        whole_deck.append(cards)

decks_number = 4
build_deck(decks_number)

print(f"The deck is: {whole_deck}")

game_on = True
player_cards = []
dealer_cards = []

def player_deal():
    """Give player one card"""
    player_cards.append(random.choice(cards))

def dealer_deal():
    """Give dealer one card"""
    dealer_cards.append(random.choice(cards))

def blackjack():
    player_score = 0
    dealer_score = 0

    player_deal()
    dealer_deal()
    player_deal()
    dealer_deal()

    for value in player_cards:
        player_score += value

    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(dealer_cards)

if game_on:
    blackjack()


