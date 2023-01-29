#1.print Question.text (True or False)
#2.judge True or False Through writed Answer
#print All Question

#print All Question not complete 2023/01/30
class Question_Opearte:
    def __init__(self, question_data):
        self.question_data = question_data
    
    for index,question in enumerate(question_data):
        q_text = question["text"]
        q_answer = question["answer"]

        print(question["text"][index])



