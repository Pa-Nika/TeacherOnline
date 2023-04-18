from PyQt5.QtWidgets import QWidget


class Graph(QWidget):
    def __init__(self, parent=None):
        super(Graph, self).__init__(parent)
        self.initUI()
