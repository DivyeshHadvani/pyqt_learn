# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Learn_03.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from all_Learn_3 import *
import threading
import time

import serial
import serial.tools.list_ports

from PyQt5.QtCore import *

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(640, 480)
		MainWindow.setMinimumSize(QtCore.QSize(7, 0))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		l = threading.current_thread().getName()
		print("l",l)
		
		self.plainTextEdit_ob = QtWidgets.QPlainTextEdit(self.centralwidget)
		self.plainTextEdit_ob.setGeometry(QtCore.QRect(20, 290, 441, 121))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.plainTextEdit_ob.setFont(font)
		self.plainTextEdit_ob.setObjectName("plainTextEdit_ob")

		self.widget = QtWidgets.QWidget(self.centralwidget)
		self.widget.setGeometry(QtCore.QRect(20, 20, 438, 256))
		self.widget.setObjectName("widget")
		self.gridLayout = QtWidgets.QGridLayout(self.widget)
		self.gridLayout.setContentsMargins(0, 0, 0, 0)
		self.gridLayout.setObjectName("gridLayout")

		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../Learn_03/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../Learn_03/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		  
		self.label = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap("../Learn_03/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

		icon1 = QtGui.QIcon()
		icon1.addPixmap(QtGui.QPixmap("../Learn_03/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		
		# self.spray_ob = spray_c(self.centralwidget, icon, icon1,)      
		self.spray_ob = spray_c(self.widget, icon, icon1,)

		self.gridLayout.addLayout(self.spray_ob.verticalLayout, 0, 1, 1, 1)

		self.label_2 = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
		
		
		self.gridLayout.addLayout(self.spray_ob.verticalLayout_2, 0, 3, 1, 1)
		
		self.label_3 = QtWidgets.QLabel(self.widget)
		font = QtGui.QFont()
		font.setPointSize(10)
		self.label_3.setFont(font)
		self.label_3.setObjectName("label_3")
		self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
		
		
		self.gridLayout.addLayout(self.spray_ob.verticalLayout_3, 0, 5, 1, 1)
		
		self.widget1 = QtWidgets.QWidget(self.centralwidget)
		self.widget1.setGeometry(QtCore.QRect(520, 130, 62, 128))
		self.widget1.setObjectName("widget1")
		
		self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
		self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout_4.setObjectName("verticalLayout_4")
		
		self.pb_start_ob = QtWidgets.QPushButton(self.widget1)
		self.pb_start_ob.setMinimumSize(QtCore.QSize(60, 60))
		self.pb_start_ob.setMaximumSize(QtCore.QSize(60, 60))
		self.pb_start_ob.setObjectName("pb_start_ob")
		
		self.verticalLayout_4.addWidget(self.pb_start_ob)
		
		self.pb_stop_ob = QtWidgets.QPushButton(self.widget1)
		self.pb_stop_ob.setMinimumSize(QtCore.QSize(60, 60))
		self.pb_stop_ob.setMaximumSize(QtCore.QSize(60, 60))
		self.pb_stop_ob.setObjectName("pb_stop_ob")
		
		self.verticalLayout_4.addWidget(self.pb_stop_ob)


		
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


		# change_S1_val = pyqtSignal(int)


		self.on_clicks()


	def on_clicks(self):
		self.spray_ob.pb_up_s_ob.clicked.connect(self.pb_up_s_ob_clicked)
		self.spray_ob.pb_dn_s_ob.clicked.connect(self.pb_dn_s_ob_clicked)
		self.spray_ob.pb_up_d_ob.clicked.connect(self.pb_up_d_ob_clicked)
		self.spray_ob.pb_dn_d_ob.clicked.connect(self.pb_dn_d_ob_clicked)
		self.spray_ob.pb_up_c_ob.clicked.connect(self.pb_up_c_ob_clicked)
		self.spray_ob.pb_dn_c_ob.clicked.connect(self.pb_dn_c_ob_clicked)
		self.pb_start_ob.clicked.connect(self.pb_start_ob_clicked)
		self.pb_stop_ob.clicked.connect(self.pb_stop_ob_clicked)


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

	def pb_up_s_ob_clicked(self):
		if self.up_check(self.spray_ob.S1_val):
			self.spray_ob.S1_val +=1
			# a = str(self.spray_ob.S1_val)
			print("Clicked")
			self.spray_ob.lcdNumber_ob.display(self.spray_ob.S1_val)
			
		pass

	def pb_dn_s_ob_clicked(self):
		if self.down_check(self.spray_ob.S1_val):
			self.spray_ob.S1_val -=1
			print("Clicked")
			self.spray_ob.lcdNumber_ob.display(self.spray_ob.S1_val)
			
		pass

	def pb_up_d_ob_clicked(self):
		if self.up_check(self.spray_ob.D1_val):
			self.spray_ob.D1_val +=1
			# a = str(self.spray_ob.S1_val)
			print("Clicked")
			self.spray_ob.lcdNumber_ob_2.display(self.spray_ob.D1_val)
			
		pass

	def pb_dn_d_ob_clicked(self):
		if self.down_check(self.spray_ob.D1_val):
			self.spray_ob.D1_val -=1
			print("Clicked")
			self.spray_ob.lcdNumber_ob_2.display(self.spray_ob.D1_val)
			
		pass

	def pb_up_c_ob_clicked(self):
		if self.up_check(self.spray_ob.C1_val):
			self.spray_ob.C1_val +=1
			# a = str(self.spray_ob.S1_val)
			print("Clicked")
			self.spray_ob.lcdNumber_ob_3.display(self.spray_ob.C1_val)
			
		pass

	def pb_dn_c_ob_clicked(self):
		if self.down_check(self.spray_ob.C1_val):
			self.spray_ob.C1_val -=1
			print("Clicked")
			self.spray_ob.lcdNumber_ob_3.display(self.spray_ob.C1_val)
			
		pass
	
	#########################################################################################################

	def pb_start_ob_clicked(self):

		print("start_clicked")

		n = threading.current_thread().getName()
		print('n',n)

		self.temp_S1_val = self.spray_ob.S1_val
		self.temp_D1_val = self.spray_ob.D1_val
		self.temp_C1_val = self.spray_ob.C1_val


		# self.spray_ob.S1_val


		t1 = threading.Thread(target=self.spraytime,name="spray_thread")
		t2 = threading.Thread(target=self.drytime,name="dry_thread")
		t3 = threading.Thread(target=self.cycletime,name="cycle_thread")

		# self.t1.change_S1_val.connect(self.setPT)

		t1.start()
		t2.start()
		t3.start()
		
		pass

	def pb_stop_ob_clicked(self):
		pass

	def setPT(self,ti):
		self.plainTextEdit_ob.setPlainText("Add_S")
		self.plainTextEdit_ob.appendPlainText(ti)



	######################################################################

	def spraytime(self):

		m = threading.current_thread().getName()
		print('m',m)
		
		while self.temp_S1_val >0:
			# change_S1_val = pyqtSignal(int)

			self.temp_S1_val -=1

			a = str(self.temp_S1_val)
			# self.change_S1_val.emit(int)		#	self.spray_ob.S1_val
			print("spraytime")
			self.plainTextEdit_ob.setPlainText("Add_S")
			self.plainTextEdit_ob.appendPlainText(a)

			time.sleep(1)
		pass

	def drytime(self):
		while self.temp_D1_val >0:
			self.temp_D1_val -=1

		# b = str(self.spray_ob.D1_val)
		# self.spray_ob.plainTextEdit_ob.setPlainText("Add_D")
		# self.spray_ob.plainTextEdit_ob.appendPlainText(b)

			print("drytime")
			print(self.temp_D1_val)
			time.sleep(1)
		pass

	def cycletime(self):
		# self.spray_ob.C1_val -=1

		# c = str(self.spray_ob.C1_val)
		# self.spray_ob.plainTextEdit_ob.setPlainText("Add_C")
		# self.spray_ob.plainTextEdit_ob.appendPlainText(c)

		# time.sleep(1)
		pass


	######################################################################



		


	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Spray Time :-"))
		self.label_2.setText(_translate("MainWindow", "Dry Time :-"))
		self.label_3.setText(_translate("MainWindow", "Cycle :-"))
		self.pb_start_ob.setText(_translate("MainWindow", "Start"))
		self.pb_stop_ob.setText(_translate("MainWindow", "Stop"))


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

