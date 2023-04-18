from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from windows import abstractWindow


class UiGraphWindow(abstractWindow.Window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.app = None
        self.observer = None
        self.Window = QtWidgets.QMainWindow()
        self.label = None
        self.graph_widget = None
        self.central_widget = None

    def setup_ui(self):
        self.Window.setObjectName("Window")
        self.Window.resize(1000, 800)
        self.Window.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.central_widget = QtWidgets.QWidget(self.Window)
        self.central_widget.setObjectName("central_widget")
        self.graph_widget = QtWidgets.QWidget(self.central_widget)
        self.graph_widget.setGeometry(QtCore.QRect(250, 250, 500, 300))
        self.graph_widget.setObjectName("graph_widget")
        self.label = QtWidgets.QLabel(self.central_widget)
        self.label.setGeometry(QtCore.QRect(390, 150, 220, 61))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Window.setCentralWidget(self.central_widget)

        self.retranslate_ui(self.Window)
        QtCore.QMetaObject.connectSlotsByName(self.Window)

    def retranslate_ui(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "MainWindow"))
        self.label.setText(_translate("Window", "Положение в кадре"))

    def show_window(self):
        self.Window.show()

    def set_main_window(self, window_):
        self.observer = window_

    def close(self):
        self.Window.close()

    def work(self):
        pass

    def set_application(self, application):
        self.app = application
