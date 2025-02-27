# TODO: checking if the answer was correct

class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        choice = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} (True/False)?: ")
        self.question_number += 1
        self.check_answer(choice, self.question_list[self.question_number - 1].answer)
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, choice, answer):
        if choice.lower() == answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")
