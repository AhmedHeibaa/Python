from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
# q1 = Question(question_data['text'],bool)
question_bank = []
for dict in question_data:
    question_bank.append(Question(dict['text'],dict['answer']))
    
# print(question_bank[1].text)
# print(question_bank[1].answer)
quiz = QuizBrain(question_bank)

while quiz.still_have_question():
    quiz.next_question()
print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")