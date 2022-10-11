from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the secret auction program!")
all_bits = {}


def info():
    name = input("What is your name?: ")
    bid = input("How much you can bid: ")
    all_bits[name] = int(bid)
    other = input("Are there any other bidders? Type Yes or No?\n")
    if other == "Yes":
        clear()
        info()
    elif other == "No" or "no":
        print(max(all_bits, key=all_bits.get))
    else:
        "You should choose Yes or No"
        print(other)


info()
