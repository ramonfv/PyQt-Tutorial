from events import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class ManagerEvents(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.clearButton.clicked.connect(self.clearItems)
        self.ui.sendButton.clicked.connect(self.publishItems)
        
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
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = ManagerEvents()
    MainWindow.show()
    sys.exit(app.exec_())