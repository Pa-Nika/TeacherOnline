from PyQt5.QtWidgets import QApplication
from windows import startWindow as sW
from windows import workWindow as wW
import sys


class MainWindow(object):
    def __init__(self):
        self.workWindow = None
        self.startWindow = None
        self.app = QApplication(sys.argv)

    def show_window_1(self):
        self.startWindow = sW.UiStartWindow()
        self.startWindow.set_main_window(self)
        self.startWindow.setup_ui()
        self.startWindow.show_window()

    def show_window_2(self, path):
        self.workWindow = wW.UiWorkWindow(path)
        self.workWindow.setup_ui()
        self.workWindow.show_window()
        self.startWindow.close()
        self.workWindow.work()
