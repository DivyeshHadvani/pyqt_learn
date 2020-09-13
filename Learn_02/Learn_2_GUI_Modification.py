
from PyQt5 import QtCore, QtGui, QtWidgets
from all_learn_2 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.spray_ob = spray_c(self.centralwidget, icon, icon1,)       #   self.spray_ob = spray_c(icon, icon1,)

        #self.S1_val = 0
        self.on_clicks()


    def on_clicks(self):
        self.spray_ob.pb_up_ob.clicked.connect(self.pb_up_ob_clicked)
        self.spray_ob.pb_dn_ob.clicked.connect(self.pb_dn_ob_clicked)


    ######################################################################

    def up_check(self,current_val):
        if abs(current_val)>=0 and abs(current_val)<9:
            return True
        else:
            return False

    def down_check(self, current_val):
        if abs(current_val)>0 and abs(current_val)<=9:
            return True
        else:
            return False

    ######################################################################

    def pb_up_ob_clicked(self):
        if self.up_check(self.spray_ob.S1_val):
            self.spray_ob.S1_val +=1
            a = str(self.spray_ob.S1_val)
            print("Clicked")
            self.spray_ob.lcdNumber_ob.display(self.spray_ob.S1_val)
            #self.spray_ob.plainTextEdit_ob.setPlainText("Add")
            #self.spray_ob.plainTextEdit_ob.setPlainText(a)
            self.spray_ob.plainTextEdit_ob.setPlainText("Add")
            self.spray_ob.plainTextEdit_ob.appendPlainText(a)
        pass

    def pb_dn_ob_clicked(self):
        if self.down_check(self.spray_ob.S1_val):
            self.spray_ob.S1_val -=1
            print("Clicked")
            self.spray_ob.lcdNumber_ob.display(self.spray_ob.S1_val)
            self.spray_ob.plainTextEdit_ob.setPlainText("Remove")
        pass
    
    ######################################################################


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

