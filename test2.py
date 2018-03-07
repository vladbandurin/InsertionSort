import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal,QPointF,QTimer
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import time
from random import randint
import copy
# from algorithm import insertion_sort

class Communicate(QObject):
    updateValue = pyqtSignal(int)
    updateCurrent = pyqtSignal(int)

class BurningWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(1, 100)
        self.value = 75
        self.num = [100-i for i in range(0,100)]
        self.lines_el = [0 for i in range(100)]

        self.weight = 300

        self.n = 100
        self.size_line = self.weight/(self.n+1)

        n = copy.copy(self.num)
        self.insertion_sort(n)
    def setValue(self, value):
        print(value)
        self.value= velue

        self.lines_el[int(value)] = 1
        # print(self.lines_el)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
    def setCurrent(self,current):
        print("current",current)
        self.lines_el = [0 for i in range(100)]

        self.lines_el[int(current)] = 1
        self.current = current
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
            elif self.current == i:
                qp.setPen(QPen(QColor(0,255,0), self.size_line))


            qp.drawLine(QPointF(i*(self.size_line+2), 100- self.num[i]),
                        QPointF(i*(self.size_line+2), 1000))
    def insertion_sort(self,A):
        for j in range(1,len(A)):
            # time.sleep(1)
            timer = QTimer()
            timer.start(100)

            # self.current = j
            # self.setCurrent(j)
            # self.repaint()

            key = A[j]
            i = j-1
            while i>=0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
        return A


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(0, 99)
        sld.setValue(0)
        sld.setGeometry(30, 0, 150, 100)

        self.c = Communicate()
        self.wid = BurningWidget()
        self.c.updateValue[int].connect(self.wid.setValue)
        self.c.updateCurrent[int].connect(self.wid.setCurrent)

        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        self.setLayout(vbox)



        self.setGeometry(300, 300, 390, 500)
        self.setWindowTitle('Burning widget')
        self.show()
        a = [2,6,7,5,47,6,1,3]
        # print(self.insertion_sort(a))

    def changeValue(self, value):
        self.c.updateCurrent.emit(value)
        self.wid.repaint()

    def insertion_sort(self,A):
        for j in range(1,len(A)):
            self.c.updateCurrent.emit(j)
            self.wid.repaint()
            print("================")
            key = A[j]
            i = j-1
            while i>=0 and A[i] > key:
                A[i+1] = A[i]
                i = i - 1
            A[i+1] = key
            time
        return A


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
