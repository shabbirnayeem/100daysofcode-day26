from question_model import Question
from data import question_data
from quiz_brain import QuizBrian

question_bank = []
for question in question_data:
    # print(question['question'])
    # print(question['correct_answer'])
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
            ##  or  ##
    #  question_bank.append(Question(question['text'], question['answer']))


quiz = QuizBrian(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've complete the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")