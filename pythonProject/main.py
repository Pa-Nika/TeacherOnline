import sys
from windows import startWindow as sW
from PyQt5.QtWidgets import QApplication
from windows import observer as obs


def application():
    app = QApplication(sys.argv)
    start_window = sW.UiStartWindow()
    window = obs.Observer()
    window.set_new_window(start_window)
    sys.exit(app.exec_())


if __name__ == "__main__":   # Если вызываем этот файл в качестве главного файла
    application()

# pyuic5 -x workWindow.ui -o workWindow.py
# C:\!Папка Вероники\Учеба\Практика\video\My_video.mp4
# C:\!Папка Вероники\Учеба\Практика\video\Test_video.mp4