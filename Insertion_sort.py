import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout,
                                QApplication)
from PyQt5.QtCore import QObject, Qt, pyqtSignal,QPointF,QTimer, QThread
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import time
from random import randint
import copy

from Communicate import Communicate
from BurningWidget import BurningWidget

class Insertion_sort(QThread):
    def __init__(self,parent = None):
        QThread.__init__(self, parent)
        self.c = Communicate()
        self.count = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.runtimer)

        self.wid = BurningWidget()
        self.c.updateValue[int].connect(self.wid.setValue)
        self.c.updateCurrent[int].connect(self.wid.setCurrent)
    def run(self):
        A = [2,6,7,5,47,6,1,3]
        self.count = len(A)
        for j in range(1,len(A)):
            self.sleep(1)
            self.c.updateValue.emit(j)
            self.wid.repaint()
            print("================")
            key = A[j]
            i = j-1
            while i>=0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
    def runtimer(self):

        self.count -= 1
        if self.count == 0:
            self.timer.stop()
