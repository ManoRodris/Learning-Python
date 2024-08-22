class QuizBrain(object):

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        amount_of_questions = len(self.question_list)
        return self.question_number < amount_of_questions

    def check_answer(self, answer, correct_question):
        if answer == correct_question:
            print("You're right!")
            self.score += 1
        else:
            print("You're wrong.")
        print(f"The correct answer was {correct_question}")
        print(f"Your current scores is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        accessing_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {accessing_question.text} (True/False)?:")
        correct_answer = accessing_question.answer
        self.check_answer(user_answer, correct_answer)
