from kivy.clock import Clock
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

import main_screen
from screens import test_screen, abc_screen, categories_screen
import data_loader

Builder.load_file( "main_screen.kv" )
Builder.load_file( "screens/test_screen.kv" )


class QuizApp( MDApp ):
    TYPES = ["abc", "categories"]

    def __init__( self, **kwargs ):
        super().__init__( **kwargs )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.questions = data_loader.questions


if __name__ == "__main__":
    QuizApp().run()
