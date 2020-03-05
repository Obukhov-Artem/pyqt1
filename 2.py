from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 600, 400)
        self.setWindowTitle('Вторая программа')

        self.btn = QPushButton('111', self)
        self.btn.move(120, 340)
        self.btn.clicked.connect(self.run)

        self.file_name = QLineEdit(self)
        self.file_name.move(140, 20)
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.image.move(1280,260)
        self.image.resize(250,250)
        self.image.setPixmap(self.pixmap)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())