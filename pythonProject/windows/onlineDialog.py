import cv2
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QDialog

# Константы
width = 330
height = 220


class UiOnlineDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.pixmap = None
        self.frame = None
        self.label = None
        self.buttonBox = None
        self.start_window = None

    def setupUi(self, window):
        window.setObjectName("window")
        window.setStyleSheet("background-color: rgb(221, 221, 221);")
        self.buttonBox = QtWidgets.QDialogButtonBox(window)
        self.buttonBox.setGeometry(QtCore.QRect(120, 300, 200, 32))
        self.buttonBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(25, 10, 401, 51))
        self.label.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QLabel(window)
        self.frame.setGeometry(QtCore.QRect(60, 75, 330, 220))
        self.frame.setObjectName("frame")

        self.retranslateUi(window)
        self.buttonBox.accepted.connect(window.accept)  # type: ignore
        self.buttonBox.rejected.connect(window.reject)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Teacher Online"))
        self.label.setText(_translate("window", "Убедитесь, что Вы сидите ровно перед камерой"))
        self.frame.setText(_translate("window", ""))

    def accept(self):
        print("OK")
        self.start_window.online_finish()

    def reject(self):
        print("Cansel!")

    def set_start_window(self, start_window):
        self.start_window = start_window


class MyDialog(UiOnlineDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.cap = None

    def show_video(self):
        self.cap = cv2.VideoCapture(0)

        while True:
            flag, frame = self.cap.read()

            if not flag:
                break

            dim = (width, height)
            frame = cv2.resize(frame, dim)
            frame = cv2.flip(frame, 1)
            cv2.rectangle(frame,
                          (round(width / 3), round(height * 0.09)),
                          (round(width * 2 / 3), round(height * 0.7)),
                          (0, 0, 255),
                          2)
            cv2.imwrite('cam.png', frame)

            self.pixmap = QtGui.QPixmap('cam.png')
            self.frame.setPixmap(self.pixmap)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def closeEvent(self, event):
        self.cap.release()
        cv2.destroyAllWindows()

    def hand_finish(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.close()
