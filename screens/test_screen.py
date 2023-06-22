from abc import abstractmethod

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.app import App
import random

from data.colors import COLORS

Builder.load_file("screens/test_screen.kv")


class TestScreen(Screen):
    ALL_ANSWERS = ("answer_a", "answer_b", "answer_c", "answer_d", "answer_e")

    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        super().__init__(**kwargs)

        self.selected_answer = -1
        self.current_question = None

    def on_kv_post(self, base_widget):
        self.next_question()

    def next_question(self):
        self.current_question = random.choice(self.questions)
        self.update_labels()

    def update_labels(self):
        for answer in self.ALL_ANSWERS:
            self.ids[answer].reset()

        self.ids.contents.text = self.current_question.contents

        draw_list = [0, 1, 2, 3, 4]

        for answer in self.ALL_ANSWERS:
            index = random.choice(draw_list)
            text = self.current_question.answers[index]
            is_correct = index in self.current_question.correct_answers
            self.ids[answer].set_parameters(text, is_correct)
            draw_list.remove(index)

    def check_answer(self):
        for answer in self.ALL_ANSWERS:
            widget = self.ids[answer]
            if widget.selected and widget.is_correct:
                widget.set_color(COLORS["right"])

            elif widget.selected and not widget.is_correct:
                widget.set_color(COLORS["wrong"])

            elif (not widget.selected) and widget.is_correct:
                widget.set_color(COLORS["missed"])


        # selected_answer_label = None
        # correct_answer_label = None
        #
        # for answer in self.ALL_ANSWERS:
        #     if self.mark_condition(self.ids[answer]):
        #         correct_answer_label = self.ids[answer]
        #
        #     if self.ids[answer].selected:
        #         selected_answer_label = self.ids[answer]
        #
        # if self.check_condition() and selected_answer_label is not None:
        #     selected_answer_label.set_color(COLORS["right"])
        #
        # else:
        #     if selected_answer_label is not None:
        #         selected_answer_label.set_color(COLORS["wrong"])
        #
        #     correct_answer_label.set_color(COLORS["right"])
    def clear_selection(self):
        for answer in self.ALL_ANSWERS:
            self.ids[answer].set_color()
            self.ids[answer].selected = False

    @abstractmethod
    def check_condition(self):
        pass

    @abstractmethod
    def mark_condition(self, answer: 'Answer'):
        pass
