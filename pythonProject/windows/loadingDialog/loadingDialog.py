from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class UiLoadingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.progressBar = None
        self.stop = None
        self.pause = None
        self.frame = None
        self.label = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setStyleSheet("background-color: rgb(68, 56, 72);\n")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(135, 20, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(40, 100, 320, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.progressBar.setFont(font)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(
            "QProgressBar {\n"
            "    background-color: rgb(124, 113, 116);\n"
            "    border-radius: 10px;\n"
            "    color: rgb(255, 255, 255);\n"
            "    text-align: center;\n"
            "}\n"
            "\n"
            "QProgressBar::chunk{\n"
            "    border-radius: 10px;\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(52, 0, 168, 255),"
            " stop:1 rgba(255, 255, 255, 255))\n"
            "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.pause = QtWidgets.QPushButton(self.frame)
        self.pause.setGeometry(QtCore.QRect(145, 175, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pause.setFont(font)
        self.pause.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-radius: 10px;")
        self.pause.setObjectName("pause")
        self.stop = QtWidgets.QPushButton(self.frame)
        self.stop.setGeometry(QtCore.QRect(145, 230, 110, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stop.setFont(font)
        self.stop.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-radius: 10px;")
        self.stop.setObjectName("stop")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Загрузка"))
        self.pause.setText(_translate("Dialog", "Пауза"))
        self.stop.setText(_translate("Dialog", "Остановить"))
