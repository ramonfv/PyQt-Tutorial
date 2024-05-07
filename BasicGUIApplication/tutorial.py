from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("PyQt Tutorial")
    
    label = QLabel(win)
    label.setText("My first label with PyQt!")
    label.adjustSize()
    # label.clear()
    label.move(50, 50)
    # label.setStyleSheet("border: 1px solid black;") 
    
    win.show()
    sys.exit(app.exec_())

window()