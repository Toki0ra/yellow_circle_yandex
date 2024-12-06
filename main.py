import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 800, 600)
        self.flag = False
        self.create_circle_btn = QPushButton("Создать круг", self)
        self.create_circle_btn.clicked.connect(self.click)

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.circle(qp)
            qp.end()
        self.flag = False

    def click(self):
        self.flag = True
        self.update()

    def circle(self, qp):
        x, y = randint(1, 800), randint(1, 600)
        r = randint(1, 100)
        first = randint(1, 255)
        second = randint(1, 255)
        third = randint(1, 255)
        qp.setBrush(QColor(first, second, third))
        qp.drawEllipse(x, y, r, r)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())