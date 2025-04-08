from src.view.console.gui.gui import AhorcadoApp
from src.controller.app_controlador import AppControlador

if __name__ == '__main__':
    app_controlador: AppControlador = AppControlador()
    AhorcadoApp(app_controlador).run()