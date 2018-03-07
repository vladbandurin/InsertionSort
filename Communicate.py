import sys
from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout,
                                QApplication)
from PyQt5.QtCore import QObject, Qt, pyqtSignal,QPointF,QTimer, QThread
from PyQt5.QtGui import QPainter, QFont, QColor, QPen
import time
from random import randint
import copy

class Communicate(QObject):
    start = pyqtSignal(bool)
    updateValue = pyqtSignal(int)
    updateCurrent = pyqtSignal(int)
    updateSubstitute = pyqtSignal(int)
    swap = pyqtSignal(int)
    finish = pyqtSignal(int)
