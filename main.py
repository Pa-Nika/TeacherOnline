import sys
from PyQt5.QtWidgets import QApplication
from windows import mainWindow as mW


app = QApplication(sys.argv)
w = mW.MainWindow()
w.show_window_1()
sys.exit(app.exec_())


# pyuic5 -x workWindow.ui -o workWindow.py
# C:\!Папка Вероники\Учеба\Практика\video\My_video.mp4
# C:\!Папка Вероники\Учеба\Практика\video\Test_video.mp4