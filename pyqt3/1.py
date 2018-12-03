import sys
from PyQt5.QtWidgets import QWidget, QApplication,QPushButton,QInputDialog
from PyQt5.QtGui import QPainter, QColor
import random,copy

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.draw = None
        self.base = [80,80,120,30]
    def initUI(self):
        self.setGeometry(300, 300, 300, 400)
        self.setWindowTitle('Цветной флаг')

        self.button_1 = QPushButton(self)
        self.button_1.move(20,40)
        self.button_1.setText("Ввести количество цветов флага")
        self.button_1.clicked.connect(self.run)

        self.show()

    def run(self):
        i,okBtnPressed = QInputDialog.getInt(self, "Введите число цветов флага", "Сколько цветов?", 3, 1, 10, 1)
        if okBtnPressed:
            self.flag = None
            self.draw = i

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.drawFlag(qp)
            qp.end()

    def drawFlag(self,qp):
        base = copy.copy(self.base)
        for i in range(self.draw):
            rand_color = QColor(*[random.randrange(255) for _ in range(3)])
            qp.setBrush(rand_color)
            qp.drawRect(*base)
            base[1]+=30
        self.draw = None


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
