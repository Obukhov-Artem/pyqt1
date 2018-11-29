# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(472, 329)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(30, 10, 82, 17))
        self.radioButton.setAutoFillBackground(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 50, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(Form)
        self.radioButton_4.setGeometry(QtCore.QRect(130, 30, 82, 17))
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(Form)
        self.radioButton_5.setGeometry(QtCore.QRect(130, 50, 82, 17))
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(Form)
        self.radioButton_6.setGeometry(QtCore.QRect(130, 10, 82, 17))
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(Form)
        self.radioButton_7.setGeometry(QtCore.QRect(250, 30, 82, 17))
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(Form)
        self.radioButton_8.setGeometry(QtCore.QRect(250, 50, 82, 17))
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(Form)
        self.radioButton_9.setGeometry(QtCore.QRect(250, 10, 82, 17))
        self.radioButton_9.setObjectName("radioButton_9")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 130, 361, 51))
        self.label.setAutoFillBackground(True)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(90, 190, 361, 51))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 250, 361, 51))
        self.label_3.setAutoFillBackground(True)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(360, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Flag"))
        self.radioButton.setText(_translate("Form", "Red"))
        self.radioButton_2.setText(_translate("Form", "Blue"))
        self.radioButton_3.setText(_translate("Form", "Green"))
        self.radioButton_4.setText(_translate("Form", "Blue"))
        self.radioButton_5.setText(_translate("Form", "Green"))
        self.radioButton_6.setText(_translate("Form", "Red"))
        self.radioButton_7.setText(_translate("Form", "Blue"))
        self.radioButton_8.setText(_translate("Form", "Green"))
        self.radioButton_9.setText(_translate("Form", "Red"))
        self.pushButton.setText(_translate("Form", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

