from kivy.lang import Builder
from kivymd.app import MDApp

import main_screen
import random_screen
import data_loader

Builder.load_file( "main_screen.kv" )
Builder.load_file( "random_screen.kv" )


class QuizApp( MDApp ):
    def __init__( self, **kwargs ):
        super().__init__( **kwargs )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.questions = data_loader.questions


if __name__ == "__main__":
    QuizApp().run()