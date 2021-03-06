from PyQt5 import QtCore, QtGui, QtWidgets

class spray_c(QtWidgets.QWidget):
	# def __init__(self, centralwidget, icon, icon1):		#	def __init__(self, icon, icon1):
	def __init__(self, widget, icon, icon1):
		super(spray_c, self).__init__()

		self.S1_val = 0
		self.D1_val = 0
		self.C1_val = 0

		#########################################################################################################################

		# self.widget = QtWidgets.QWidget(centralwidget)				#	self.widget = QtWidgets.QWidget(self.centralwidget)
		# self.widget.setGeometry(QtCore.QRect(20, 20, 438, 256))
		# self.widget.setObjectName("widget")
		# self.gridLayout = QtWidgets.QGridLayout(self.widget)
		# self.gridLayout.setContentsMargins(0, 0, 0, 0)
		# self.gridLayout.setObjectName("gridLayout")

		########################################################################################

		#######################################################

		# self.label = QtWidgets.QLabel(self.widget)
		# font = QtGui.QFont()
		# font.setPointSize(10)
		# self.label.setFont(font)
		# self.label.setObjectName("label")
		# self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.verticalLayout = QtWidgets.QVBoxLayout()
		self.verticalLayout.setObjectName("verticalLayout")

		# self.label.setText(_translate("MainWindow", "Spray Time :-"))
		
		#######################################################

		self.pb_up_s_ob = QtWidgets.QPushButton(widget)			#	self.pb_up_s_ob = QtWidgets.QPushButton(self.widget)
		self.pb_up_s_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_up_s_ob.setMaximumSize(QtCore.QSize(60, 80))
		self.pb_up_s_ob.setStyleSheet("background-color:white;")
		self.pb_up_s_ob.setText("")
		
		self.pb_up_s_ob.setIcon(icon)
		self.pb_up_s_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_up_s_ob.setObjectName("pb_up_s_ob")
		
		#######################################################

		self.lcdNumber_ob = QtWidgets.QLCDNumber(widget)		#	self.lcdNumber_ob = QtWidgets.QLCDNumber(self.widget)
		self.lcdNumber_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob.setMaximumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob.setObjectName("lcdNumber_ob")
		

		#######################################################

		self.pb_dn_s_ob = QtWidgets.QPushButton(widget)		#	self.pb_dn_s_ob = QtWidgets.QPushButton(self.widget)
		self.pb_dn_s_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_dn_s_ob.setMaximumSize(QtCore.QSize(70, 80))
		self.pb_dn_s_ob.setStyleSheet("background-color:white;")
		self.pb_dn_s_ob.setText("")

		self.pb_dn_s_ob.setIcon(icon1)
		self.pb_dn_s_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_dn_s_ob.setObjectName("pb_dn_s_ob")

		#######################################################

		self.verticalLayout.addWidget(self.pb_up_s_ob)
		self.verticalLayout.addWidget(self.lcdNumber_ob)
		self.verticalLayout.addWidget(self.pb_dn_s_ob)

		#self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
		
		########################################################################################

		# self.label_2 = QtWidgets.QLabel(self.widget)
		# font = QtGui.QFont()
		# font.setPointSize(10)
		# self.label_2.setFont(font)
		# self.label_2.setObjectName("label_2")
		# self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")

		# self.label_2.setText(_translate("MainWindow", "Dry Time :-"))
		
		self.pb_up_d_ob = QtWidgets.QPushButton(widget)			#	self.pb_up_d_ob = QtWidgets.QPushButton(self.widget)
		self.pb_up_d_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_up_d_ob.setMaximumSize(QtCore.QSize(60, 80))
		self.pb_up_d_ob.setStyleSheet("background-color:white;")
		self.pb_up_d_ob.setText("")
		self.pb_up_d_ob.setIcon(icon)
		self.pb_up_d_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_up_d_ob.setObjectName("pb_up_d_ob")
		
		self.lcdNumber_ob_2 = QtWidgets.QLCDNumber(widget)			#	self.lcdNumber_ob_2 = QtWidgets.QLCDNumber(self.widget)
		self.lcdNumber_ob_2.setMinimumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob_2.setMaximumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob_2.setObjectName("lcdNumber_ob_2")
		
		self.pb_dn_d_ob = QtWidgets.QPushButton(widget)		#	self.pb_dn_d_ob = QtWidgets.QPushButton(self.widget)
		self.pb_dn_d_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_dn_d_ob.setMaximumSize(QtCore.QSize(70, 80))
		self.pb_dn_d_ob.setStyleSheet("background-color:white;")
		self.pb_dn_d_ob.setText("")
		self.pb_dn_d_ob.setIcon(icon1)
		self.pb_dn_d_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_dn_d_ob.setObjectName("pb_dn_d_ob")
		
		#######################################################
		
		self.verticalLayout_2.addWidget(self.pb_up_d_ob)
		self.verticalLayout_2.addWidget(self.lcdNumber_ob_2)
		self.verticalLayout_2.addWidget(self.pb_dn_d_ob)
		
		#self.gridLayout.addLayout(self.verticalLayout_2, 0, 3, 1, 1)
		

		########################################################################################

		# self.label_3 = QtWidgets.QLabel(self.widget)
		# font = QtGui.QFont()
		# font.setPointSize(10)
		# self.label_3.setFont(font)
		# self.label_3.setObjectName("label_3")
		# self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")

		# self.label_3.setText(_translate("MainWindow", "Cycle :-"))
		
		
		self.pb_up_c_ob = QtWidgets.QPushButton(widget)			#	self.pb_up_c_ob = QtWidgets.QPushButton(self.widget)
		self.pb_up_c_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_up_c_ob.setMaximumSize(QtCore.QSize(60, 80))
		self.pb_up_c_ob.setStyleSheet("background-color:white;")
		self.pb_up_c_ob.setText("")
		self.pb_up_c_ob.setIcon(icon)
		self.pb_up_c_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_up_c_ob.setObjectName("pb_up_c_ob")


		
		self.lcdNumber_ob_3 = QtWidgets.QLCDNumber(widget)			#	self.lcdNumber_ob_3 = QtWidgets.QLCDNumber(self.widget)
		self.lcdNumber_ob_3.setMinimumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob_3.setMaximumSize(QtCore.QSize(70, 80))
		self.lcdNumber_ob_3.setObjectName("lcdNumber_ob_3")
		
		
		self.pb_dn_c_ob = QtWidgets.QPushButton(widget)			#	self.pb_dn_c_ob = QtWidgets.QPushButton(self.widget)
		self.pb_dn_c_ob.setMinimumSize(QtCore.QSize(70, 80))
		self.pb_dn_c_ob.setMaximumSize(QtCore.QSize(70, 80))
		self.pb_dn_c_ob.setStyleSheet("background-color:white;")
		self.pb_dn_c_ob.setText("")
		self.pb_dn_c_ob.setIcon(icon1)
		self.pb_dn_c_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_dn_c_ob.setObjectName("pb_dn_c_ob")
		
		#######################################################
		
		self.verticalLayout_3.addWidget(self.pb_up_c_ob)
		self.verticalLayout_3.addWidget(self.lcdNumber_ob_3)
		self.verticalLayout_3.addWidget(self.pb_dn_c_ob)
		
		#self.gridLayout.addLayout(self.verticalLayout_3, 0, 5, 1, 1)
		
		#########################################################################################################################

		# self.widget1 = QtWidgets.QWidget(centralwidget)				#	self.widget1 = QtWidgets.QWidget(self.centralwidget)
		# self.widget1.setGeometry(QtCore.QRect(520, 130, 62, 128))
		# self.widget1.setObjectName("widget1")
		
		# self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget1)
		# self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
		# self.verticalLayout_4.setObjectName("verticalLayout_4")
		
		# self.pb_start_ob = QtWidgets.QPushButton(self.widget1)
		# self.pb_start_ob.setMinimumSize(QtCore.QSize(60, 60))
		# self.pb_start_ob.setMaximumSize(QtCore.QSize(60, 60))
		# self.pb_start_ob.setObjectName("pb_start_ob")
		
		# self.verticalLayout_4.addWidget(self.pb_start_ob)
		
		# self.pb_stop_ob = QtWidgets.QPushButton(self.widget1)
		# self.pb_stop_ob.setMinimumSize(QtCore.QSize(60, 60))
		# self.pb_stop_ob.setMaximumSize(QtCore.QSize(60, 60))
		# self.pb_stop_ob.setObjectName("pb_stop_ob")
		
		# self.verticalLayout_4.addWidget(self.pb_stop_ob)

		# self.pb_start_ob.setText(_translate("MainWindow", "Start"))
		# self.pb_stop_ob.setText(_translate("MainWindow", "Stop"))
		
		#######################################################