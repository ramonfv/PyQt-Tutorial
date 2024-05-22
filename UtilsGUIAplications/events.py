from uavItems import Ui_MainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QHBoxLayout, QSizePolicy

class Events(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uavUi = Ui_MainWindow()
        self.uavUi.setupUi(self)
        self.turnOn()
        self.uavUi.all.clicked.connect(lambda: self.showLinearVelocity(self.getItems(), None))
        self.uavUi.submit.clicked.connect(lambda: self.showLinearVelocity(self.getItems()))
        self.uavUi.titleWindow.adjustSize()
        self.uavUi.showVel.hide()

    def turnOn(self):
        for i in range(self.uavUi.listWidget.count()):
            item = self.uavUi.listWidget.item(i)
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)

    def allItems(self):
        items = []
        for i in range(self.uavUi.listWidget.count()):
            item = self.uavUi.listWidget.item(i)
            item.setCheckState(Qt.Checked)
            items.append(item)
        return items

    def submitItems(self):
        items = []
        for i in range(self.uavUi.listWidget.count()):
            item = self.uavUi.listWidget.item(i)
            if item.checkState() == Qt.Checked:
                items.append(item)
        return items
    
    def getItems(self):       
        sender = self.sender()
        items = []
        if sender == self.uavUi.all:
                items = self.allItems()
        elif sender == self.uavUi.submit:
                items = self.submitItems()
        return items
    
    def createLabel(self, value):
        label = QLabel("")
        label.setStyleSheet("border: 1px solid black;") 
        label.setText(value)
        return label.text()
    
   
    def showLinearVelocity(self, items, msg=None):
        self.uavUi.showVel.show()  
        for item in items:
                    variable = f"Velocidade Linear {item.text()}: {self.createLabel(msg)}"                   
                    width = variable.__len__()
                    self.uavUi.showVariables.addItem(variable)

        self.uavUi.showVel.setMinimumWidth(width+400)
        self.uavUi.showVariables.setMinimumWidth(width+100)    


