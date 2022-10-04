import random


print("Welcome to amazing game!)")
your_choice = input("What do you choose? Rock, Paper or Scissors?)\n")
truce_choice = ["Rock", "Paper", "Scissors"]
random = random.randint(0, 2)
computer_choice = truce_choice[random]
if your_choice not in truce_choice:
    print("Choose Paper, Paper or Scissors")
print("Computer choose: " + computer_choice)
if your_choice == computer_choice:
    print("Draw")
if your_choice == "Paper" and computer_choice == "Rock":
    print("You won!)")
if your_choice == "Scissors" and computer_choice == "Paper":
    print("You won!)")
if your_choice == "Rock" and computer_choice == "Scissors":
    print("You won!)")
if computer_choice == "Rock" and your_choice == "Scissors":
    print("Sorry<>Looser:)")
if computer_choice == "Scissors" and your_choice == "Paper":
    print("Sorry<>Looser:)")
if computer_choice == "Paper" and your_choice == "Rock":
    print("Sorry<>Looser:)")
