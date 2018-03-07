import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout,
                                QApplication)
from PyQt5.QtCore import QObject, Qt, pyqtSignal,QPointF,QTimer, QThread
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import time
from random import randint,shuffle
import copy
from Communicate import Communicate

class VisualizationWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 100)

        self.num = [100-i for i in range(0,100)]
        self.lines_el = [0 for i in range(100)]

        self.weight = 300
        self.values = [100-i for i in range(100)]
        shuffle(self.values)


        self.n = 100
        self.size_line = self.weight/(self.n+1)

    def setValue(self, values):
        """Set the list to sort."""
        self.values= values
        self.n = len(values)
        self.lines_el = [0 for i in range(self.n)]
        self.update()



    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()


    def setCurrent(self,current):
        try:
            i = self.lines_el.index(1)
            self.lines_el[i] = 0
        except:
            pass
        self.lines_el[int(current)] = 1
        self.current = current
        self.update()

    def setSubstitute(self,s):
        try:
            i = self.lines_el.index(2)
            self.lines_el[i] = 0
        except:
            pass
        self.k=self.values[s]

        self.values[s+1] = self.values[s]


        self.lines_el[s] = 2
        self.update()

    def swap(self, i):
        """Swap the lines"""
        self.values[i] = self.k

    def finish(self,current):
        for i in range(len(self.lines_el)):
            self.lines_el[int(current)] = 1
        self.update()



    def drawWidget(self, qp):
        font = QFont('Serif', 100, QFont.Light)
        qp.setFont(font)

        size = self.size()
        w = size.width()
        h = size.height()

        qp.setPen(QPen(QColor(0, 0, 255), self.size_line))
        for i in range(self.n):
            if self.lines_el[i] == 0:
                qp.setPen(QPen(QColor(0, 0, 255), self.size_line))
            elif self.lines_el[i] == 1:
                qp.setPen(QPen(QColor(0, 255, 0), self.size_line))
            elif self.lines_el[i] == 2:
                qp.setPen(QPen(QColor(255,0,0), self.size_line))
            qp.drawLine(QPointF(i*(self.size_line+2), 100 - self.values[i]),
                        QPointF(i*(self.size_line+2), 1000))
