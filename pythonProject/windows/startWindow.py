import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from windows import abstractWindow
from windows import workWindow as wW
from windows.onlineDialog import MyDialog

# Константы
width = 330
height = 220


class UiStartWindow(abstractWindow.Window, QMainWindow):
    def __init__(self):
        super().__init__()
        self.online_but = None
        self.work_window = None
        self.observer = None
        self.new_class = None
        self.w = None
        self.workWindow = None
        self.path = None
        self.export_but = None
        self.label_2 = None
        self.label = None
        self.centralwidget = None
        self.app = None
        self.StartWindow = QtWidgets.QMainWindow()
        self.pixmap = None
        self.dialog = None

    def setup_ui(self):
        self.StartWindow.setObjectName("StartWindow")
        self.StartWindow.resize(1000, 800)
        self.StartWindow.setStyleSheet("background-color: rgb(72, 72, 72);border-color: rgb(54, 54, 54);")
        self.centralwidget = QtWidgets.QWidget(self.StartWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 30, 1000, 80))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("background-color: rgb(148, 148, 148);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 900, 600))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setWordWrap(False)
        self.label_2.setMargin(20)
        self.label_2.setObjectName("label_2")
        self.export_but = QtWidgets.QPushButton(self.centralwidget)
        self.export_but.setGeometry(QtCore.QRect(720, 400, 90, 30))
        self.export_but.setIconSize(QtCore.QSize(30, 20))
        self.export_but.setObjectName("export_but")
        self.export_but.setStyleSheet("background-color: rgb(255, 255, 255);border-color: rgb(54, 54, 54);")
        self.online_but = QtWidgets.QPushButton(self.centralwidget)
        self.online_but.setGeometry(QtCore.QRect(470, 475, 90, 30))
        self.online_but.setIconSize(QtCore.QSize(60, 20))
        self.online_but.setObjectName("online_but")
        self.online_but.setStyleSheet("background-color: rgb(255, 255, 255);border-color: rgb(54, 54, 54);")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(300, 400, 400, 30))
        self.path.setObjectName("path")
        self.path.setPlaceholderText("Enter path")
        self.path.setStyleSheet("background-color: rgb(255, 255, 255);border-color: rgb(54, 54, 54);")
        self.StartWindow.setCentralWidget(self.centralwidget)
        self.retranslate_ui(self.StartWindow)
        QtCore.QMetaObject.connectSlotsByName(self.StartWindow)
        self.add_functions()

    def retranslate_ui(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Teacher Online"))
        self.label.setText(_translate("StartWindow", "Teacher Online"))
        self.label_2.setText(_translate("StartWindow", "Enter path to your video"))
        self.export_but.setText(_translate("StartWindow", "Export"))
        self.online_but.setText(_translate("StartWindow", "Online"))

    def show_window(self):
        self.StartWindow.show()

    def add_functions(self):
        self.path.returnPressed.connect(self.get_path)
        self.export_but.clicked.connect(self.get_path)
        self.online_but.clicked.connect(self.dialog_online_window)

    def set_main_window(self, window_):
        self.observer = window_

    def close(self):
        self.StartWindow.close()

    def work(self):
        pass

    def get_path(self):
        if self.path.text() != "":
            self.work_window = wW.UiWorkWindow(self.path.text())
        else:
            self.work_window = wW.UiWorkWindow("0")

        self.observer.set_new_window(self.work_window)

    def set_application(self, application):
        self.app = application

    def dialog_online_window(self):
        self.dialog = MyDialog()
        self.dialog.set_start_window(self)
        self.dialog.show()
        self.dialog.show_video()

    def online_finish(self):
        self.dialog.hand_finish()
        self.get_path()
