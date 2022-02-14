import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

while True:
    try:
       print(game_images[choice])
    except IndexError:
        sys.exit("Oops!  That was no valid number.  Try again...")

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])


if choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and choice == 2:
  print("You lose")
elif computer_choice > choice:
  print("You lose")
elif choice > computer_choice:
  print("You win!")
elif computer_choice == choice:
  print("It's a draw")