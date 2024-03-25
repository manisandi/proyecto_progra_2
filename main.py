from PyQt5.QtWidgets import QMainWindow,QApplication, QLineEdit
from PyQt5.QtGui import QGuiApplication,QIcon
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
import sys

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi('design.ui',self)


if __name__== '__main__':
    app = QApplication(sys.argv)
    my_app=Login()
    my_app.show()
    sys.exit(app.exec_())
