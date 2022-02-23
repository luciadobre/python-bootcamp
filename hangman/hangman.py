import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
end_of_game = False
word_length = len(chosen_word)
lives = 6

print(hangman_art.logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(len(chosen_word)):
  display += "_"

print(' '.join(display))

#Replace guessed letter
while not end_of_game:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f"You already guessed the {guess} letter.")

  for i in range(word_length):
    letter = chosen_word[i]
    if letter == guess:
        display[i] = letter
        print(' '.join(display))
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You lose.")

  if "_" not in display:
    end_of_game = True
    print("You win.")

  print(hangman_art.stages[lives])

