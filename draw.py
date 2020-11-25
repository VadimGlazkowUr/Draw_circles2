import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('button.ui', self)
        self.pushButton.clicked.connect(self.count)
        self.draw_circles = False


    def count(self):
        self.pushButton.close()
        self.draw_circles = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw_circles:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
            self.draw_circles = False

    def draw_flag(self, qp):
        qp.setPen(QColor(255, 255, 0))
        score = randint(5, 10)
        for _ in range(score):
            diameter = randint(50, 100)
            x = randint(diameter, 660 - diameter)
            y = randint(diameter, 325 - diameter)
            qp.drawEllipse(x, y, diameter, diameter)
            print(x, y, diameter)



    def except_hook(cls, exception, traceback):
            sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())