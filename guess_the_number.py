import random


logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
print("Welcome to the Number Guessing Mode!")
answered_number = random.randint(0, 100)
choose_level = input(f"Choose a difficulty. Type 'easy' or 'hard': ")
if choose_level == "easy":
    attempts = 10
else:
    attempts = 5

while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    your_supposition = input("Make a guess: ")
    if int(your_supposition) != answered_number:
        attempts -= 1
        if int(your_supposition) > answered_number:
            print("Too much\nGuess again.")
        elif int(your_supposition) < answered_number:
            print("Too low\nGuess again.")
        elif attempts == 0:
            print("You are out of attempts(")

    else:
        print("Good job! That's right)")
        break








