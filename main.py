import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout
from PyQt5.QtGui import QIcon,QImage,QPalette,QBrush,QFont
from PyQt5.QtCore import pyqtSlot,QSize
from PyQt5 import QtCore

from Window1 import Window_1
from draw_graph import PlotCanvas
from VisualizationWidget import VisualizationWidget
from VisualizationWindow import VisualizationWindow

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Lab 2'
        self.left = 0
        self.top = 0
        self.width = 450
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)

        oImage = QImage("back1.jpg")
        sImage = oImage.scaled(QSize(self.height, self.width))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        # self.setPalette(palette)




        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = Window_1()
        self.tab2 = VisualizationWindow()
        self.tab3 = PlotCanvas()
        # self.tab3 = Window_3()

        self.tabs.resize(500,1500)

        # Add tabs
        self.tabs.addTab(self.tab1,"Main")
        self.tabs.addTab(self.tab2,"Visualization sort")
        self.tabs.addTab(self.tab3,"Graph")

        # self.tabs.addTab(self.tab3,"Cycle algorithm")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("Lab 1")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
