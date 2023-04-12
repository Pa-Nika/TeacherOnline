from PyQt5.QtCore import QBasicTimer

from windows.loadingDialog.loadingDialog import UiLoadingDialog
from position import positionAnalysis


class MyLoadingDialog(UiLoadingDialog):
    def __init__(self, path):
        super().__init__()
        self.position = None
        self.setupUi(self)
        self.start_window = None
        self.timer = QBasicTimer()
        self.step = 0
        self.path = path

    # def read_info_thread(self):
    #     self.position.work()

    def step_analysis(self):
        self.my_event()
        self.position = positionAnalysis.PositionAnalysis(self.path)
        self.position.set_loading_dialog(self)
        self.timer.start(100, self)
        # создать поток для просчитывания сетов из позиции
        # th = Thread(target=self.read_info_thread)
        # th.start()
        self.position.work()

    def my_event(self):
        if self.step >= 100:
            self.timer.stop()
            # self.btn.setText('Finished')
            return

        self.step += 1
        self.progressBar.setValue(self.step)
        # print(self.step)

    def set_start_window(self, start_window):
        self.start_window = start_window

