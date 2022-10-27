class Logic:
    def __init__(self, question_):
        self.number_of_question = 0
        self.question_list = question_
        self.answer = ""
        self.current_score = 0

    def still_question(self):
        if self.number_of_question < len(self.question_list):
            return True
        else:
            print(f"Your final score {self.current_score}/{self.number_of_question}")

    def next_question(self):
        current_question = self.question_list[self.number_of_question]
        self.number_of_question += 1
        self.answer = input(f"Q.{self.number_of_question}: {current_question.text} (True/False): ")

    def check_the_answer(self):
        if self.answer == "True":
            self.current_score += 1
            print("You got it right! The correct answer was: True")
            print(f"Your current score is {self.current_score}/{self.number_of_question}")
        elif self.answer == "False":
            self.current_score += 1
            print("You got it right! The correct answer was: False")
            print(f"Your current score is {self.current_score}/{self.number_of_question}")
        else:
            print(f"That's wrong. The correct answer was: True.")
            print(f"Your current score is {self.current_score}/{self.number_of_question}")

