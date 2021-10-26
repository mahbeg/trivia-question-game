import html



class QuizBrain():
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_text = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        correct_text = self.current_question.text
        correct_answer = self.current_question.answer
        self.question_number += 1
        return correct_text


    # def true_button(self, correct_answer):
    #     if correct_answer.lower() == True:
    #         self.score += 1
    #
    # def false_button(self, correct_answer):
    #     if correct_answer.lower() == False:
    #         self.score += 1


