import time
from progress.bar import IncrementalBar


class Observer(object):
    def __init__(self):
        self.workWindow = None
        self.startWindow = None
        self.new_window = None

    def set_new_window(self, new_window_):
        if self.new_window is not None:
            self.new_window.close()
        self.new_window = new_window_
        self.new_window.set_main_window(self)
        self.new_window.setup_ui()
        self.new_window.show_window()
