import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Ui_Login import Ui_MainWindow
from model import login
# from Ui_MenuPrincipal import Ui_MenuPrincipal

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

from PyQt5.QtWidgets import QMainWindow
from Ui_Login import Ui_MainWindow  # Importar la clase Ui_MainWindow desde ui_login.py

class mdiApp(QMainWindow):#
    def __init__(self):
        super().__init__()
        
        # Crear la instancia de la clase generada por Qt Designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def login(self):
        # Obtener los datos de usuario y contraseña
        usuario = self.ui.usuario.text()
        contrasenia = self.ui.contrasenia.text()

        # Validar los datos de inicio de sesión (aquí debes agregar tu lógica de autenticación)
        if usuario == "admin" and contrasenia == "1234":
            print("Inicio de sesión exitoso")
        else:
            print("Inicio de sesión fallido ")