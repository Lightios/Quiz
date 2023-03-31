from kivy.properties import StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.app import App

import random

COLORS = {
    "selected": (0, 1, 1, 1),
    "right": (0, 1, 0, 1),
    "wrong": (1, 0, 0, 1),
}


class RandomScreen( Screen ):
    ALL_ANSWERS = ("answer_a", "answer_b", "answer_c", "answer_d")

    def __init__( self, **kwargs ):
        self.app = App.get_running_app()
        super().__init__( **kwargs )

        self.selected_answer = -1
        self.current_question = None

        Clock.schedule_once( lambda x: self.update_labels() )

    def update_labels( self ):
        for answer in self.ALL_ANSWERS:
            self.ids[ answer ].set_color()

        self.current_question = random.choice( self.app.questions )

        self.ids.contents.text = self.current_question.contents

        draw_list = [0, 1, 2, 3]

        for answer in self.ALL_ANSWERS:
            index = random.choice( draw_list )
            text = self.current_question.answers[ index ]
            self.ids[ answer ].set_text( text )
            self.ids[ answer ].answer_index = index
            draw_list.remove( index )

    def color_label( self, to_color: str ):
        if to_color == "a":
            widget = self.ids.answer_a
        elif to_color == "b":
            widget = self.ids.answer_b
        elif to_color == "c":
            widget = self.ids.answer_c
        else:
            widget = self.ids.answer_d

        for answer in self.ALL_ANSWERS:
            self.ids[ answer ].set_color()
            self.ids[ answer ].selected = False

        widget.set_color( COLORS["selected"] )
        widget.selected = True
        self.selected_answer = widget.answer_index

    def check_answer( self ):
        selected_answer_label = None
        correct_answer_label = None

        for answer in self.ALL_ANSWERS:
            if self.ids[ answer ].answer_index == 0:
                correct_answer_label = self.ids[ answer ]

            if self.ids[ answer ].selected:
                selected_answer_label = self.ids[ answer ]

        if self.selected_answer == 0 and selected_answer_label is not None:
            selected_answer_label.set_color( COLORS["right"] )

        else:
            if selected_answer_label is not None:
                selected_answer_label.set_color( COLORS["wrong"] )

            correct_answer_label.set_color( COLORS["right"] )


class Answer( RelativeLayout ):
    letter = StringProperty()

    def __init__(self, **kwargs):
        super().__init__( **kwargs )
        self.selected = False
        self.answer_index = -1

    def set_color(self, color=(1, 1, 1, 1)):
        """
        sets label text color
        :param color: RGBA tuple, default is (1, 1, 1, 1) (white)
        :return: None
        """
        self.ids.label.color = color

    def set_text( self, text: str ):
        self.ids.label.text = text

