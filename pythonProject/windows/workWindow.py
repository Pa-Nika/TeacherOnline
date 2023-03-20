from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from position import positionAnalysis as pA
from windows import abstractWindow
import dlib
from threading import Thread


class UiWorkWindow(abstractWindow.Window):
    def __init__(self, path):
        super().__init__()
        self.centralWidget = None
        self.predictor = None
        self.detector = None
        self.observer = None
        self.position = None
        self.label = None
        self.frame = None
        self.textEdit = None
        self.app = None
        self.workWindow = QtWidgets.QMainWindow()
        self.pixmap = None
        self.path = path

        # создать поток для просчитывания сетов из позиции
        # th = Thread(target=self.read_info_thread)
        # th.start()

    def read_info_thread(self):
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def setup_ui(self):
        self.workWindow.setObjectName("MainWindow")
        self.workWindow.resize(1000, 800)
        self.workWindow.setStyleSheet("background-color: rgb(148, 148, 148);")
        self.centralWidget = QtWidgets.QWidget(self.workWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QLabel(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(630, 70, 330, 220))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setText("")
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(630, 330, 330, 400))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 70, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.workWindow.setCentralWidget(self.centralWidget)

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

    def work(self):
        self.position.work(self.detector, self.predictor)

    def close(self):
        self.workWindow.close()

    def set_application(self, application):
        self.app = application

