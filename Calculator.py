# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:02:00 2021

@author: skama
"""
import PyQt5

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
  
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Calculator ")
  
        # setting geometry
        self.setGeometry(100, 100, 360, 350)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
        # method for widgets
    def UiComponents(self):
  
        # creating a label
        self.label = QLabel(self)
  
        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 70)
  
        # creating label multi line
        self.label.setWordWrap(True)
  
        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid black;"
                                 "background : white;"
                                 "}")
  
        # setting alignment to the label
        self.label.setAlignment(Qt.AlignRight)
  
        # setting font
        self.label.setFont(QFont('Arial', 15))
  
  
        # adding number button to the screen
        # creating a push button
        btn1 = QPushButton("1", self)
  
        # setting geometry
        btn1.setGeometry(5, 150, 80, 40)
  
        # creating a push button
        btn2 = QPushButton("2", self)
  
        # setting geometry
        btn2.setGeometry(95, 150, 80, 40)
  
        # creating a push button
        btn3 = QPushButton("3", self)
  
        # setting geometry
        btn3.setGeometry(185, 150, 80, 40)
  
        # creating a push button
        btn4 = QPushButton("4", self)
  
        # setting geometry
        btn4.setGeometry(5, 200, 80, 40)
  
        # creating a push button
        btn5 = QPushButton("5", self)
  
        # setting geometry
        btn5.setGeometry(95, 200, 80, 40)
  
        # creating a push button
        btn6 = QPushButton("5", self)
  
        # setting geometry
        btn6.setGeometry(185, 200, 80, 40)
  
        # creating a push button
        btn7 = QPushButton("7", self)
  
        # setting geometry
        btn7.setGeometry(5, 250, 80, 40)
  
        # creating a push button
        btn8 = QPushButton("8", self)
  
        # setting geometry
        btn8.setGeometry(95, 250, 80, 40)
  
        # creating a push button
        btn9 = QPushButton("9", self)
  
        # setting geometry
        btn9.setGeometry(185, 250, 80, 40)
  
        # creating a push button
        btn0 = QPushButton("0", self)
  
        # setting geometry
        btn0.setGeometry(5, 300, 80, 40)
  
        # adding operator push button
        # creating push button
        btnequal = QPushButton("=", self)
  
        # setting geometry
        btnequal.setGeometry(275, 300, 80, 40)
  
        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        btnequal.setGraphicsEffect(c_effect)
  
        # creating push button
        btn_plus = QPushButton("+", self)
  
        # setting geometry
        btn_plus.setGeometry(275, 250, 80, 40)
  
        # creating push button
        btn_minus = QPushButton("-", self)
  
        # setting geometry
        btn_minus.setGeometry(275, 200, 80, 40)
  
        # creating push button
        btn_mul = QPushButton("*", self)
  
        # setting geometry
        btn_mul.setGeometry(275, 150, 80, 40)
  
        # creating push button
        btn_div = QPushButton("/", self)
  
        # setting geometry
        btn_div.setGeometry(185, 300, 80, 40)
  
        # creating push button
        btn_point = QPushButton(".", self)
  
        # setting geometry
        btn_point.setGeometry(95, 300, 80, 40)
  
  
        # clear button
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 200, 40)
  
        # del one character button
        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 145, 40)
  
        # adding action to each of the button
        btn_minus.clicked.connect(self.calc_minus)
        btnequal.clicked.connect(self.action_equal)
        btn0.clicked.connect(self.set0)
        btn1.clicked.connect(self.set1)
        btn2.clicked.connect(self.set2)
        btn3.clicked.connect(self.set3)
        btn4.clicked.connect(self.set4)
        btn5.clicked.connect(self.set5)
        btn6.clicked.connect(self.set6)
        btn7.clicked.connect(self.set7)
        btn8.clicked.connect(self.set8)
        btn9.clicked.connect(self.set9)
        btn_div.clicked.connect(self.calc_div)
        btn_mul.clicked.connect(self.calc_mul)
        btn_plus.clicked.connect(self.calc_plus)
        btn_point.clicked.connect(self.dec_pnt)
        push_clear.clicked.connect(self.clear)
        push_del.clicked.connect(self.calc_del)
  
  
    def action_equal(self):
  
        # get the label text
        equation = self.label.text()
  
        try:
            # getting the ans
            ans = eval(equation)
  
            # setting text to the label
            self.label.setText(str(ans))
  
        except:
            # setting text to the label
            self.label.setText("Wrong Input")
  
    def calc_plus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " + ")
  
    def calc_minus(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " - ")
  
    def calc_div(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " / ")
  
    def calc_mul(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + " * ")
  
    def dec_pnt(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + ".")
  
    def set0(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "0")
  
    def set1(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "1")
  
    def set2(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "2")
  
    def set3(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "3")
  
    def set4(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "4")
  
    def set5(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "5")
  
    def set6(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "6")
  
    def set7(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "7")
  
    def set8(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "8")
  
    def set9(self):
        # appending label text
        text = self.label.text()
        self.label.setText(text + "9")
  
    def clear(self):
        # clearing the label text
        self.label.setText("")
  
    def calc_del(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text)-1])
        self.label.setText(text[:len(text)-1])
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())