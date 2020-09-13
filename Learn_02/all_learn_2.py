from PyQt5 import QtCore, QtGui, QtWidgets

class spray_c(QtWidgets.QWidget):
	def __init__(self, centralwidget, icon, icon1):					#	def __init__(self, icon, icon1):
		super(spray_c, self).__init__()

		self.S1_val = 0

		#######################################################

		self.pb_up_ob = QtWidgets.QPushButton(centralwidget)			#	self.pb_up_ob = QtWidgets.QPushButton(self.centralwidget)
		self.pb_up_ob.setGeometry(QtCore.QRect(90, 40, 75, 101))
		self.pb_up_ob.setStyleSheet("background-color:white;")
		self.pb_up_ob.setText("")
		# icon = QtGui.QIcon()
		# icon.addPixmap(QtGui.QPixmap("up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pb_up_ob.setIcon(icon)
		self.pb_up_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_up_ob.setObjectName("pb_up_ob")

		#######################################################

		self.pb_dn_ob = QtWidgets.QPushButton(centralwidget)			#	self.pb_dn_ob = QtWidgets.QPushButton(self.centralwidget)
		self.pb_dn_ob.setGeometry(QtCore.QRect(90, 270, 75, 101))
		self.pb_dn_ob.setStyleSheet("background-color:white;")
		self.pb_dn_ob.setText("")
		# icon1 = QtGui.QIcon()
		# icon1.addPixmap(QtGui.QPixmap("down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.pb_dn_ob.setIcon(icon1)
		self.pb_dn_ob.setIconSize(QtCore.QSize(60, 60))
		self.pb_dn_ob.setObjectName("pb_dn_ob")

		#######################################################

		self.lcdNumber_ob = QtWidgets.QLCDNumber(centralwidget)
		self.lcdNumber_ob.setGeometry(QtCore.QRect(243, 172, 101, 71))
		self.lcdNumber_ob.setObjectName("lcdNumber_ob")

		#######################################################

		self.plainTextEdit_ob = QtWidgets.QPlainTextEdit(centralwidget)
		self.plainTextEdit_ob.setGeometry(QtCore.QRect(80, 170, 104, 71))
		self.plainTextEdit_ob.setObjectName("plainTextEdit_ob")

		#######################################################

		#######################################################

