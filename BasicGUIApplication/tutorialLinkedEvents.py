from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self, title, messageToShow):
        super(MyWindow, self).__init__()
        self.messageToShow = messageToShow
        self.setGeometry(200,200,400,400)
        self.setWindowTitle(title)
        self.initUi()

    def initUi(self):
        self.label = QLabel(self)
        self.label.setStyleSheet("border: 1px solid black;") 
        self.label.move(50, 50)

        self.button1 = QPushButton(self)
        self.button1.setText("PushButton")
        self.button1.adjustSize()
        # self.label.move(50, 50)
        self.button1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText(self.messageToShow)
        self.uptadeLabel()

    def uptadeLabel(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow("PyQt Tutorial", "Pressed Button")
    win.show()
    sys.exit(app.exec_())

window()