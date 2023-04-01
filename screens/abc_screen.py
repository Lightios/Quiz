from screens.test_screen import TestScreen, Answer


class ABCScreen( TestScreen ):
    def check_condition( self ):
        return self.selected_answer == 0

    def mark_condition( self, answer: Answer ):
        return answer.answer_index == 0
