"""
Module that implements the quizzing and answering functionality
"""


class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        if self.question_number > (len(self.question_list)-1):
            return False
        else:
            return True

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?:  ").title()
        self.answer = user_answer
    
    def check_answer(self):
        question = self.question_list[self.question_number - 1]
        if self.answer == question.answer:
            self.score += 1
            print("You got it right!\n")
        else:
            print("That's wrong\n")
        print(f"The corrct answer was {question.answer}\n")
        print(f"Your current score is {self.score}/{self.question_number}\n")