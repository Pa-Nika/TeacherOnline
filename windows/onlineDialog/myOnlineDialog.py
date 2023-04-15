import cv2
from PyQt5 import QtGui

from windows.onlineDialog.onlineDialog import UiOnlineDialog

# Константы
width = 330
height = 220


class MyOnlineDialog(UiOnlineDialog):
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
