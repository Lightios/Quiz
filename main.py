from kivy.lang import Builder
from kivymd.app import MDApp

import main_screen
import random_screen

Builder.load_file( "main_screen.kv" )
Builder.load_file( "random_screen.kv" )


class QuizApp( MDApp ):
    def __init__( self, **kwargs ):
        super().__init__( **kwargs )

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"

        self.data = []

        with open( "data.txt", encoding="utf-8" ) as file:
            file_content = file.readlines()

        for i in range( len( file_content ) ):
            file_content[ i ] = file_content[ i ].replace( "\n", " " )

        i = 0
        length = len( file_content )
        while i < length - 5:
            content = ""
            while not file_content[ i ].startswith("odp:"):
                content += file_content[ i ]
                i += 1

            question = Question( content, file_content[ i ], file_content[ i + 1 ], file_content[ i + 2 ], file_content[ i + 3 ] )
            self.data.append( question )
            i += 4


class Question:
    def __init__( self, contents, a, b, c, d ):
        self.contents = contents

        a = a.replace( "odp: ", "" )
        self.answers = [a, b, c, d]


if __name__ == "__main__":
    QuizApp().run()
