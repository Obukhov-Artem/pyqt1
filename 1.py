from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QLabel, QLineEdit
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Первая программа')

        self.btn = QPushButton('Пуск', self)
        self.btn.move(120, 60)
        self.btn.clicked.connect(self.run)

        self.first_input = QLineEdit(self)
        self.first_input.move(20, 20)

        self.second_input = QLineEdit(self)
        self.second_input.move(160, 20)

        self.summa = QLabel(self)
        self.summa.setText("Сумма")
        self.summa.move(20, 100)

        self.summ = QLCDNumber(self)
        self.summ.move(200, 100)

        self.raznost = QLabel(self)
        self.raznost.setText("Разность")
        self.raznost.move(20, 140)

        self.ras = QLCDNumber(self)
        self.ras.move(200, 140)

        self.chastnoe = QLabel(self)
        self.chastnoe.setText("Частное")
        self.chastnoe.move(20, 180)

        self.chas = QLCDNumber(self)
        self.chas.move(200, 180)

        self.proisvedenie = QLabel(self)
        self.proisvedenie.setText("Произведение")
        self.proisvedenie.move(20, 220)

        self.prois = QLCDNumber(self)
        self.prois.move(200, 220)

    def run(self):
        try:
            x, y = list(map(int, [self.first_input.text(), self.second_input.text()]))
            self.summ.display(x + y)
            self.ras.display(x - y)
            try:
                self.chas.display(x / y)
            except:
                self.chas.display("ERROR")
            self.prois.display(x * y)
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
