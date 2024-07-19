from events import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json


class ManagerEvents(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadEventNamesFromFile('eventsName.json')
        self.ui.clearButton.clicked.connect(self.clearItems)
        self.ui.sendButton.clicked.connect(self.publishItems)
        self.ui.refreshButton.clicked.connect(self.refreshItems)
        
        
    def clearItems(self):
        for index in range(self.ui.EventsList.count()):
            item = self.ui.EventsList.item(index)
            item.setCheckState(QtCore.Qt.Unchecked)
    
    def publishItems(self):
        checked_items = []
        for index in range(self.ui.EventsList.count()):
            item = self.ui.EventsList.item(index)
            if item.checkState() == QtCore.Qt.Checked:
                checked_items.append(item.text())
        print("Selected items:", checked_items)
        
    def loadEventNamesFromFile(self, filename):
        try:
            with open(filename, 'r') as file:
                events = json.load(file)
                self.ui.EventsList.clear()
                for event in events:
                    item = QtWidgets.QListWidgetItem(event["event"])
                    item.setCheckState(QtCore.Qt.Unchecked)
                    self.ui.EventsList.addItem(item)
        except Exception as e:
            print(f"Failed to load events from {filename}: {e}")
            
    def refreshItems(self):
        self.loadEventNamesFromFile('eventsName.json')
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ManagerEvents()
    MainWindow.show()
    sys.exit(app.exec_())