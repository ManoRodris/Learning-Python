from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for questions in question_data[0]["results"]:
    question_bank += [Question(questions["question"], questions["correct_answer"])]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    if not quiz.still_has_questions():
        print("You've completed the quiz")
        print(f"Your final score was {quiz.score}/{quiz.question_number}")