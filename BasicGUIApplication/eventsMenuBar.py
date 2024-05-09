from MenuBar import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMainWindow, QFileDialog



class Events(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menuBarUi = Ui_MainWindow()
        self.menuBarUi.setupUi(self)
        self.menuBarUi.actionImport.triggered.connect(self.importImage)
        self.menuBarUi.actionSave.triggered.connect(self.saveFile)


    def importImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        fileName, _ = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()", "", "All Files (*);;Image Files (*.jpg *.png)", options=options)
        if fileName:
            self.menuBarUi.label.setPixmap(QtGui.QPixmap(fileName))
            self.menuBarUi.label.adjustSize()

    def saveFile(self):
        pass




