# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\paobe\Documents\proyecto_progra_2\Usuarios.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PantallaUsuarios(object):
    def setupUi(self, PantallaUsuarios):
        PantallaUsuarios.setObjectName("PantallaUsuarios")
        PantallaUsuarios.setEnabled(True)
        PantallaUsuarios.resize(628, 509)
        PantallaUsuarios.setMaximumSize(QtCore.QSize(628, 509))
        PantallaUsuarios.setStyleSheet("background-image: url(:/fondo/imagen-llamativa-cintas-sobre-fondo-oscuro-generacion-ai_724548-22165.jpg);")
        self.tablaUsuarios = QtWidgets.QTableWidget(PantallaUsuarios)
        self.tablaUsuarios.setGeometry(QtCore.QRect(10, 221, 601, 271))
        self.tablaUsuarios.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tablaUsuarios.setAccessibleName("")
        self.tablaUsuarios.setStyleSheet("color: rgb(255, 255, 255);\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0));")
        self.tablaUsuarios.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablaUsuarios.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablaUsuarios.setObjectName("tablaUsuarios")
        self.tablaUsuarios.setColumnCount(0)
        self.tablaUsuarios.setRowCount(0)
        self.horizontalLayoutWidget = QtWidgets.QWidget(PantallaUsuarios)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 130, 371, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnAgregar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnAgregar.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color: rgb(255,255,255);\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"")
        self.btnAgregar.setObjectName("btnAgregar")
        self.horizontalLayout.addWidget(self.btnAgregar)
        self.btnEditar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEditar.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color: rgb(255,255,255);\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"\n"
"")
        self.btnEditar.setObjectName("btnEditar")
        self.horizontalLayout.addWidget(self.btnEditar)
        self.btnEliminar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnEliminar.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color: rgb(255,255,255);\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"")
        self.btnEliminar.setObjectName("btnEliminar")
        self.horizontalLayout.addWidget(self.btnEliminar)
        self.btnCancelar_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btnCancelar_3.setStyleSheet("QPushButton{\n"
"    color: rgb(127, 0, 190);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid #ffffff;\n"
"}\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color: rgb(255,255,255);\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"")
        self.btnCancelar_3.setObjectName("btnCancelar_3")
        self.horizontalLayout.addWidget(self.btnCancelar_3)
        self.label_3 = QtWidgets.QLabel(PantallaUsuarios)
        self.label_3.setGeometry(QtCore.QRect(430, 10, 171, 181))
        self.label_3.setStyleSheet("image: url(:/fondo/perfil-de-usuario (1).png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.lblUsuarios = QtWidgets.QLabel(PantallaUsuarios)
        self.lblUsuarios.setEnabled(True)
        self.lblUsuarios.setGeometry(QtCore.QRect(31, 21, 81, 31))
        self.lblUsuarios.setStyleSheet("QLabel{    \n"
"color:rgb(255,255,254);\n"
"font: 12pt\"Arial\";\n"
"background-color: rgb(170, 85, 0);;\n"
"}")
        self.lblUsuarios.setObjectName("lblUsuarios")
        self.txtUsuario = QtWidgets.QLineEdit(PantallaUsuarios)
        self.txtUsuario.setGeometry(QtCore.QRect(140, 20, 221, 31))
        self.txtUsuario.setStyleSheet("QLineEdit{\n"
"/*background-color:rgba(0,0,0);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid rgb(255,255,255);*/\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"/*background-color:rgba(0,0,0);\n"
"background-color: :rgba(12,12,12);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"border:2px solid rgb(120,0,171);*/\n"
"\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"/*color: rgb(255,255,255);*/\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"QLineEdit:focus{\n"
"background-color:rgba(0,0,0);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"border:2px solid rgb(120,0,171);\n"
"}\n"
"")
        self.txtUsuario.setObjectName("txtUsuario")
        self.lblContrasenia = QtWidgets.QLabel(PantallaUsuarios)
        self.lblContrasenia.setGeometry(QtCore.QRect(31, 71, 91, 31))
        self.lblContrasenia.setStyleSheet("QLabel{    \n"
"color:rgb(255,255,254);\n"
"font: 12pt\"Arial\";\n"
"background-color: rgb(170, 85, 0);;\n"
"}")
        self.lblContrasenia.setObjectName("lblContrasenia")
        self.txtContrasenia = QtWidgets.QLineEdit(PantallaUsuarios)
        self.txtContrasenia.setGeometry(QtCore.QRect(140, 70, 221, 31))
        self.txtContrasenia.setStyleSheet("QLineEdit{\n"
"/*background-color:rgba(0,0,0);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"border:2px solid rgb(255,255,255);*/\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"color:rgb(255,255,254);\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"/*background-color:rgba(0,0,0);\n"
"background-color: :rgba(12,12,12);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"border:2px solid rgb(120,0,171);*/\n"
"\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"/*color: rgb(255,255,255);*/\n"
"border:2px solid rgb(120,0,171);\n"
"  background-color: rgb(170, 85, 0);\n"
"}\n"
"QLineEdit:focus{\n"
"background-color:rgba(0,0,0);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"border:2px solid rgb(120,0,171);\n"
"}\n"
"")
        self.txtContrasenia.setObjectName("txtContrasenia")

        self.retranslateUi(PantallaUsuarios)
        QtCore.QMetaObject.connectSlotsByName(PantallaUsuarios)

    def retranslateUi(self, PantallaUsuarios):
        _translate = QtCore.QCoreApplication.translate
        PantallaUsuarios.setWindowTitle(_translate("PantallaUsuarios", "Form"))
        self.btnAgregar.setText(_translate("PantallaUsuarios", "Agregar"))
        self.btnEditar.setText(_translate("PantallaUsuarios", "Editar"))
        self.btnEliminar.setText(_translate("PantallaUsuarios", "Eliminar"))
        self.btnCancelar_3.setText(_translate("PantallaUsuarios", "Cancelar/Reintentar"))
        self.lblUsuarios.setText(_translate("PantallaUsuarios", "Usuario"))
        self.lblContrasenia.setText(_translate("PantallaUsuarios", "Contraseña"))

