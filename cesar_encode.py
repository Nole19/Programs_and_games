import string


while True:
    def encode():
        word = input("What is your word?\n")
        word = word.lower()
        shift_number = input("Choose a shift number\n")
        all_letters = list(string.ascii_letters)
        new_word = []
        for i in word:
            new_word.append(all_letters[all_letters.index(i) + int(shift_number)])
            if len(new_word) == len(word):
                encode_result = (''.join(new_word))
                print(encode_result.lower())


    def decode():
        word = input("What is your word?\n")
        word = word.lower()
        shift_number = input("Choose a shift number\n")
        all_letters = list(string.ascii_letters)
        new_word = []
        for i in word:
            new_word.append(all_letters[all_letters.index(i) - int(shift_number)])
            if len(new_word) == len(word):
                decode_result = (''.join(new_word))
                print(decode_result.lower())


    encode_decode = input("What do you want to do? Put 1 for Encode and 2 to  Decode\n")
    if encode_decode == "1":
        encode()
    elif encode_decode == "2":
        decode()
    else:
        print(encode_decode)
    decision = input("Do you want to try again? Put y for yes or n for not\n")
    print(decision)
    if decision == "y" or decision == "yes":
        continue
    else:
        break

