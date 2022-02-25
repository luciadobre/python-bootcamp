import math

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(alphabet[19])
#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction = 'decode'
#text = input("Type your message:\n").lower()
text = ("klmnopqrstuvwxyzabcdefghij").lower()
#shift = int(input("Type the shift number:\n"))
shift = 140

def encrypt(text, shift):
  final_text = []
  for i in text:
    if i in alphabet:
      #print(f"I is: {i} and its position is: {alphabet.index(i)}")
      second_index = alphabet.index(i) + shift
      if second_index > len(alphabet):
        #print(f"Second index is: {second_index}")
        place = alphabet.index(i)+shift
        #print(f"Place is: {place}")
        trunc = math.trunc(place/len(alphabet))
        #print(f"Floor is: {floor}")
        final_index = (place - trunc*len(alphabet))-1
        #print(f"Final index is: {final_index}")
        second_index = final_index+1
      final_text.append(alphabet[second_index])
    else:
      final_text.append(i)
  printed_text = ''.join(final_text)
  print(printed_text)

def decrypt(text, shift):
  final_text = []
  for i in text:
    if i in alphabet:
      #print(f"I is: {i} and its position is: {alphabet.index(i)}")
      second_index = alphabet.index(i) - shift
      #print(f"Second index is: {second_index}")
      if second_index < 0:
        truncs = math.trunc(second_index/len(alphabet))
        #print(f"Trunc is: {truncs} {second_index}/{len(alphabet)}={second_index/len(alphabet)}")
        diff = shift + len(alphabet)*truncs
        #print(f"Diff is: {diff}")
        place = alphabet.index(i) - diff
        #print(f"Place is: {place}")
        final_index = len(alphabet) + place
        #print(f"Final index is: {final_index}")
        second_index = final_index
      if second_index == 26:
        second_index = 0
      final_text.append(alphabet[second_index])
      #print(final_text)
    else:
      final_text.append(i)
  printed_text = ''.join(final_text)
  print(printed_text)

if direction == 'encode':
  encrypt(text, shift)
else:
  decrypt(text, shift)