from abc import abstractmethod
from PyQt5.QtWidgets import QMainWindow, QMessageBox


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

    @abstractmethod
    def setup_ui(self):
        pass

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def set_main_window(self, window_):
        pass

    @abstractmethod
    def show_window(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def set_application(self, application):
        pass
