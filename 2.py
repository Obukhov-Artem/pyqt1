from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('Вторая программа')

        #Кнопка загрузки изображения
        self.btn = QPushButton('Показать картинку', self)
        self.btn.move(120, 340)
        self.btn.clicked.connect(self.run)

        ## Поле для ввода имени файла
        self.file_name = QLineEdit(self)
        self.file_name.move(140, 20)

        ## Изображение
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(80,60)
        self.image.resize(250,250)
        self.image.setPixmap(self.pixmap)



    def run(self):
        ## Загружаем изображение и отображаем его
        self.pixmap.load(self.file_name.text())
        self.image.setPixmap(self.pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())