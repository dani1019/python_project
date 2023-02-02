from question_model import Question
from data import question_data
from quiz_brain import Question_Opearte

question_bank = []  
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)


quiz_object = Question_Opearte(question_bank)
quiz_object.print_question()


