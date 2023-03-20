import sys
from windows import startWindow as sW
from PyQt5.QtWidgets import QApplication, QMessageBox
from windows import observer as obs


def application():
    app = QApplication(sys.argv)
    start_window = sW.UiStartWindow()
    window = obs.Observer(app)
    window.set_new_window(start_window)
    sys.exit(app.exec_())


if __name__ == "__main__":  # Если вызываем этот файл в качестве главного файла
    application()

# pyuic5 -x workWindow.ui -o workWindow.py
# C:\!Папка Вероники\Учеба\Практика\video\My_video.mp4
# C:\!Папка Вероники\Учеба\Практика\video\Test_video.mp4




    # def closeEvent(self, event):
    #     print("AAAA")
    #     # Переопределить colseEvent
    #     reply = QMessageBox.question\
    #         (self, 'Вы нажали на крестик',
    #          "Вы уверены, что хотите уйти?",
    #          QMessageBox.Yes,
    #          QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         event.accept()
    #     else:
    #         event.ignore()