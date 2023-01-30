#1.print Question.text (True or False)
#2.judge True or False Through writed Answer
#print All Question

#print All Question not complete 2023/01/30
class Question_Opearte:
    def __init__(self, question_bank):
        self.question_bank = question_bank
    
        for index,element in enumerate(question_bank):
            print(question_bank[index].text)


