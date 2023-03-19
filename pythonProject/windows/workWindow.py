from PyQt5 import QtCore, QtGui, QtWidgets
from position import positionAnalysis as pA
import sys
from windows import window


class UiWorkWindow(window.Window):
    def __init__(self, path):
        super().__init__()
        self.observer = None
        self.position = None
        self.label = None
        self.frame = None
        self.textEdit = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.workWindow = QtWidgets.QMainWindow()
        self.pixmap = None
        self.path = path

    def setup_ui(self):
        self.workWindow.setObjectName("MainWindow")
        self.workWindow.resize(1000, 800)
        self.workWindow.setStyleSheet("background-color: rgb(148, 148, 148);")
        self.centralwidget = QtWidgets.QWidget(self.workWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(630, 70, 330, 220))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(630, 330, 330, 400))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.workWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui()
        QtCore.QMetaObject.connectSlotsByName(self.workWindow)

    def set_frame(self, frame):
        self.pixmap = QtGui.QPixmap(frame)
        self.frame.setPixmap(self.pixmap)

    def retranslate_ui(self):
        _translate = QtCore.QCoreApplication.translate
        self.workWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Position in the frame"))

    def set_main_window(self, window_):
        self.observer = window_

    def show_window(self):
        self.position = pA.PositionAnalysis(self.path, self.textEdit, self.frame)
        self.position.set_work_window(self)
        self.workWindow.show()
        # self.pixmap = QtGui.QPixmap('wait.png')
        # self.frame.setPixmap(self.pixmap)
        self.work()

    def work(self):
        self.position.work()

    def close(self):
        self.workWindow.close()

