import random



def colors():
    return {"white": (255, 255, 255),
            "dark_orange": (201, 90, 10),
            "light_orange": (245, 127, 10),
            "dark_purple": (110, 60, 128),
            "light_purple": (145, 17, 171),
            }

def cards():
    return {'2_of_clubs': {'name': '2_of_clubs.png', 'value': 2},
            '2_of_diamonds': {'name': '2_of_diamonds.png', 'value': 2},
            '2_of_hearts': {'name': '2_of_hearts.png', 'value': 2},
            '2_of_spades': {'name': '2_of_spades.png', 'value': 2},
            '3_of_clubs': {'name': '3_of_clubs.png', 'value': 3},
            '3_of_diamonds': {'name': '3_of_diamonds.png', 'value': 3},
            '3_of_hearts': {'name': '3_of_hearts.png', 'value': 3},
            '3_of_spades': {'name': '3_of_spades.png', 'value': 3},
            '4_of_clubs': {'name': '4_of_clubs.png', 'value': 4},
            '4_of_diamonds': {'name': '4_of_diamonds.png', 'value': 4},
            '4_of_hearts': {'name': '4_of_hearts.png', 'value': 4},
            '4_of_spades': {'name': '4_of_spades.png', 'value': 4},
            '5_of_clubs': {'name': '5_of_clubs.png', 'value': 5},
            '5_of_diamonds': {'name': '5_of_diamonds.png', 'value': 5},
            '5_of_hearts': {'name': '5_of_hearts.png', 'value': 5},
            '5_of_spades': {'name': '5_of_spades.png', 'value': 5},
            '6_of_clubs': {'name': '6_of_clubs.png', 'value': 6},
            '6_of_diamonds': {'name': '6_of_diamonds.png', 'value': 6},
            '6_of_hearts': {'name': '6_of_hearts.png', 'value': 6},
            '6_of_spades': {'name': '6_of_spades.png', 'value': 6},
            '7_of_clubs': {'name': '7_of_clubs.png', 'value': 7},
            '7_of_diamonds': {'name': '7_of_diamonds.png', 'value': 7},
            '7_of_hearts': {'name': '7_of_hearts.png', 'value': 7},
            '7_of_spades': {'name': '7_of_spades.png', 'value': 7},
            '8_of_clubs': {'name': '8_of_clubs.png', 'value': 8},
            '8_of_diamonds': {'name': '8_of_diamonds.png', 'value': 8},
            '8_of_hearts': {'name': '8_of_hearts.png', 'value': 8},
            '8_of_spades': {'name': '8_of_spades.png', 'value': 8},
            '9_of_clubs': {'name': '9_of_clubs.png', 'value': 9},
            '9_of_diamonds': {'name': '9_of_diamonds.png', 'value': 9},
            '9_of_hearts': {'name': '9_of_hearts.png', 'value': 9},
            '9_of_spades': {'name': '9_of_spades.png', 'value': 9},
            '10_of_clubs': {'name': '10_of_clubs.png', 'value': 10},
            '10_of_diamonds': {'name': '10_of_diamonds.png', 'value': 10},
            '10_of_hearts': {'name': '10_of_hearts.png', 'value': 10},
            '10_of_spades': {'name': '10_of_spades.png', 'value': 10},
            'ace_of_clubs': {'name': 'ace_of_clubs.png', 'value': 10},
            'ace_of_diamonds': {'name': 'ace_of_diamonds.png', 'value': 11},
            'ace_of_hearts': {'name': 'ace_of_hearts.png', 'value': 11},
            'ace_of_spades': {'name': 'ace_of_spades.png', 'value': 11},
            'jack_of_clubs': {'name': 'jack_of_clubs.png', 'value': 10},
            'jack_of_diamonds': {'name': 'jack_of_diamonds.png', 'value': 10},
            'jack_of_hearts': {'name': 'jack_of_hearts.png', 'value': 10},
            'jack_of_spades': {'name': 'jack_of_spades.png', 'value': 10},
            'king_of_clubs': {'name': 'king_of_clubs.png', 'value': 10},
            'king_of_diamonds': {'name': 'king_of_diamonds.png', 'value': 10},
            'king_of_hearts': {'name': 'king_of_hearts.png', 'value': 10},
            'king_of_spades': {'name': 'king_of_spades.png', 'value': 10},
            'queen_of_clubs': {'name': 'queen_of_clubs.png', 'value': 10},
            'queen_of_diamonds': {'name': 'queen_of_diamonds.png', 'value': 10},
            'queen_of_hearts': {'name': 'queen_of_hearts.png', 'value': 10},
            'queen_of_spades': {'name': 'queen_of_spades.png', 'value': 10}
            }


# Game functions

CARDS = cards()


def deal():
    """Return a random card from the deck"""
    choice = random.choice(list(CARDS))
    return choice


def score(cards):
    """Add the card value from the dictionary to score list"""
    value = CARDS[cards[-1]]['value']
    return value


def keep_score(value):
    """Calculate score. Input is the score list."""
    if sum(value) == 21 and len(value) == 2:
        return 0
    while sum(value) > 21:
        if 11 in value:
            value.remove(11)
            value.append(1)
    return sum(value)


def compare(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"

    if player_score == dealer_score:
        return "Draw 🙃"
    elif dealer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif player_score > 21:
        return "You went over. You lose 😭"
    elif dealer_score > 21:
        return "Opponent went over. You win 😁"
    elif player_score > dealer_score:
        return "You win 😃"
    else:
        return "You lose 😤"
