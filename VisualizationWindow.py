import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout,
                                QApplication, QPushButton,QGridLayout)
from PyQt5.QtCore import QObject, Qt, pyqtSignal,QPointF,QTimer, QThread
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import time
from random import randint,shuffle
from VisualizationWidget import VisualizationWidget
# from Insertion_sort import Insertion_sort
from Communicate import Communicate

class VisualizationWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        #Define slider
        self.sld = QSlider(Qt.Horizontal, self)
        self.sld.setFocusPolicy(Qt.NoFocus)
        self.sld.setRange(0, 99)
        self.sld.setValue(0)
        self.sld.setGeometry(30, 0, 150, 100)

        #Define buttons
        self.start_but = QPushButton('Start')
        self.start_but.clicked.connect(self.start)
        self.but_load = QPushButton('Load from file')
        self.but_load.clicked.connect(self.load_from_file)

        self.but_load_500 = QPushButton('Load 500')
        self.but_load_500.clicked.connect(self.load_500)

        self.c = Communicate()
        self.wid = VisualizationWidget()
        self.c.updateValue[int].connect(self.wid.setValue)
        self.c.updateCurrent[int].connect(self.wid.setCurrent)
        self.c.updateSubstitute[int].connect(self.wid.setSubstitute)
        self.c.finish[int].connect(self.wid.finish)

        self.sld.valueChanged[int].connect(self.changeInterval)
        layout = QGridLayout()
        layout.addWidget(self.start_but)
        layout.addWidget(self.but_load)
        layout.addWidget(self.but_load_500)



        layout.addWidget(self.wid)
        layout.addWidget(self.sld)

        self.setLayout(layout)

        self.setGeometry(300, 300, 390, 500)
        self.setWindowTitle('VisualizationWidget')

        #Create Timer which will create events to repainting of sortWidget
        self.interval = 5
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.runtimer)
        self.timer.setInterval(self.interval)

        #Create the list with values
        self.amount_el = 50
        self.values = [self.amount_el+10-i for i in range(self.amount_el)]
        shuffle(self.values)
        self.wid.setValue(self.values)

        self.show()

    def load_500(self):
        with open('./arrays/reverse_100.txt','r') as f:
            text = f.read()
            print(text)
        A = [float(i) for i in text.split(',')]
        self.wid.setValue(A)
        self.values = A

    def load_from_file(self):
        with open('list1.txt','r') as f:
            text = f.read()
            print(text)
        A = [float(i) for i in text.split(',')]
        self.wid.setValue(A)
        self.values = A


    def start(self):
        """Start timer"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.runtimer)
        self.interval = self.sld.value()*10
        self.timer.setInterval(self.interval)

        self.sortGen = self.insertion_sort()
        self.timer.start()


    def changeInterval(self,i):
        """Change timer interval"""
        self.interval = i
        self.timer.setInterval(i*10)



    def insertion_sort(self):
        """Sort function."""

        A = self.values
        print(A)
        self.count = len(A)
        for j in range(1,len(A)):
            yield (0,j)

            key = A[j]
            i = j-1
            while i>=0 and A[i] > key:
                yield (1,i)
                A[i+1] = A[i]
                i = i - 1
            yield (2,i)
            A[i+1] = key


    def finish(self):
        self.c.finish.emit(self.n)
        self.n+=1
        if self.n == len(self.values):
            self.timer.stop()
            self.n = 0
            print('stop timer')



    def runtimer(self):

        try:
            s = self.sortGen.__next__()
            if s[0] == 0:
                self.c.updateCurrent.emit(s[1])
            elif s[0] == 1:
                self.c.updateSubstitute.emit(s[1])
            elif s[0] == 2:
                self.c.swap.emit(s[1])
        except:
            self.n=0
            self.timer.timeout.connect(self.finish)
            self.interval = 0.5
            self.timer.setInterval(0.5)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VisualizationWindow()
    sys.exit(app.exec_())
