class QuizBrain:
    def __init__(self,questionList):
        self.question_number = 0
        self.score = 0
        self.question_list = questionList
    def still_have_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
    def next_question(self):
        question_text = self.question_list[self.question_number].text
        question_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_answer,question_answer)
        
    def check_answer(self,userAnswer, correctAnswer):
        if userAnswer.lower() == correctAnswer.lower():
            self.score +=1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer is: {correctAnswer}")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
        