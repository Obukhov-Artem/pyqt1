import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QInputDialog


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('Диалоговые окна')

        self.button_1 = QPushButton(self)
        self.button_1.move(20, 10)
        self.button_1.setText("Кнопка")
        self.button_1.clicked.connect(self.run)
        self.button_2 = QPushButton(self)
        self.button_2.move(20, 40)
        self.button_2.setText("Кнопка2")
        self.button_2.clicked.connect(self.run2)
        self.button_3 = QPushButton(self)
        self.button_3.move(20, 70)
        self.button_3.setText("Кнопка3")
        self.button_3.clicked.connect(self.run3)

        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getText(self, "Введите имя", "Как тебя зовут?")
        if okBtnPressed:
            self.button_1.setText(i)

    def run2(self):
        i, okBtnPressed = QInputDialog.getInt(self, "Введите возраст", "Сколько тебе лет?", 20, 18, 27, 1)
        if okBtnPressed:
            self.button_2.setText(str(i))

    def run3(self):
        i, okBtnPressed = QInputDialog.getItem(self, "Выберите вашу страну", "Откуда ты?",
                                               ("Россия", "Германия", "США"), 1, False)
        if okBtnPressed:
            self.button_3.setText(i) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
