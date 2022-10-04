import random
import string


print("Welcome to the password Generator!!!!!!!!!!!!!!!!!!!!!!!!!\n")
letters = input("How many letters do you prefer?\n")
symbols = input("How many symbols do you prefer?\n")
numbers = input("How many numbers do you prefer?\n")
all_letters = list(string.ascii_letters)
punctuation = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
digits = list(string.digits)
password = []
for i in range(0, int(letters)):
    password.append(random.choice(all_letters))
for i in range(0, int(symbols)):
    password.append(random.choice(punctuation))
for i in range(0, int(numbers)):
    password.append(random.choice(digits))
password_string = ""
for x in password:
    password_string += x
your_password = ''.join(random.sample(password_string, len(password_string)))
print(your_password)


