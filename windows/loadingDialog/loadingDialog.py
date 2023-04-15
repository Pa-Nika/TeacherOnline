from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog


class UiLoadingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.buttonBox = None
        self.progressBar = None
        self.label = None
        self.frame = None
        self.pause = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.frame.setStyleSheet("background-color: rgb(68, 56, 72);")
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
            "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,"
            " stop:0 rgba(52, 0, 168, 255), stop:1 rgba(255,     255, 255, 255))\n"
            "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar.setObjectName("progressBar")
        self.pause = QtWidgets.QPushButton(self.frame)
        self.pause.setGeometry(QtCore.QRect(150, 180, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pause.setFont(font)
        self.pause.setStyleSheet("background-color: rgb(255, 255, 255);\nborder-color: rgb(0, 0, 0);")
        self.pause.setObjectName("pause")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.frame)
        self.buttonBox.setGeometry(QtCore.QRect(150, 230, 90, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.buttonBox.setFont(font)
        self.buttonBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        # self.buttonBox.rejected.connect(Dialog.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        # self.add_functions()

    def add_functions(self):
        self.pause.clicked.connect(self.pause_load)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Loading"))
        self.pause.setText(_translate("Dialog", "Pause"))

    def pause_load(self):
        print("Pause")

    def reject(self):
        super(UiLoadingDialog, self).reject()
        # print("aaa")
