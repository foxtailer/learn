from question_model import Question
from data import get_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in get_data():
    question_text = question[0]
    question_answer = question[1]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

ui = QuizInterface(quiz)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
