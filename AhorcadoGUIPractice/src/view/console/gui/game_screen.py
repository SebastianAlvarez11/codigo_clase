from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador

Builder.load_file("src/view/console/gui/kv/game_screen.kv")

class MainScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def abrir_pantalla_de_juego(self):
        self.manager.current = "MainScreen"