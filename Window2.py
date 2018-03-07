import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPolygonF, QImage
from PyQt5.QtCore import Qt, QRectF, QPointF
from math import sin, cos, pi

class Window_2(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)

    def paintEvent(self, event):
        # Создаём QPainter и начинаем рисование на виджете.
        p = QPainter()
        p.begin(self)
        # необязательная настройка для рисования линий. Рисование будет идти
        # чуть медленнее, но сами линии будут более сглаженными.
        p.setRenderHint(QPainter.Antialiasing)

        # Устанавливаем красную ручку шириной 2 пикселя для рисования контура
        p.setPen(QPen(QColor(255, 0, 0), 2))
	# Рисуем точку в координате 30, 40.
        p.drawPoint(QPointF(30, 40))

	# Рисуем две параллельные линии, одну зелёным, другую синим цветом
        p.setPen(QPen(QColor(0, 255, 0), 2))
        p.drawLine(QPointF(50, 10), QPointF(100, 110))
        p.setPen(QPen(QColor(0, 0, 255), 2))
        p.drawLine(QPointF(70, 10), QPointF(120, 110))

	# Чёрная ручка шириной 2 для контура и светло-красная кисть
        # для внутренней части фигуры
        p.setPen(QPen(QColor(0, 0, 100), 2))
        p.setBrush(QBrush(QColor(200, 100, 100)))
	# Рисуем прямоугольник 50 на 50 с левой верхней точкой (150, 40).
        p.drawRect(QRectF(150, 40, 50, 50))
	# Рисуем эллипс с центром в точке (270, 65) и полуосями
        # 50 по X и 30 по Y.
        p.setPen(QPen(QColor(0, 230, 100), 2))

        p.drawEllipse(QPointF(270, 65), 50, 30)

        # Рисуем небольшой прямогуольный треугольник с помощью
	# drawPolygon
        points = [QPointF(50, 350), QPointF(70, 370), QPointF(50, 390)]
        polygon = QPolygonF(points)
        p.drawPolygon(polygon)

        p.drawText(50, 200, "Hello world!")

        # Загружаем рисунок из файла. Загрузка рисунка достаточно
        # долгая операция, поэтому в более сложных программах лучше
        # выполнять загрузки не при каждой перерисовке окна, как здесь,
        # а один раз загружать картинку в свойство и потом пользоваться им.
        # Например, можно перенести загрузку картинок в метод __init__.
        img = QImage("grumpycat.jpg")
        p.drawImage(QPointF(200, 200), img)
        p.drawImage(QRectF(70, 250, 50, 50), img)

        # Заканчиваем рисование
        p.end()
