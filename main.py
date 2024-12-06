import sys

from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from random import randint


class Circle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
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
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(x, y, r, r)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circle()
    ex.show()
    sys.exit(app.exec())