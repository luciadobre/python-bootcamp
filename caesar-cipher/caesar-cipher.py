import math
import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#direction = 'decode'
text = input("Type your message:\n").lower()
#text = ("Ifmmp hvzt, ipx bsf zpv??!!11").lower()
shift = int(input("Type the shift number:\n"))
#shift = 1

print(logo.logo)

def caesar(text, shift, direction):
  final_text = []
  for i in text:
    if i in alphabet:
      #print(f"I is: {i} and its position is: {alphabet.index(i)}")
      difference = shift%len(alphabet)
      if direction == 'encode':
        difference *= -1
      second_index = alphabet.index(i) - difference
      #print(f"Second index is: {second_index}")
      if second_index >= len(alphabet):
        final_index = second_index%len(alphabet)
        second_index = final_index
      #print(f"Final index is: {second_index}")
      final_text.append(alphabet[second_index])
    else:
      final_text.append(i)
    printed_text = ''.join(final_text)
  print(f'The {direction}d text is "{printed_text}"')

answer = 'yes'

while answer == 'yes':
  caesar(text, shift, direction)
  answer = input("Type 'yes' if you would like to go again. Type 'no' to exit\n").lower()
else:
  exit()