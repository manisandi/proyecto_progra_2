
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import *
from Ui_Login import Ui_MainWindow
import tkinter as tk
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QErrorMessage
from PyQt5 import QtCore, QtGui, QtWidgets


#importar clases 
from model.empleados import Empleados
from model.usuarios import Usuarios
from model.login import login
from Ui_Empleados import Ui_Empleados
from Ui_Usuarios import Ui_Usuarios
from Ui_MenuPrincipal import Ui_MenuPrincipal
from model.Menu import MenuPrincipal

class mdiApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uimdi = Ui_MainWindow()
        self.uimdi.setupUi(self)
        self.show()

        #eventos para mostrar ventanas
        self.uimdi.iniciarSesion.clicked.connect(self.login)
        
    # Crear la instancia de la clase generada por Qt Designer
    def login(self):
    
    # Obtener los datos de usuario y contraseña
        usuario = self.uimdi.usuario.text()
        contrasenia = self.uimdi.contrasenia.text()

    # Validar los datos de inicio de sesión (aquí debes agregar tu lógica de autenticación)
        if usuario == "admin" and contrasenia == "1234":
            print("Inicio de sesión exitoso")
            self.ui = Ui_MenuPrincipal()
            self.ui.setupUi(self)
            self.show()
        else:
            print("Inicio de sesión fallido ")

    def mostrar_ventana_usuarios(self):
        ventana_usuarios = QtWidgets.QMainWindow()
        Ui_Usuarios = Ui_Usuarios()
        Ui_Usuarios.setupUi(ventana_usuarios)
        ventana_usuarios.setWidget(Ui_Usuarios)
        self.ui.mdiArea.addSubWindow(ventana_usuarios)
        ventana_usuarios.show()

    def mostrar_ventana_empleados(self):
        ventana_empleados = QtWidgets.QMainWindow()
        Ui_Empleados = Ui_Empleados()
        Ui_Empleados.setupUi(ventana_empleados)
        ventana_empleados.setWidget(Ui_Empleados)
        self.ui.mdiArea.addSubWindow(ventana_empleados)
        ventana_empleados.show() 

        self.ui.btnUsuarios.clicked.connect(self.openWinUsuarios)
        self.ui.btnEmpleados.clicked.connect(self.openWinEmpleados)


    def msgBox(self, mensaje, icono, tipo=0):
        msg = QMessageBox()
        msg.setIcon(icono)
        msg.setText(mensaje)
        msg.setWindowTitle("Mensaje")
        retval = msg.exec_() 

    def openWinUsuarios(self):
        usuario = Usuarios()
        self.winUsuarios = winUsuarios
        # agregar la ventana al mdi
        self.uimdi.centralwidget.showFullScreen(self.winUsuarios)
        # eventos
        self.winUsuarios.uiUsuarios.btnAgregar.clicked.connect(self.guardarUS)
        self.winUsuarios.uiUsuarios.btnEditar.clicked.connect(self.editarUS)
        self.winUsuarios.uiUsuarios.btnEliminar.clicked.connect(self.eliminarUS)
        #self.winUsuarios.uiUsuarios.btnCancelar.clicked.connect(self.cancelar)

        self.winUsuarios.uiUsuarios.tableWidget.clicked.connect(self.cargarDatosUS)
        self.cargarTablaUS(usuario.getNumeroRegistrosUS(), usuario.getUsuario())
        self.habiltarGuardarUS()
        self.winUsuarios.show()

    def guardarUS(self):
        usuario = Usuarios(
            self.winUsuarios.uiUsuarios.txtUsuario.text(),
            self.winUsuarios.uiUsuarios.txtContrasenia.text(),
        )
        if usuario.guardar() == 1:
            self.msgBox("Datos Guardados Correctamente", QMessageBox.Information)
            self.limpiar()
            self.cargarTablaUS(usuario.getNumeroRegistrosUS(), usuario.getUsuario())
        else:
            self.msgBox("Error al Guardar los datos", QMessageBox.Warning)

    def editarUS(self):
        usuario = Usuarios(
            self.winUsuarios.uiUsuarios.txtUsuario.text(),
            self.winUsuarios.uiUsuarios.txtContrasenia.text(),
        )
        if usuario.editar() == 1:
            self.msgBox("Datos Editar Correctamente", QMessageBox.Information)
            self.limpiar()
            self.cargarTablaUS(usuario.getNumeroRegistrosUS(), usuario.getUsuarios())
        else:
            self.msgBox("Error al Editar los datos", QMessageBox.Warning)

    def eliminarUS(self):
        usuario = Usuarios(
            self.winUsuarios.uiUsuarios.txtUsuario.text(),
            self.winUsuarios.uiUsuarios.txtContrasenia.text(),
        )
        if usuario.eliminar() == 1:
            self.msgBox("Datos Eliminados Correctamente", QMessageBox.Information)
            self.limpiar()
            self.cargarTablaUS(usuario.getNumeroRegistrosUS(), usuario.getUsuarios())
        else:
            self.msgBox("Error al Eliminar los datos", QMessageBox.Warning)

    def cargarTablaUS(self, numFilas, datos):
        # determinar el #de filas de la tabla
        self.winUsuarios.uiUsuarios.tableWidget.setRowCount(numFilas)
        # determinar el # de columnas
        self.winUsuarios.uiUsuarios.tableWidget.setColumnCount(2)
        i = 0
        for d in datos:
            print(d)
            self.winUsuarios.uiUsuarios.tableWidget.setItem(
                i, 0, QTableWidgetItem(d["usuario"])
            )
            self.winUsuarios.uiUsuarios.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["contrasenia"])
            )

            i += 1

    def cargarDatosUS(self):
        self.habiltarModificarEliminarUS()
        numFila = self.winUsuarios.uiUsuarios.tableWidget.currentRow()
        # cargamos datos en el formualario
        self.winUsuarios.uiUsuarios.txtUsuario.setText(
            self.winUsuarios.uiUsuarios.tableWidget.item(numFila, 0).text()
        )
        self.winUsuarios.uiUsuarios.txtContrasenia.setText(
            self.winUsuarios.uiUsuarios.tableWidget.item(numFila, 1).text()
        )

    def habiltarGuardarUS(self):
        self.winUsuarios.uiUsuarios.btnGuardar.setEnabled(True)
        self.winUsuarios.uiUsuarios.btnEditar.setEnabled(False)
        self.winUsuarios.uiUsuarios.btnEliminar.setEnabled(False)

    def habiltarModificarEliminarUS(self):
        self.winUsuarios.uiUsuarios.btnGuardar.setEnabled(False)
        self.winUsuarios.uiUsuarios.btnEditar.setEnabled(True)
        self.winUsuarios.uiUsuarios.btnEliminar.setEnabled(True)

    def limpiar(self):
        self.winUsuarios.uiUsuarios.txtUsuario.setText("")
        self.winUsuarios.uiUsuarios.txtContrasenia.setText("")
        self.habiltarGuardarUS()

    def openWinEmpleados(self):
        empleado = Empleados()
        self.winEmpleados = winEmpleados
        # agregar la ventana al mdi
        self.uimdi.mdiArea.addSubWindow(self.winEmpleados)
        # eventos
        self.winEmpleados.uiEmpleados.btnGuardar.clicked.connect(self.guardarEM)
        self.winEmpleados.uiEmpleados.btnEditar.clicked.connect(self.editarEM)
        self.winEmpleados.uiEmpleados.btnEliminar.clicked.connect(self.eliminarEM)
        #self.winEmpleados.uiEmpleados.btnCancelar.clicked.connect(self.cancelar)

        self.winEmpleados.uiEmpleados.tableWidget.clicked.connect(self.cargarDatosEM)
        self.cargarTablaEM(empleado.getNumeroRegistrosEM(), empleado.getEmpleado())
        self.habiltarGuardarEM()
        self.winEmpleados.show()

    def guardarEM(self):
        empleado = Empleados(
            self.winEmpleados.uiEmpleados.txtCedula.text(),
            self.winEmpleados.uiEmpleados.txtNombre.text(),
            self.winEmpleados.uiEmpleados.txtApellidos.text(),
            self.winEmpleados.uiEmpleados.txtTelefono.text(),
            self.winEmpleados.uiEmpleados.txtDireccion.text(),
            self.winEmpleados.uiEmpleados.txtPuesto.text(),
            self.winEmpleados.uiEmpleados.txtFecha.text(),
            self.winEmpleados.uiEmpleados.txtJefatura.text(),
        )
        if empleado.guardar() == 1:
            self.msgBox("Datos Guardados Correctamente", QMessageBox.Information)
            self.limpiarEM()
            self.cargarTablaEM(empleado.getNumeroRegistrosEM(), empleado.getEmpleados())
        else:
            self.msgBox("Error al Guardar los datos", QMessageBox.Warning)

    def editarEM(self):
        empleado = Empleados(
            self.winEmpleados.uiEmpleados.txtCedula.text(),
            self.winEmpleados.uiEmpleados.txtNombre.text(),
            self.winEmpleados.uiEmpleados.txtApellidos.text(),
            self.winEmpleados.uiEmpleados.txtTelefono.text(),
            self.winEmpleados.uiEmpleados.txtDireccion.text(),
            self.winEmpleados.uiEmpleados.txtPuesto.text(),
            self.winEmpleados.uiEmpleados.txtFecha.text(),
            self.winEmpleados.uiEmpleados.txtJefatura.text(),
        )
        if empleado.editar() == 1:
            self.msgBox("Datos Editar Correctamente", QMessageBox.Information)
            self.limpiarEM()
            self.cargarTablaEM(empleado.getNumeroRegistrosEM(), empleado.getEmpleados())
        else:
            self.msgBox("Error al Editar los datos", QMessageBox.Warning)

    def eliminarEM(self):
        empleado = Empleados(
            self.winEmpleados.uiEmpleados.txtCedula.text(),
            self.winEmpleados.uiEmpleados.txtNombre.text(),
            self.winEmpleados.uiEmpleados.txtApellidos.text(),
            self.winEmpleados.uiEmpleados.txtTelefono.text(),
            self.winEmpleados.uiEmpleados.txtDireccion.text(),
            self.winEmpleados.uiEmpleados.txtPuesto.text(),
            self.winEmpleados.uiEmpleados.txtFecha.text(),
            self.winEmpleados.uiEmpleados.txtJefatura.text(),
        )
        if empleado.eliminar() == 1:
            self.msgBox("Datos Eliminados Correctamente", QMessageBox.Information)
            self.limpiarEM()
            self.cargarTablaEM(empleado.getNumeroRegistrosEM(),empleado.getEmpleados())
        else:
            self.msgBox("Error al Eliminar los datos", QMessageBox.Warning)

    def cargarTablaEM(self, numFilas, datos):
        # determinar el #de filas de la tabla
        self.winEmpleados.uiEmpleados.tableWidget.setRowCount(numFilas)
        # determinar el # de columnas
        self.winEmpleados.uiEmpleados.tableWidget.setColumnCount(8)
        i = 0
        for d in datos:
            print(d)
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 0, QTableWidgetItem(d["cedula"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["nombre"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["apellidos"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["telefono"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["direccion"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["puesto"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["fecha de ingreso"])
            )
            self.winEmpleados.uiEmpleados.tableWidget.setItem(
                i, 1, QTableWidgetItem(d["jefatura"])
            )
            i += 1

    def cargarDatosEM(self):
        self.habiltarModificarEliminarEM()
        numFila = self.winEmpleados.uiEmpleados.tableWidget.currentRow()
        # cargamos datos en el formualario
        self.winEmpleados.uiEmpleados.txtCedula.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 0).text()
        )
        self.winEmpleados.uiEmpleados.txtNombre.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 1).text()
        )
        self.winEmpleados.uiEmpleados.txtApellidos.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 2).text()
        )
        self.winEmpleados.uiEmpleados.txtTelefono.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 3).text()
        )
        self.winEmpleados.uiEmpleados.txtDireccion.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 4).text()
        )
        self.winEmpleados.uiEmpleados.txtPuesto.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 5).text()
        )
        self.winEmpleados.uiEmpleados.txtFecha.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 6).text()
        )
        self.winEmpleados.uiEmpleados.txtJefatura.setText(
            self.winEmpleados.uiEmpleados.tableWidget.item(numFila, 7).text()
        )

    def habiltarGuardarEM(self):
        self.winEmpleados.uiEmpleados.btnGuardar.setEnabled(True)
        self.winEmpleados.uiEmpleados.btnEditar.setEnabled(False)
        self.winEmpleados.uiEmpleados.btnEliminar.setEnabled(False)

    def habiltarModificarEliminarEM(self):
        self.winEmpleados.uiEmpleados.btnGuardar.setEnabled(False)
        self.winEmpleados.uiEmpleados.btnEditar.setEnabled(True)
        self.winEmpleados.uiEmpleados.btnEliminar.setEnabled(True)

    def limpiarEM(self):
        self.winEmpleados.uiEmpleados.txtCedula.setText("")
        self.winEmpleados.uiEmpleados.txtNombre.setText("")
        self.winEmpleados.uiEmpleados.txtApellidos.setText("")
        self.winEmpleados.uiEmpleados.txtTelefono.setText("")
        self.winEmpleados.uiEmpleados.txtDireccion.setText("")
        self.winEmpleados.uiEmpleados.txtPuesto.setText("")
        self.winEmpleados.uiEmpleados.txtFecha.setText("")
        self.winEmpleados.uiEmpleados.txtJefatura.setText("")
        self.habiltarGuardarEM()

class winEmpleados(QWidget):
    def __init__(self):
        super().__init__()
        self.uiEmpleados = Ui_Empleados()
        self.uiEmpleados.setupUi(self)

class winUsuarios(QWidget):
    def __init__(self):
        super().__init__()
        self.uiUsuarios = Ui_Usuarios()
        self.uiUsuarios.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mdiApp()
    window.show()
    sys.exit(app.exec_())