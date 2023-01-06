from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

test_001 = QuizBrain(question_bank)

while test_001.still_has_questions():
    test_001.next_question()
    test_001.check_answer()