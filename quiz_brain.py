# Asks user for next question, checks if answer is right, checks if the user is at the end of the quiz
import random


class QuizBrain:

    def __init__(self, questions_list, num_questions):
        """Initializes the QuizBrain class."""
        self.question_num = 0
        self.questions_list = questions_list
        self.score = 0
        self.num_questions = num_questions
        self.questions_asked = []

    def still_has_questions(self):
        """Checks whether there are any questions remaining in the quiz."""
        return self.question_num < self.num_questions

    def next_question(self):
        """Asks the next question. Ensures that questions are not repeated"""
        question = self.questions_list[random.randint(0, 49)]
        while question in self.questions_asked:
            question = self.questions_list[random.randint(0, 49)]
        self.questions_asked.append(question)
        self.question_num += 1
        user_ans = input(f"Q{self.question_num}. {question.text} Your answer: ")
        self.check_answer(user_ans, question.answer)

    def check_answer(self, user_answer, c_answer):
        """Checks whether the user's answer is correct."""
        if user_answer.lower() == c_answer.lower():
            print("Congrats! You got the right answer!")
            self.score += 1
        else:
            print("Sorry, wrong answer!")
            print(f"The correct answer is {c_answer}.")
        print(f"Your current score is {self.score}/{self.question_num}.")
        print("\n")
