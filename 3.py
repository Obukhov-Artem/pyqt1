from PyQt5.QtWidgets import QApplication, QWidget,QPushButton,QCheckBox,QPlainTextEdit
from PyQt5.QtGui import QPixmap
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = ["Чизбургер", "Гамбургер", "Кока-кола", "Нагетсы"]
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 300, 300, 400)
        self.setWindowTitle('Заказ в Макдональдсе')

        self.check_b = [QCheckBox(self) for i in self.menu]

        self.btn = QPushButton('Заказать', self)
        self.btn.clicked.connect(self.run)
        self.btn.move(10, 20 * (len(self.check_b) + 1))

        for i in range(len(self.check_b)):
            self.check_b[i].setText(self.menu[i])
            self.check_b[i].move(10,20*i)

        self.result = QPlainTextEdit(self)
        self.result.setEnabled(False)
        self.result.move(10,20*(len(self.check_b)+3))

    def run(self):
        self.result.clear()
        result = [i.text() for i in self.check_b if i.isChecked()]
        result.insert(0,"Ваш заказ\n")

        self.result.appendPlainText("\n".join(result))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())