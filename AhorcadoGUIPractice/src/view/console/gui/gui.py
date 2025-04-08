from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.controller.app_controlador import AppControlador
from src.view.console.gui.main_screen import MainScreen
from src.view.console.gui.game_screen import GameScreen



class AhorcadoApp(App):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name = "MainScreen", controlador = self.controlador))
        screen_manager.add_widget(GameScreen(name = "GameScreen", controlador = self.controlador))
        screen_manager.current 
        return screen_manager