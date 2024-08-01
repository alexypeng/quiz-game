# Simple quiz game created by Alexander Peng on 2024/07/31.
# Makes use of Object-Oriented Programming to organize and run the program.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question = Question(question["question"], question["correct_answer"])
    question_bank.append(question)

num_q = int(input("How many questions? (1-50): "))

quiz = QuizBrain(question_bank, num_q)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Final score: {quiz.score}/{quiz.question_num}")
