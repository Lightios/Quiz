from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.app import App

import random


class RandomScreen( Screen ):
    def __init__( self, **kwargs ):
        self.app = App.get_running_app()
        super().__init__( **kwargs )

        self.selected_answer = None
        self.current_question = None

        Clock.schedule_once( lambda x: self.update_labels() )

    def update_labels( self ):
        self.ids.answer_a.text_color = (1, 1, 1, 1)
        self.ids.answer_b.text_color = (1, 1, 1, 1)
        self.ids.answer_c.text_color = (1, 1, 1, 1)
        self.ids.answer_d.text_color = (1, 1, 1, 1)

        self.current_question = random.choice( self.app.data )

        self.ids.contents.text = self.current_question.contents

        draw_list = [0, 1, 2, 3]

        for answer in ( "answer_a", "answer_b", "answer_c", "answer_d" ):
            index = random.choice( draw_list )
            self.ids[ answer ].text = self.current_question.answers[ index ]
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

        self.ids.answer_a.text_color = (1, 1, 1, 1)
        self.ids.answer_b.text_color = (1, 1, 1, 1)
        self.ids.answer_c.text_color = (1, 1, 1, 1)
        self.ids.answer_d.text_color = (1, 1, 1, 1)

        widget.text_color = (0, 1, 1, 1)
        self.selected_answer = self.current_question.answers.index( widget.text )

    def check_answer( self ):
        selected_answer_label = None
        correct_answer_label = None

        for answer in ( "answer_a", "answer_b", "answer_c", "answer_d" ):
            if self.ids[ answer ].text == self.current_question.answers[ 0 ]:
                correct_answer_label = self.ids[ answer ]

            if self.ids[ answer ].text_color == [0, 1, 1, 1]:
                selected_answer_label = self.ids[ answer ]

        if self.selected_answer == 0:
            selected_answer_label.text_color = (0, 1, 0, 1)

        else:
            if selected_answer_label is not None:
                selected_answer_label.text_color = (1, 0, 0, 1)

            correct_answer_label.text_color = (0, 1, 0, 1)