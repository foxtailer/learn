class QuizBrain:
    def __init__(self, qeustions) -> None:
        self.question_number = 0
        self.score = 0
        self.current_answer = ""
        self.question_list = qeustions
    
    def still_has_questions(self):
        # if len(self.question_list) > self.question_number:
        #     return True
        # return False
        # ========
        # return len(self.question_list) > self.question_number
        # ========
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("You've complete the test.")
            print(f"Your final score is {self.score}/{len(self.question_list)}")

    def next_question(self):
        self.current_answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.question_number += 1

    def check_answer(self):
        right_answer = self.question_list[self.question_number - 1].answer.lower()
        if self.current_answer.lower() == right_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"Yous score is {self.score}/{self.question_number}")
        print(f"Right answer is {right_answer.capitalize()}")
        print()
        print()
