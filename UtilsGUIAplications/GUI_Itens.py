from events import Events
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = Events()
window.show()
sys.exit(app.exec_())
