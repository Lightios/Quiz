from screens.test_screen import TestScreen
from screens.abc_loader import questions
from widgets.answer import Answer

class ABCScreen(TestScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.questions = questions

    def check_condition(self):
        return self.selected_answer == 0

    def mark_condition(self, answer: Answer):
        return answer.answer_index == 0
