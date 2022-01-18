from traceback import print_tb
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question = Question(data['text'], data['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
    quiz.check_answer()