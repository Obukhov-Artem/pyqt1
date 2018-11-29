import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('my.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        if self.radioButton.isChecked():
            self.label.setStyleSheet("QLabel { background-color : red}")
        if self.radioButton_2.isChecked():
            self.label.setStyleSheet("QLabel { background-color : blue}")
        if self.radioButton_3.isChecked():
            self.label.setStyleSheet("QLabel { background-color : green}")
        if self.radioButton_6.isChecked():
            self.label_2.setStyleSheet("QLabel { background-color : red}")
        if self.radioButton_4.isChecked():
            self.label_2.setStyleSheet("QLabel { background-color : blue}")
        if self.radioButton_5.isChecked():
            self.label_2.setStyleSheet("QLabel { background-color : green}")
        if self.radioButton_9.isChecked():
            self.label_3.setStyleSheet("QLabel { background-color : red}")
        if self.radioButton_7.isChecked():
            self.label_3.setStyleSheet("QLabel { background-color : blue}")
        if self.radioButton_8.isChecked():
            self.label_3.setStyleSheet("QLabel { background-color : green}")


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
