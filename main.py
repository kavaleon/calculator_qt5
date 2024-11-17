from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.result = '0'
        self.screen = QLabel(self.result)

        self.btn_0 = QPushButton('0')
        self.btn_1 = QPushButton('1')
        self.btn_2 = QPushButton('2')
        self.btn_3 = QPushButton('3')
        self.btn_4 = QPushButton('4')
        self.btn_5 = QPushButton('5')
        self.btn_6 = QPushButton('6')
        self.btn_7 = QPushButton('7')
        self.btn_8 = QPushButton('8')
        self.btn_9 = QPushButton('9')

        self.btn_neg = QPushButton('+/-')
        self.btn_сom = QPushButton('.')
        self.btn_equal = QPushButton('=')

        self.btn_minus = QPushButton('-')
        self.btn_plus = QPushButton('+')
        self.btn_incr = QPushButton('×')
        self.btn_div = QPushButton('/')
        self.btn_del = QPushButton('←')
        self.btn_clear = QPushButton('C')
        self.btn_per = QPushButton('%')

        h_1 = QHBoxLayout()
        h_1.addWidget(self.screen, alignment=Qt.AlignRight)

        h_2 = QHBoxLayout()
        h_2.addWidget(self.btn_per)
        h_2.addWidget(self.btn_clear)
        h_2.addWidget(self.btn_del)
        h_2.addWidget(self.btn_div)

        h_3 = QHBoxLayout()
        h_3.addWidget(self.btn_7)
        h_3.addWidget(self.btn_8)
        h_3.addWidget(self.btn_9)
        h_3.addWidget(self.btn_incr)

        h_4 = QHBoxLayout()
        h_4.addWidget(self.btn_4)
        h_4.addWidget(self.btn_5)
        h_4.addWidget(self.btn_6)
        h_4.addWidget(self.btn_minus)

        h_5 = QHBoxLayout()
        h_5.addWidget(self.btn_1)
        h_5.addWidget(self.btn_2)
        h_5.addWidget(self.btn_3)
        h_5.addWidget(self.btn_plus)

        h_6 = QHBoxLayout()
        h_6.addWidget(self.btn_neg)
        h_6.addWidget(self.btn_0)
        h_6.addWidget(self.btn_сom)
        h_6.addWidget(self.btn_equal)

        self.btn_0.clicked.connect(lambda: self.press('0'))
        self.btn_1.clicked.connect(lambda: self.press('1'))
        self.btn_2.clicked.connect(lambda: self.press('2'))
        self.btn_3.clicked.connect(lambda: self.press('3'))
        self.btn_4.clicked.connect(lambda: self.press('4'))
        self.btn_5.clicked.connect(lambda: self.press('5'))
        self.btn_6.clicked.connect(lambda: self.press('6'))
        self.btn_7.clicked.connect(lambda: self.press('7'))
        self.btn_8.clicked.connect(lambda: self.press('8'))
        self.btn_9.clicked.connect(lambda: self.press('9'))

        self.btn_del.clicked.connect(lambda: self.delete())
        self.btn_neg.clicked.connect(lambda: self.plus_minus())
        self.btn_сom.clicked.connect(lambda: self.dot())
        self.btn_clear.clicked.connect(lambda: self.press("C"))

        self.btn_minus.clicked.connect(lambda: self.press('-'))
        self.btn_plus.clicked.connect(lambda: self.press('+'))
        self.btn_incr.clicked.connect(lambda: self.press('*'))
        self.btn_div.clicked.connect(lambda: self.press('/'))
        self.btn_per.clicked.connect(lambda: self.press('%'))

        self.btn_equal.clicked.connect(lambda: self.math())

        v = QVBoxLayout(self)
        v.addLayout(h_1)
        v.addLayout(h_2)
        v.addLayout(h_3)
        v.addLayout(h_4)
        v.addLayout(h_5)
        v.addLayout(h_6)


    def math(self):
        try:
            answer = eval(self.screen.text())
            self.screen.setText(str(answer))
        except:
            self.screen.setText("ERROR")

    def press(self, pressed):
        if pressed == "C":
            self.screen.setText("0")
        else:
            if self.screen.text() == "0":
                self.screen.setText("")
            self.screen.setText(f'{self.screen.text()}{pressed}')

    def delete(self):
        self.screen.setText(self.screen.text()[:-1])

    def plus_minus(self):
        if "-" in self.screen.text():
            self.screen.setText(self.screen.text().replace("-", ""))
        else:
            self.screen.setText(f'-{self.screen.text()}')

    def dot(self):
        if self.screen.text()[-1] == ".":
            pass
        else:
            self.screen.setText(f'{self.screen.text()}.')



def main():
    app = QApplication([])
    w = MainWindow()
    w.setWindowTitle('Калькулятор')
    w.resize(400, 600)
    w.show()
    app.exec_()

main()