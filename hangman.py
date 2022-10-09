import random
import string


HANGMAN_PICS = ['''
  3.   +---+
  4.       |
  5.       |
  6.       |
  7.      ===''', '''
  8.   +---+
  9.   O   |
 10.       |
 11.       |
 12.      ===''', '''
 13.   +---+
 14.   O   |
 15.   |   |
 16.       |
 17.      ===''', '''
 18.   +---+
 19.   O   |
 20.  /|   |
 21.       |
 22.      ===''', '''
 23.   +---+
 24.   O   |
 25.  /|\  |
 26.       |
 27.      ===''', '''
 28.   +---+
 29.   O   |
 30.  /|\  |
 31.  /    |
 32.      ===''', '''
 33.   +---+
 34.   O   |
 35.  /|\  |
 36.  / \  |
 37.      ===''']

words = {1: "ant", 2: "lion", 3: "cougar", 4: "horse", 5: "monkey", 6: "lama", 7: "tiger", 8: "panda", 9: "sheep"}
computer_word = list(words[random.randint(1, 9)])
print(computer_word)
mystery = []
for i in computer_word:
    mystery.append("_")


while "_" in mystery:
    def trying():
        letter_try = input("Guess the letter\n").lower()
        for position in range(len(computer_word)):
            letter = computer_word[position]
            if letter == letter_try:
                mystery[position] = letter
        if letter_try not in computer_word:
            print("Ops, wrong...\n\n")
            print(HANGMAN_PICS[0])
            HANGMAN_PICS.pop(0)

    print(f"{''.join(mystery)}\n\n")
    if not HANGMAN_PICS:
        print("You died")
        break

    trying()


if mystery == computer_word:
    print("Congrats, you won!!!!!")
