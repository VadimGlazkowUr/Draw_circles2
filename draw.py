import sys

from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow
from button import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        score = randint(5, 10)
        for _ in range(score):
            r_color = randint(0, 255)
            g_color = randint(0, 255)
            b_color = randint(0, 255)
            qp.setPen(QColor(r_color, g_color, b_color))
            diameter = randint(50, 100)
            x = randint(diameter, 660 - diameter)
            y = randint(diameter, 325 - diameter)
            qp.drawEllipse(x, y, diameter, diameter)

    def except_hook(cls, exception, traceback):
            sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())