from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivymd.uix.card import MDCard

Builder.load_file('widgets/select_button.kv')

class SelectButton(MDCard):
    type = StringProperty()
    icon = StringProperty()
    text = StringProperty()
    main_screen = ObjectProperty()

    def on_kv_post(self, base_widget):
        if self.type == "abc":
            self.icon = "alphabetical"
            self.text = "ABC"

        elif self.type == "category":
            self.icon = "shape-outline"
            self.text = "Category"

        elif self.type == "translation":
            self.icon = "translate-variant"
            self.text = "Translation"