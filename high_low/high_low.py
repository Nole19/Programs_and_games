import random


list_of_people = [
    {"Name": "Ronaldo",
     "Followers": 111,
     "Profession": "football player",
     "Country": "Portugal"},
    {"Name": "Ann",
     "Followers": 19911,
     "Profession": "gangster",
     "Country": "Russia"},
    {"Name": "Kate",
     "Followers": 235,
     "Profession": "lox",
     "Country": "France"},
    {"Name": "Carlsen",
     "Followers": 5671,
     "Profession": "chess player",
     "Country": "Norway"},
     ]


def del_people_from_list(person):
    for people in list_of_people:
        if people.get("Name") == person:
            list_of_people.remove(people)
            break


def get_random_human():
    second_men = (list_of_people[random.randint(0, len(list_of_people)-1)]["Name"])
    return second_men


def get_the_info(name):
    for people in list_of_people:
        if people.get("Name") == name:
            return people["Profession"], people["Country"], people["Followers"]


first = get_random_human()
profession_1 = get_the_info(first)
del_people_from_list(first)
second = get_random_human()
profession_2 = get_the_info(second)
del_people_from_list(first)
points = 0
while list_of_people:
    print(f"Compare A:{first}, {profession_1[0]}, from {profession_1[1]}")
    print(f"Against B:{second}, {profession_2[0]}, from {profession_2[1]}")
    your_choice = input("Who has more followers? Type 'A' or 'B': ")
    if profession_1[2] > profession_2[2] and your_choice == "A":
        points += 1
        print(f"You're right! Current score: {points}")
        second = get_random_human()
        profession_2 = get_the_info(second)
        del_people_from_list(second)
    elif profession_1[2] < profession_2[2] and your_choice == "B":
        points += 1
        print(f"You're right! Current score: {points}")
        first = second
        profession_1 = get_the_info(first)
        second = get_random_human()
        profession_2 = get_the_info(second)
        del_people_from_list(second)
    else:
        print(f"Sorry, that's wrong. Final score: {points}")
        break



