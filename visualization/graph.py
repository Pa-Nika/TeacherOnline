from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib import pyplot as plt


class Graph:
    def __init__(self, df):
        self.frame = None
        self.pixmap = None
        self.loading_dialog = None
        self.df = df

    def print_graph(self):
        a = plt.hist(self.df['max'])
        # self.loading_dialog.set_frame('cam.png')
        self.set_frame(a)
        plt.show()

    def set_frame(self, frame):
        self.pixmap = QtGui.QPixmap(frame)
        self.frame.setPixmap(self.pixmap)
