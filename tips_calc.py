print("Welcome to the tip calculator")


def check_for_one():
    total = input("What was the total bill?\n")
    people = input("How many people split the bill?\n")
    percentage = input("What percentage you'll choose? 10,12 or 15?\n")
    percentage_choose = ("10", "12", "15")
    if percentage in percentage_choose:
        full_payment = float(percentage) / 100 * float(total) + float(total)
        for_one = full_payment // float(people)
        print("$" + str(for_one))
    else:
        print("Choose normal tips)")


check_for_one()
