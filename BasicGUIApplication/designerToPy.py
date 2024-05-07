# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtDesignerFirstScreen.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(804, 603)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.butttonSendMessage = QtWidgets.QPushButton(self.centralwidget)
        self.butttonSendMessage.setGeometry(QtCore.QRect(360, 400, 121, 41))
        self.butttonSendMessage.setTabletTracking(True)
        self.butttonSendMessage.setObjectName("butttonSendMessage")
        self.labelShowMessage = QtWidgets.QLabel(self.centralwidget)
        self.labelShowMessage.setGeometry(QtCore.QRect(310, 80, 211, 141))
        self.labelShowMessage.setMouseTracking(True)
        self.labelShowMessage.setAutoFillBackground(True)
        self.labelShowMessage.setScaledContents(False)
        self.labelShowMessage.setWordWrap(True)
        self.labelShowMessage.setOpenExternalLinks(False)
        self.labelShowMessage.setObjectName("labelShowMessage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuFile.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.butttonSendMessage.setText(_translate("MainWindow", "Send"))
        self.labelShowMessage.setText(_translate("MainWindow", "My First label with designer"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
