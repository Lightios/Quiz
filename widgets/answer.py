from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout

from data.colors import COLORS

Builder.load_file('widgets/answer.kv')

class Answer(RelativeLayout):
    letter = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.selected = False
        self.answer_index = -1
        self.is_correct = False

    def set_color(self, color=(1, 1, 1, 1)):
        """
        sets label text color
        :param color: RGBA tuple, default is (1, 1, 1, 1) (white)
        :return: None
        """
        self.ids.label.color = color

    def set_parameters(self, text: str, is_correct: bool):
        self.ids.label.text = text
        self.is_correct = is_correct

    def reset(self):
        self.set_color()
        self.is_correct = False
        self.selected = False

    def on_press(self):
        self.selected = not self.selected

        if self.selected:
            self.set_color(COLORS["selected"])
        else:
            self.set_color()