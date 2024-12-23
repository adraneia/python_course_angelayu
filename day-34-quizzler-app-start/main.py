from question_model import Question
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface
from data import data

#from data import question_data


# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

# quiz = QuizBrain(question_bank)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")
##------------------------------------------------------------------------






# response = requests.get("https://opentdb.com/api.php?amount=10&category=20&type=boolean")
# response.raise_for_status()
# data = response.json()

#print(data)
# print(data["results"])
# print(data["results"][1])
# print(data["results"][1]["question"])

question_bank = []
for question in data["results"]:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
