from kivy.properties import StringProperty, ColorProperty
from kivymd.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard

PROPER_POS = {"center_x": 0.5, "center_y": 0.4}
HIDE_POS = {"center_x": -2}


class MainScreen( Screen ):
    def __init__( self, **kwargs ):
        self.app = App.get_running_app()

        super().__init__( **kwargs )

    def choose_screen( self, screen: str ):
        self.app.root.ids.screen_manager.current = screen

    def select( self, select_button ):
        for i in range( 3 ):
            self.ids[ f"select_{i}" ].color = "white"
        select_button.color = "orange"

        if select_button.icon == "alphabetical":
            self.ids.abc_options.pos_hint = PROPER_POS
            self.ids.translation_options.pos_hint = HIDE_POS
            self.ids.category_options.pos_hint = HIDE_POS
        elif select_button.icon == "translate-variant":
            self.ids.abc_options.pos_hint = HIDE_POS
            self.ids.translation_options.pos_hint = PROPER_POS
            self.ids.category_options.pos_hint = HIDE_POS
        elif select_button.icon == "shape-outline":
            self.ids.abc_options.pos_hint = HIDE_POS
            self.ids.translation_options.pos_hint = HIDE_POS
            self.ids.category_options.pos_hint = PROPER_POS


class SelectButton( MDCard ):
    icon = StringProperty()
    color = ColorProperty()

    def select(self):
        self.parent.select( self )


class ABCOptions( MDCard ):
    pass


class TranslationOptions( MDCard ):
    pass


class CategoryOptions( MDCard ):
    pass
