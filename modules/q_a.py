"""
Init Q & A Module
"""


class Answers:
    """
    Class to handle answer provided by user
    """

    def __init__(self, answer):
        self.answer = answer

    def __str__(self):
        return str(self.answer)

    def check_answer(self):
        """
        Check if answer is valid
        """
        if str(self) not in ('help', 'skip', 'yes', 'no'):
            return f"{str(self)} is not Valid!!!"
        else:
            return f"{str(self)} is Valid :)"


class Help(Answers):
    """
    Class to handle help answer
    """

    def run_replay(self):
        """
        Return replay
        """


question = Answers(input("Whats your answer? "))

help_answer = Help(question)
print(help_answer)
answer_check = help_answer.check_answer()
print(answer_check)
