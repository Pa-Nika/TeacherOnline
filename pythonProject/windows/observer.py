
class Observer(object):
    def __init__(self, app):
        self.workWindow = None
        self.startWindow = None
        self.new_window = None
        self.app = app

    def set_new_window(self, new_window_):
        if self.new_window is not None:
            self.new_window.close()
        self.new_window = new_window_
        self.new_window.set_main_window(self)
        self.new_window.set_application(self.app)
        self.new_window.setup_ui()
        self.new_window.show_window()
        self.new_window.work()
