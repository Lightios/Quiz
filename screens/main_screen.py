from kivy.lang import Builder
from kivy.properties import StringProperty, ColorProperty
from kivymd.app import App
from kivy.uix.screenmanager import Screen
from kivymd.uix.card import MDCard

from widgets.select_button import SelectButton

PROPER_POS = {"center_x": 0.5, "center_y": 0.4}
HIDE_POS = {"center_x": -2}

Builder.load_file("screens/main_screen.kv")


class MainScreen(Screen):
    def __init__(self, **kwargs):
        self.app = App.get_running_app()
        self.selected_mode = None

        super().__init__(**kwargs)

    def choose_mode(self):
        if self.selected_mode:
            self.app.root.ids.screen_manager.current = self.selected_mode

        self.app.root.ids.screen_manager.current = "abc"

    def select(self, select_button):
        for i in range(3):
            self.ids[f"select_{i}"].color = "white"
        select_button.color = "orange"

        if select_button.icon == "alphabetical":
            self.ids.abc_options.pos_hint = PROPER_POS
            self.ids.translation_options.pos_hint = HIDE_POS
            self.ids.category_options.pos_hint = HIDE_POS
            self.selected_mode = "abc"
        elif select_button.icon == "translate-variant":
            self.ids.abc_options.pos_hint = HIDE_POS
            self.ids.translation_options.pos_hint = PROPER_POS
            self.ids.category_options.pos_hint = HIDE_POS
        elif select_button.icon == "shape-outline":
            self.ids.abc_options.pos_hint = HIDE_POS
            self.ids.translation_options.pos_hint = HIDE_POS
            self.ids.category_options.pos_hint = PROPER_POS


class SelectButton(MDCard):
    icon = StringProperty()
    color = ColorProperty()

    def select(self):
        self.parent.select(self)


class ABCOptions(MDCard):
    pass


class TranslationOptions(MDCard):
    pass


class CategoryOptions(MDCard):
    pass
