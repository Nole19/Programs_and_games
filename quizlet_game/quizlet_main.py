from question_model import Question
from data import question_data
from brain import Logic


question_bank = []

for i in question_data:
    question = Question(i["question"], i["correct_answer"])
    question_bank.append(question)


quiz = Logic(question_bank)
while quiz.still_question():
    quiz.next_question()
    quiz.check_the_answer()



