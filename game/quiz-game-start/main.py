from question_model import Question
from data import question_data

question_bank = []
for data in question_data:
    question_bank.append(Question(data["text"],data["answer"]))

print(question_bank)