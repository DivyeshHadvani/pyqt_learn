# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Learn_2_GUI.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pb_up_ob = QtWidgets.QPushButton(self.centralwidget)
        self.pb_up_ob.setGeometry(QtCore.QRect(90, 40, 75, 101))
        self.pb_up_ob.setStyleSheet("background-color:white;")
        self.pb_up_ob.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_up_ob.setIcon(icon)
        self.pb_up_ob.setIconSize(QtCore.QSize(60, 60))
        self.pb_up_ob.setObjectName("pb_up_ob")
        self.pb_dn_ob = QtWidgets.QPushButton(self.centralwidget)
        self.pb_dn_ob.setGeometry(QtCore.QRect(90, 270, 75, 101))
        self.pb_dn_ob.setStyleSheet("background-color:white;")
        self.pb_dn_ob.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_dn_ob.setIcon(icon1)
        self.pb_dn_ob.setIconSize(QtCore.QSize(60, 60))
        self.pb_dn_ob.setObjectName("pb_dn_ob")
        self.lcdNumber_ob = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_ob.setGeometry(QtCore.QRect(243, 172, 101, 71))
        self.lcdNumber_ob.setObjectName("lcdNumber_ob")
        self.plainTextEdit_ob = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_ob.setGeometry(QtCore.QRect(80, 170, 104, 71))
        self.plainTextEdit_ob.setObjectName("plainTextEdit_ob")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

