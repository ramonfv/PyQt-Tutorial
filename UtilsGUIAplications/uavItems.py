# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uavItems.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 190, 274, 264))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.titleWindow = QtWidgets.QLabel(self.widget)
        self.titleWindow.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.titleWindow.setAlignment(QtCore.Qt.AlignCenter)
        self.titleWindow.setObjectName("titleWindow")
        self.gridLayout.addWidget(self.titleWindow, 0, 0, 1, 3)
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 3)
        self.all = QtWidgets.QPushButton(self.widget)
        self.all.setObjectName("all")
        self.gridLayout.addWidget(self.all, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(81, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.submit = QtWidgets.QPushButton(self.widget)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 2, 2, 1, 1)
        self.showVel = QtWidgets.QWidget(self.centralwidget)
        self.showVel.setGeometry(QtCore.QRect(370, 170, 274, 241))
        self.showVel.setObjectName("showVel")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.showVel)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.showVariables = QtWidgets.QListWidget(self.showVel)
        self.showVariables.setObjectName("showVariables")
        self.gridLayout_3.addWidget(self.showVariables, 0, 0, 1, 3)
        self.takeOff = QtWidgets.QPushButton(self.showVel)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(78, 154, 6))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.takeOff.setPalette(palette)
        self.takeOff.setObjectName("takeOff")
        self.gridLayout_3.addWidget(self.takeOff, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 1, 1, 1)
        self.land = QtWidgets.QPushButton(self.showVel)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(164, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.land.setPalette(palette)
        self.land.setObjectName("land")
        self.gridLayout_3.addWidget(self.land, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleWindow.setText(_translate("MainWindow", "Select Agents"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "UAV 1"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "UAV 2"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.all.setText(_translate("MainWindow", "All"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.takeOff.setText(_translate("MainWindow", "TakeOff"))
        self.land.setText(_translate("MainWindow", "Land"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
