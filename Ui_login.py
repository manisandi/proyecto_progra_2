# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\paobe\Documents\proyecto_progra_2\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(396, 461)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-image: url(:/fondo/imagen-llamativa-cintas-sobre-fondo-oscuro-generacion-ai_724548-22165.jpg);\n"
"    \n"
"border-radius:10px;\n"
"\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(400, 600))
        self.frame_3.setStyleSheet("QLabel{    \n"
"color:rgb(255,255,254);\n"
"font: 12pt\"Arial\";\n"
"background-color: rgb(170, 85, 0);;\n"
"}\n"
"\n"
"QLineEdit{\n"
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
"\n"
"QLineEdit:focus{\n"
"background-color:rgba(0,0,0);\n"
"border-radius:10px;\n"
"font:12pt\"Arial\";\n"
"border:2px solid rgb(120,0,171);\n"
"}\n"
"\n"
"QCheckBox{\n"
"font:12pt\"Arial\";\n"
"color: rgb(255,255,255);\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"width:18px;\n"
"height:18px;\n"
"}\n"
"\n"
"QPushButton{\n"
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
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.iniciarApp = QtWidgets.QLabel(self.frame_3)
        self.iniciarApp.setMinimumSize(QtCore.QSize(0, 35))
        self.iniciarApp.setMaximumSize(QtCore.QSize(16777215, 50))
        self.iniciarApp.setStyleSheet("")
        self.iniciarApp.setAlignment(QtCore.Qt.AlignCenter)
        self.iniciarApp.setObjectName("iniciarApp")
        self.verticalLayout_2.addWidget(self.iniciarApp)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.usuario = QtWidgets.QLineEdit(self.frame_3)
        self.usuario.setMinimumSize(QtCore.QSize(0, 35))
        self.usuario.setMaximumSize(QtCore.QSize(16777215, 35))
        self.usuario.setStyleSheet("image: url(:/prefijoNuevo/perfil-del-usuario.png);")
        self.usuario.setText("")
        self.usuario.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.usuario.setObjectName("usuario")
        self.verticalLayout_2.addWidget(self.usuario)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem3)
        self.contrasenia = QtWidgets.QLineEdit(self.frame_3)
        self.contrasenia.setMinimumSize(QtCore.QSize(0, 35))
        self.contrasenia.setMaximumSize(QtCore.QSize(16777215, 35))
        self.contrasenia.setStyleSheet("image: url(:/prefijoNuevo/cerrar-con-llave.png);")
        self.contrasenia.setText("")
        self.contrasenia.setEchoMode(QtWidgets.QLineEdit.Password)
        self.contrasenia.setObjectName("contrasenia")
        self.verticalLayout_2.addWidget(self.contrasenia)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.iniciarSesion = QtWidgets.QPushButton(self.frame_3)
        self.iniciarSesion.setMinimumSize(QtCore.QSize(0, 35))
        self.iniciarSesion.setMaximumSize(QtCore.QSize(16777215, 35))
        self.iniciarSesion.setObjectName("iniciarSesion")
        self.verticalLayout_2.addWidget(self.iniciarSesion)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.salir = QtWidgets.QPushButton(self.frame_3)
        self.salir.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.salir.setObjectName("salir")
        self.verticalLayout_2.addWidget(self.salir)
        self.horizontalLayout.addWidget(self.frame_3)
        spacerItem6 = QtWidgets.QSpacerItem(104, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.iniciarSesion.clicked.connect(MainWindow.show) # type: ignore
        self.salir.clicked.connect(MainWindow.lower) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.iniciarApp.setText(_translate("MainWindow", "Iniciar Aplicacion"))
        self.iniciarSesion.setText(_translate("MainWindow", "Iniciar Sesion"))
        self.salir.setText(_translate("MainWindow", "Salir"))
import images_rc
