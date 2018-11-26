from PyQt5.QtWidgets import QApplication, QWidget,QPushButton, QLineEdit,QLabel,QLCDNumber
from PyQt5.QtGui import QPixmap
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 200, 220)
        self.setWindowTitle('Калькулятор')

        ## QLCDNumber для отображения введённых чисел и результатов
        self.table = QLCDNumber(self)
        self.table.display('')
        self.table.move(10,10)
        self.table.resize(180,30)

        ## Создание и размещение на экране кнопок, отвечающих за цифры 1-9
        self.buttons_dig = [QPushButton(str(i),self) for i in range(1,10)]
        k1,k2 = 0,1
        for i in range(9):
            if (i in [0,3,6]):
                k2+=1
                k1 = 0
            k1+=50
            self.buttons_dig[i].move(k1,k2*30)
        ## Создание и размещение на экране кнопок, отвечающих за цифру 0
        self.buttons_dig.append(QPushButton('0',self))
        self.buttons_dig[9].move(100,150)
        ## Создание и размещение на экране кнопок, отвечающих за разделитель целой и дробной части
        self.buttons_dig.append(QPushButton('.',self))
        self.buttons_dig[10].move(150,150)
        ## Подключение функционала к кнопкам
        for i in self.buttons_dig:
            i.clicked.connect(self.run)

        ## Создание и размещение на экране кнопок, отвечающих за математические опрации и очистку экрана
        self.plus_btn = QPushButton('+',self)
        self.plus_btn.move(5,60)
        self.minus_btn = QPushButton('-',self)
        self.minus_btn.move(5, 90)
        self.divise_btn = QPushButton('/',self)
        self.divise_btn.move(5,120)
        self.mult_btn = QPushButton('*',self)
        self.mult_btn.move(5,150)
        self.eq_btn = QPushButton('=',self)
        self.eq_btn.move(50,150)
        self.clear_btn = QPushButton('C',self)
        self.clear_btn.move(0,180)
        self.clear_btn.resize(200,30)
        self.clear_btn.clicked.connect(self.clear)

        for i in (self.plus_btn,self.minus_btn,self.mult_btn,self.divise_btn):
            i.clicked.connect(self.calc)

        self.eq_btn.clicked.connect(self.result)

        ## Переменная, в которых хранятся последнее введённое число/результат вычисленного выражения
        self.data = ''
        ## Переменная, в которых хранятся выражение, которое нужно подсчитать
        self.data_eval = ''


    def run(self):
        ## Формируется число, с помощью нажатий кнопок и отображается на дисплее
        if self.sender().text()=='.':
            if '.' in self.data:
                return
        if self.data!='0' or (self.data=='0' and self.sender().text()=='.'):
            self.data = self.data+self.sender().text()
            self.data_eval = self.data_eval+self.sender().text()
            self.table.display(self.data)
        else:
            self.data = self.sender().text()
            self.data_eval = self.sender().text()
            self.table.display(self.data)


    def clear(self):
        self.data = ''
        self.data_eval = ''
        self.table.display('')

    def result(self):
        ## Происходит попытка вычисления выражения, в случае попытки деления на 0, выводится ошибка
        try:
            float(self.data_eval)
        except:
            try:
                self.data = eval(self.data_eval)
                self.data_eval = str(self.data)
                self.table.display(self.data)
            except ZeroDivisionError:
                self.table.display('Error')
            except:
                pass
        self.data = ''


    def calc(self):
        ## Происходит вычисление текущего выражения и дописывается новый знак. Если последним был уже знак действия, то он менятся.
        if self.data_eval:
            self.result()
            if (self.data_eval[-1] not in ['+','-','/','*']):
                self.data_eval += self.sender().text()
            else:
                self.data_eval = self.data_eval[0:len(self.data_eval)-1] + self.sender().text()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())