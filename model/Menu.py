from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_Usuarios import Ui_Usuarios
from Ui_Empleados import Ui_Empleados
from Ui_MenuPrincipal import Ui_MenuPrincipal

class MenuPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MenuPrincipal()
        self.ui.setupUi(self)

        self.ui.btnUsuarios.clicked.connect(self.mostrar_ventana_usuarios)
        self.ui.btnEmpleados.clicked.connect(self.mostrar_ventana_empleados)

    def mostrar_ventana_usuarios(self):
        ventana_usuarios = QtWidgets.QMdiSubWindow()
        ui_usuarios = Ui_Usuarios()
        ui_usuarios.setupUi(ventana_usuarios)
        ventana_usuarios.setWidget(ui_usuarios)
        self.ui.mdiArea.addSubWindow(ventana_usuarios)
        ventana_usuarios.show()

    def mostrar_ventana_empleados(self):
        ventana_empleados = QtWidgets.QMdiSubWindow()
        ui_empleados = Ui_Empleados()
        ui_empleados.setupUi(ventana_empleados)
        ventana_empleados.setWidget(ui_empleados)
        self.ui.mdiArea.addSubWindow(ventana_empleados)
        ventana_empleados.show()


