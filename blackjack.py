import random
from replit import clear
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
pull = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
decision = input("Do you want to play a game? Type 'y' or 'n': ")


def add_card_to_you():
    return your_cards.append(random.choice(pull))


def add_comp_card():
    return computer_cards.append(random.choice(pull))


while decision == "y":
    print(logo)


    def checking():
        print(f"Your cards: {your_cards}, your final score: {sum(your_cards)}")
        print(f"Computer final hand: {computer_cards}, final score: {sum(computer_cards)}")
        if sum(your_cards) > 21:
            print("You lose")
        elif sum(computer_cards) > 21:
            print("You won")
        elif sum(your_cards) > sum(computer_cards):
            print("You won :)")
        elif sum(your_cards) == sum(computer_cards):
            print("Draw")
        else:
            print("Computer won :(")
    your_cards = []
    computer_cards = []
    for i in range(2):
        add_card_to_you()
        add_comp_card()
    while sum(computer_cards) < 17:
        add_comp_card()
        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards.remove(11)
            computer_cards.append(1)
    print(f"Computer's first card is {computer_cards[0]}")
    print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
    add_or_not = input("Do you want to take one more card? Type 'y' or 'n': ")
    while add_or_not == "y":
        add_card_to_you()
        if 11 in your_cards and sum(your_cards) > 21:
            your_cards.remove(11)
            your_cards.append(1)
        print(f"Your cards: {your_cards}, current score: {sum(your_cards)}")
        if sum(your_cards) > 21:
            print("You lose")
            break
        else:
            add_or_not = input("Do you want to take one more card? Type 'y' or 'n': ")
    checking()
    clear()
    decision = input("Do you want to play a game? Type 'y' or 'n': ")
