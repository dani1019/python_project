#1.print Question.text (True or False)
#2.judge True or False Through writed Answer
#print All Question

#print All Question not complete 2023/01/30
class Question_Opearte:
    def __init__(self, question_bank):
        self.question_bank = question_bank
        self.correct_number = 0
        self.len_question_bank = len(question_bank) - 1

    def print_question(self):
        print(f"1111111 {self.question_bank}");
        for index,element in enumerate(self.question_bank):
            q_text = self.question_bank[index].text
            q_answer = self.question_bank[index].answer

            print(f"q_text: {q_text}")
            print(f"q_answer: {q_answer}")
            
            #print question and require answer to user
            select_boolean= input(f"Q.{index + 1}: {q_text} (True/False)?: ")
            #check whether answer is correct
            self.check_answer_correct(select_boolean,q_answer)

            #print result
            if index == self.len_question_bank:
                self.print_result()
    
    def check_answer_correct(self,select_boolean,q_answer):
        if select_boolean == q_answer:
            self.correct_number += 1
    
    def print_result(self):
        print(f"You are correct {self.correct_number}")
    



            
            


