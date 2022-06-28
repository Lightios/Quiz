from kivymd.app import App
from kivy.uix.screenmanager import Screen


class MainScreen( Screen ):
    def __init__( self, **kwargs ):
        self.app = App.get_running_app()

        super().__init__( **kwargs )

    def choose_screen( self, screen: str ):
        self.app.root.ids.screen_manager.current = screen
