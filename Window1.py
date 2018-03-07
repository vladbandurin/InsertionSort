import sys
from PyQt5.QtWidgets import QMainWindow, QApplication,\
                            QPushButton, QWidget, QAction, QTabWidget,QGridLayout,\
                            QLineEdit, QLabel
from PyQt5.QtGui import QIcon, QPixmap,QRegExpValidator
from PyQt5.QtCore import pyqtSlot, QRegExp

from algorithm import insertion_sort
class Window_1(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QGridLayout(self)

        self.a = QLineEdit()
        self.label_a = QLabel("Enter a")
        self.but_rez = QPushButton("Rezult")
        self.but_rez.clicked.connect(self.click_but)
        self.label_rez = QLabel("Rezult:")
        self.rez = QLabel()

        self.but_save = QPushButton('Save to file')
        self.but_load = QPushButton('Load from file')
        self.but_save.clicked.connect(self.save_to_file)
        self.but_load.clicked.connect(self.load_from_file)



        self.layout.addWidget(self.label_a,0,0)
        self.layout.addWidget(self.a,1,0)
        self.layout.addWidget(self.but_rez,2,0)
        self.layout.addWidget(self.label_rez,3,0)
        self.layout.addWidget(self.rez,4,0)
        self.layout.addWidget(self.but_save,5,0)
        self.layout.addWidget(self.but_load,6,0)

        self.validate_input()


    def validate_input(self):
        regexp = QRegExp('([0-9]*,?[0-9]*)*')
        validator = QRegExpValidator(regexp)
        self.a.setValidator(validator)


    def click_but(self):
        a = self.a.text()

        A = [float(i) for i in a.split(',')]
        print(A)
        self.rez.setText(str(insertion_sort(A)))


    def save_to_file(self):
        with open('list1.txt','w') as f:
            f.write(self.a.text())


    def load_from_file(self):
        with open('list1.txt','r') as f:
            text = f.read()
            print(text)
        self.a.setText(text)
        # self.z.setText(text[1])
