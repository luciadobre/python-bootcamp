import os
import pygame as pygame
from back_end import *
from constants import *
import sys
import time
pygame.init()

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 850

PLAYER_SCORE_X = 10
PLAYER_SCORE_Y = 10
DEALER_SCORE_X = 1000
DEALER_SCORE_Y = 10

MAIN_FILE_PATH = os.path.dirname(__file__)
IMAGES_FOLDER = os.path.join(MAIN_FILE_PATH, "images")
CARDS_FOLDER = os.path.join(IMAGES_FOLDER, "cards")

pygame.init()
SURFACE = pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.RESIZABLE
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Title and icon
pygame.display.set_caption("Blackjack")
icon = pygame.image.load("images/icon.png")

clock = pygame.time.Clock()

background_image = pygame.image.load("images/table_top.png")
background_image = pygame.transform.scale(background_image, (1200, 850))

# Cursor
pygame.mouse.set_cursor(*pygame.cursors.arrow)

font = pygame.font.Font(None, 32)


def main():
    running = True
    # Draw background image
    window.fill((0, 0, 0))
    window.blit(background_image, (0, 0))
    pygame.display.set_icon(icon)

    def render_player_score(score):
        show_score = font.render('Player score: ' + str(score), True, (255, 255, 255))
        window.blit(show_score, (PLAYER_SCORE_X, PLAYER_SCORE_Y))

    def render_dealer_score(score):
        show_score = font.render('Dealer score: ' + str(score), True, (255, 255, 255))
        window.blit(show_score, (DEALER_SCORE_X, DEALER_SCORE_Y))

    def render_message(message):
        show_message = font.render(str(message), True, (255, 255, 255))
        window.blit(show_message, (DEALER_SCORE_X, DEALER_SCORE_Y))

    # Game
    player_cards = []
    dealer_cards = []
    player_value = []
    dealer_value = []

    for _ in range(2):
        player_cards.append(deal())
        player_value.append(score(player_cards))
        dealer_cards.append(deal())
        dealer_value.append(score(dealer_cards))

    player_score = keep_score(player_value)
    dealer_score = keep_score(dealer_value)

    print(
        f"Player cards: {player_cards}, Player score:{player_score} Dealer cards: {dealer_cards}, Dealer score: {dealer_score}")
    render_player_score(player_score)
    render_dealer_score(dealer_score)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Player cards: {player_cards}, Player score:{player_score} Dealer cards: {dealer_cards}, Dealer score: {dealer_score}")
                window.blit(background_image, (0, 0))
                render_player_score(player_score)
                render_dealer_score(dealer_score)
                break

        clock.tick(60)
        pygame.display.flip()


main()

pygame.quit()
