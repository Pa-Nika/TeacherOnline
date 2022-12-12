from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtGui import QPixmap

from position import positionAnalysis as pA


class UiStartWindow(object):
    def __init__(self):
        self.path = None
        self.exportBut = None
        self.label_2 = None
        self.label = None
        self.centralwidget = None
        self.app = QtWidgets.QApplication(sys.argv)
        self.StartWindow = QtWidgets.QMainWindow()

    def setup_ui(self):
        self.StartWindow.setObjectName("StartWindow")
        self.StartWindow.resize(1000, 800)
        self.StartWindow.setStyleSheet("background-color: rgb(255, 255, 255);border-color: rgb(54, 54, 54);")
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
        self.exportBut = QtWidgets.QPushButton(self.centralwidget)
        self.exportBut.setGeometry(QtCore.QRect(720, 400, 90, 30))
        self.exportBut.setIconSize(QtCore.QSize(30, 20))
        self.exportBut.setObjectName("exportBut")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(300, 400, 400, 30))
        self.path.setObjectName("path")
        self.path.setPlaceholderText("Enter path")
        self.StartWindow.setCentralWidget(self.centralwidget)
        self.retranslate_ui(self.StartWindow)
        QtCore.QMetaObject.connectSlotsByName(self.StartWindow)

        self.add_functions()

    def retranslate_ui(self, StartWindow):
        _translate = QtCore.QCoreApplication.translate
        StartWindow.setWindowTitle(_translate("StartWindow", "Teacher Online"))
        self.label.setText(_translate("StartWindow", "Teacher Online"))
        self.label_2.setText(_translate("StartWindow", "Enter path to your video"))
        self.exportBut.setText(_translate("StartWindow", "Export"))

    def show_window(self):
        self.StartWindow.show()
        sys.exit(self.app.exec_())

    def add_functions(self):
        self.path.returnPressed.connect(self.get_path)
        self.exportBut.clicked.connect(self.get_path)

    def get_path(self):
        position = pA.PositionAnalysis(self.path.text())
        position.work()

