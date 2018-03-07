# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_server.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyModbusTCP.client import ModbusClient
import sys
import socket

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(837, 746)
        Form.setStyleSheet("QGroupBox {\n"
"    border: 1.5px solid gray;\n"
"    border-radius: 9px;\n"
"    margin-top: 0.5em;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"    padding: 0 3px 0 3px;\n"
"}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(160, 150, 541, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 310, 451, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.connect_cookie = QtWidgets.QLabel(self.groupBox_2)
        self.connect_cookie.setGeometry(QtCore.QRect(80, 20, 91, 20))
        self.connect_cookie.setObjectName("connect_cookie")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 391, 111))
        self.groupBox.setObjectName("groupBox")
        self.measure_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.measure_s1_btn.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.measure_s1_btn.setObjectName("measure_s1_btn")
        self.done_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.done_s1_btn.setGeometry(QtCore.QRect(150, 50, 51, 28))
        self.done_s1_btn.setObjectName("done_s1_btn")
        self.measure_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.measure_s1_lbl.setGeometry(QtCore.QRect(30, 85, 91, 21))
        self.measure_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s1_lbl.setObjectName("measure_s1_lbl")
        self.done_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.done_s1_lbl.setGeometry(QtCore.QRect(170, 85, 61, 21))
        self.done_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s1_lbl.setObjectName("done_s1_lbl")
        self.warning_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.warning_s1_lbl.setGeometry(QtCore.QRect(310, 40, 71, 20))
        self.warning_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_s1_lbl.setObjectName("warning_s1_lbl")
        self.reset_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.reset_s1_btn.setEnabled(False)
        self.reset_s1_btn.setGeometry(QtCore.QRect(200, 50, 51, 28))
        self.reset_s1_btn.setObjectName("reset_s1_btn")
        self.time_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.time_s1_lbl.setGeometry(QtCore.QRect(310, 79, 71, 21))
        self.time_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl.setObjectName("time_s1_lbl")
        self.time_s1_lbl_2 = QtWidgets.QLabel(self.groupBox)
        self.time_s1_lbl_2.setGeometry(QtCore.QRect(260, 79, 51, 21))
        self.time_s1_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_2.setObjectName("time_s1_lbl_2")
        self.time_s1_lbl_3 = QtWidgets.QLabel(self.groupBox)
        self.time_s1_lbl_3.setGeometry(QtCore.QRect(260, 39, 51, 21))
        self.time_s1_lbl_3.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_3.setObjectName("time_s1_lbl_3")
        self.time_s1_lbl_4 = QtWidgets.QLabel(self.groupBox)
        self.time_s1_lbl_4.setGeometry(QtCore.QRect(260, 59, 51, 21))
        self.time_s1_lbl_4.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_4.setObjectName("time_s1_lbl_4")
        self.error_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.error_s1_lbl.setGeometry(QtCore.QRect(310, 59, 71, 20))
        self.error_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.error_s1_lbl.setObjectName("error_s1_lbl")
        self.measure_s1_lbl_2 = QtWidgets.QLabel(self.groupBox)
        self.measure_s1_lbl_2.setGeometry(QtCore.QRect(100, 10, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.measure_s1_lbl_2.setFont(font)
        self.measure_s1_lbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s1_lbl_2.setObjectName("measure_s1_lbl_2")
        self.status_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.status_s1_lbl.setGeometry(QtCore.QRect(190, 10, 91, 41))
        self.status_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_s1_lbl.setObjectName("status_s1_lbl")
        self.connect_cookie_2 = QtWidgets.QLabel(self.groupBox_2)
        self.connect_cookie_2.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.connect_cookie_2.setObjectName("connect_cookie_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 170, 391, 111))
        self.groupBox_4.setObjectName("groupBox_4")
        self.measure_s2_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.measure_s2_btn.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.measure_s2_btn.setObjectName("measure_s2_btn")
        self.done_s2_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.done_s2_btn.setGeometry(QtCore.QRect(150, 50, 51, 28))
        self.done_s2_btn.setObjectName("done_s2_btn")
        self.measure_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.measure_s2_lbl.setGeometry(QtCore.QRect(30, 85, 91, 21))
        self.measure_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s2_lbl.setObjectName("measure_s2_lbl")
        self.done_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.done_s2_lbl.setGeometry(QtCore.QRect(170, 85, 61, 21))
        self.done_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s2_lbl.setObjectName("done_s2_lbl")
        self.warning_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.warning_s2_lbl.setGeometry(QtCore.QRect(310, 40, 71, 20))
        self.warning_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_s2_lbl.setObjectName("warning_s2_lbl")
        self.reset_s2_btn = QtWidgets.QPushButton(self.groupBox_4)
        self.reset_s2_btn.setEnabled(False)
        self.reset_s2_btn.setGeometry(QtCore.QRect(200, 50, 51, 28))
        self.reset_s2_btn.setObjectName("reset_s2_btn")
        self.time_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.time_s2_lbl.setGeometry(QtCore.QRect(310, 79, 71, 21))
        self.time_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s2_lbl.setObjectName("time_s2_lbl")
        self.time_s1_lbl_12 = QtWidgets.QLabel(self.groupBox_4)
        self.time_s1_lbl_12.setGeometry(QtCore.QRect(260, 79, 51, 21))
        self.time_s1_lbl_12.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_12.setObjectName("time_s1_lbl_12")
        self.time_s1_lbl_13 = QtWidgets.QLabel(self.groupBox_4)
        self.time_s1_lbl_13.setGeometry(QtCore.QRect(260, 39, 51, 21))
        self.time_s1_lbl_13.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_13.setObjectName("time_s1_lbl_13")
        self.time_s1_lbl_14 = QtWidgets.QLabel(self.groupBox_4)
        self.time_s1_lbl_14.setGeometry(QtCore.QRect(260, 59, 51, 21))
        self.time_s1_lbl_14.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_14.setObjectName("time_s1_lbl_14")
        self.error_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.error_s2_lbl.setGeometry(QtCore.QRect(310, 59, 71, 20))
        self.error_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.error_s2_lbl.setObjectName("error_s2_lbl")
        self.status_s2_lbl = QtWidgets.QLabel(self.groupBox_4)
        self.status_s2_lbl.setGeometry(QtCore.QRect(190, 10, 91, 41))
        self.status_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_s2_lbl.setObjectName("status_s2_lbl")
        self.measure_s1_lbl_4 = QtWidgets.QLabel(self.groupBox_4)
        self.measure_s1_lbl_4.setGeometry(QtCore.QRect(100, 10, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.measure_s1_lbl_4.setFont(font)
        self.measure_s1_lbl_4.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s1_lbl_4.setObjectName("measure_s1_lbl_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 290, 391, 111))
        self.groupBox_5.setObjectName("groupBox_5")
        self.measure_s3_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.measure_s3_btn.setGeometry(QtCore.QRect(20, 50, 93, 28))
        self.measure_s3_btn.setObjectName("measure_s3_btn")
        self.done_s3_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.done_s3_btn.setGeometry(QtCore.QRect(150, 50, 51, 28))
        self.done_s3_btn.setObjectName("done_s3_btn")
        self.measure_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.measure_s3_lbl.setGeometry(QtCore.QRect(30, 85, 91, 21))
        self.measure_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s3_lbl.setObjectName("measure_s3_lbl")
        self.done_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.done_s3_lbl.setGeometry(QtCore.QRect(170, 85, 61, 21))
        self.done_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s3_lbl.setObjectName("done_s3_lbl")
        self.warning_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.warning_s3_lbl.setGeometry(QtCore.QRect(310, 40, 71, 20))
        self.warning_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_s3_lbl.setObjectName("warning_s3_lbl")
        self.reset_s3_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.reset_s3_btn.setEnabled(False)
        self.reset_s3_btn.setGeometry(QtCore.QRect(200, 50, 51, 28))
        self.reset_s3_btn.setObjectName("reset_s3_btn")
        self.time_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.time_s3_lbl.setGeometry(QtCore.QRect(310, 79, 71, 21))
        self.time_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s3_lbl.setObjectName("time_s3_lbl")
        self.time_s1_lbl_20 = QtWidgets.QLabel(self.groupBox_5)
        self.time_s1_lbl_20.setGeometry(QtCore.QRect(260, 79, 51, 21))
        self.time_s1_lbl_20.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_20.setObjectName("time_s1_lbl_20")
        self.time_s1_lbl_21 = QtWidgets.QLabel(self.groupBox_5)
        self.time_s1_lbl_21.setGeometry(QtCore.QRect(260, 39, 51, 21))
        self.time_s1_lbl_21.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_21.setObjectName("time_s1_lbl_21")
        self.time_s1_lbl_22 = QtWidgets.QLabel(self.groupBox_5)
        self.time_s1_lbl_22.setGeometry(QtCore.QRect(260, 59, 51, 21))
        self.time_s1_lbl_22.setAlignment(QtCore.Qt.AlignCenter)
        self.time_s1_lbl_22.setObjectName("time_s1_lbl_22")
        self.error_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.error_s3_lbl.setGeometry(QtCore.QRect(310, 59, 71, 20))
        self.error_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.error_s3_lbl.setObjectName("error_s3_lbl")
        self.status_s3_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.status_s3_lbl.setGeometry(QtCore.QRect(190, 10, 91, 41))
        self.status_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.status_s3_lbl.setObjectName("status_s3_lbl")
        self.measure_s1_lbl_5 = QtWidgets.QLabel(self.groupBox_5)
        self.measure_s1_lbl_5.setGeometry(QtCore.QRect(100, 10, 101, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.measure_s1_lbl_5.setFont(font)
        self.measure_s1_lbl_5.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s1_lbl_5.setObjectName("measure_s1_lbl_5")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(200, 220, 451, 81))
        font = QtGui.QFont()
        font.setUnderline(False)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.connect_server = QtWidgets.QLabel(self.groupBox_3)
        self.connect_server.setGeometry(QtCore.QRect(320, 30, 111, 21))
        self.connect_server.setObjectName("connect_server")
        self.ip_btn = QtWidgets.QPushButton(self.groupBox_3)
        self.ip_btn.setGeometry(QtCore.QRect(210, 20, 91, 41))
        self.ip_btn.setObjectName("ip_btn")
        self.ip_txt = QtWidgets.QLineEdit(self.groupBox_3)
        self.ip_txt.setGeometry(QtCore.QRect(80, 30, 113, 22))
        self.ip_txt.setObjectName("ip_txt")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 21))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(90, 20, 301, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Logo_CEI.JPG"))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(410, 20, 301, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Enviguard_LOGO.PNG"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.regs_old = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.mask1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.mask2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.serverip=""

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "EnviGuard Port Controller"))
        self.groupBox_2.setTitle(_translate("Form", "Cookie"))
        self.connect_cookie.setText(_translate("Form", "Not Connected"))
        self.groupBox.setTitle(_translate("Form", "CDU"))
        self.measure_s1_btn.setText(_translate("Form", "Measuring"))
        self.done_s1_btn.setText(_translate("Form", "Stop"))
        self.measure_s1_lbl.setText(_translate("Form", "Idle"))
        self.done_s1_lbl.setText(_translate("Form", "Idle"))
        self.warning_s1_lbl.setText(_translate("Form", "OK"))
        self.reset_s1_btn.setText(_translate("Form", "Reset"))
        self.time_s1_lbl.setText(_translate("Form", "0"))
        self.time_s1_lbl_2.setText(_translate("Form", "Time:"))
        self.time_s1_lbl_3.setText(_translate("Form", "Warning:"))
        self.time_s1_lbl_4.setText(_translate("Form", "Error:"))
        self.error_s1_lbl.setText(_translate("Form", "OK"))
        self.measure_s1_lbl_2.setText(_translate("Form", "SENSOR STATUS:"))
        self.status_s1_lbl.setText(_translate("Form", "Unitialized"))
        self.connect_cookie_2.setText(_translate("Form", "Cookie:"))
        self.groupBox_4.setTitle(_translate("Form", "PDU"))
        self.measure_s2_btn.setText(_translate("Form", "Measuring"))
        self.done_s2_btn.setText(_translate("Form", "Stop"))
        self.measure_s2_lbl.setText(_translate("Form", "Idle"))
        self.done_s2_lbl.setText(_translate("Form", "Idle"))
        self.warning_s2_lbl.setText(_translate("Form", "OK"))
        self.reset_s2_btn.setText(_translate("Form", "Reset"))
        self.time_s2_lbl.setText(_translate("Form", "0"))
        self.time_s1_lbl_12.setText(_translate("Form", "Time:"))
        self.time_s1_lbl_13.setText(_translate("Form", "Warning:"))
        self.time_s1_lbl_14.setText(_translate("Form", "Error:"))
        self.error_s2_lbl.setText(_translate("Form", "OK"))
        self.status_s2_lbl.setText(_translate("Form", "Unitialized"))
        self.measure_s1_lbl_4.setText(_translate("Form", "SENSOR STATUS:"))
        self.groupBox_5.setTitle(_translate("Form", "ADU"))
        self.measure_s3_btn.setText(_translate("Form", "Measuring"))
        self.done_s3_btn.setText(_translate("Form", "Stop"))
        self.measure_s3_lbl.setText(_translate("Form", "Idle"))
        self.done_s3_lbl.setText(_translate("Form", "Idle"))
        self.warning_s3_lbl.setText(_translate("Form", "OK"))
        self.reset_s3_btn.setText(_translate("Form", "Reset"))
        self.time_s3_lbl.setText(_translate("Form", "0"))
        self.time_s1_lbl_20.setText(_translate("Form", "Time:"))
        self.time_s1_lbl_21.setText(_translate("Form", "Warning:"))
        self.time_s1_lbl_22.setText(_translate("Form", "Error:"))
        self.error_s3_lbl.setText(_translate("Form", "OK"))
        self.status_s3_lbl.setText(_translate("Form", "Unitialized"))
        self.measure_s1_lbl_5.setText(_translate("Form", "SENSOR STATUS:"))
        self.groupBox_3.setTitle(_translate("Form", "Server"))
        self.connect_server.setText(_translate("Form", "Server Not Connected"))
        self.ip_btn.setText(_translate("Form", "Update IP"))
        self.ip_txt.setText(_translate("Form", "192.168.1.38"))
        self.label.setText(_translate("Form", "Server IP"))

        self.ip_btn.clicked.connect(self.connectServer)
        self.measure_s1_btn.clicked.connect(self.measureS1)
        self.done_s1_btn.clicked.connect(self.doneS1)
        self.reset_s1_btn.clicked.connect(self.resetS1)
        #Updating the GUI
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(5000) #trigger 5 seconds.

    def update(self):
        print("Updating!")
        c.host(self.serverip)
        c.open()
        if c.is_open() == 1:
            print("Connected")
            self.connect_server.setText("Server Connected")
            regs = c.read_holding_registers(0, 10)

            #Update register values and masks
            for i in range(0, 10):
                if self.regs_old[i] != regs[i]:
                    self.regs_old[i]= regs[i]
                    if i<3:
                        self.mask1_1[i]=self.regs_old[i]//256
                        self.mask2_1[i]=self.regs_old[i]%256
                        self.mask1_2[i]=self.mask2_1[i]//10
                        self.mask2_2[i]=self.mask2_1[i]%10
                    elif i>=3 and i<6:
                        self.mask1[i]=self.regs_old[i]//256
                        self.mask2[i]=self.regs_old[i]%256
                    
                #Check the values of sensor 1
                if i == 0:
                    
                    if self.mask2_2[i] == 0:
                        self.measure_s1_lbl.setText("Idle")
                        
                    elif self.mask2_2[i] == 1:
                        self.measure_s1_lbl.setText("Connecting")
                        
                    elif self.mask2_2[i] == 2:
                        self.measure_s1_lbl.setText("Connected")

                    elif self.mask2_2[i] == 3:
                        self.measure_s1_lbl.setText("Measuring")

                    elif self.mask2_2[i] == 4:
                        self.measure_s1_lbl.setText("Measured")
                        self.mask2_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)

                    elif self.mask2_2[i] == 7:
                        self.error_s1_lbl.setText("error 7")
                        self.mask1_2[i]=1
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        print(writemask)
                        c.write_single_register(i,writemask)
                        self.done_s1_btn.setEnabled(True)

                    if self.mask1_2[i] == 0:
                        self.done_s1_lbl.setText("Idle")
                        
                    elif self.mask1_2[i] == 1:
                        self.done_s1_lbl.setText("Connecting")

                    elif self.mask1_2[i] == 2:
                        self.done_s1_lbl.setText("Stopping")
                        
                    elif self.mask1_2[i] == 3:
                        self.done_s1_lbl.setText("Stopped")
                        self.mask1_2[i]=0
                        self.mask2_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)
                        self.done_s1_btn.setEnabled(True)
                        self.reset_s1_btn.setEnabled(False)

                    elif self.mask1_2[i] == 7:
                        self.done_s1_lbl.setText("Can't Stop")
                        self.mask1_2[i]=1
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        print(writemask)
                        c.write_single_register(i,writemask)

                    if self.mask1[i] != 0:
                        #Status update
                        status=seek_table(self.mask1[i])
                        self.status_s1_lbl.setText(status)
                    
                #Check the values of sensor 2        
                elif i == 1:
                    if self.mask2_2[i] == 0:
                        self.measure_s2_lbl.setText("Idle")
                        
                    elif self.mask2_2[i] == 1:
                        self.error_s2_lbl.setText("CDU Not Connected")
                        
                    elif self.mask2_2[i] == 2:
                        self.measure_s2_lbl.setText("Measuring")

                    elif self.mask2_2[i] == 3:
                        self.measure_s2_lbl.setText("Measured")
                        self.mask2_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)

                    elif self.mask2_2[i] == 7:
                        self.error_s2_lbl.setText("No Water")
                        self.done_s1_btn.setEnabled(True)

                    if self.mask1_2[i] == 0:
                        self.done_s2_lbl.setText("Idle")
                        
                    elif self.mask1_2[i] == 1:
                        self.done_s2_lbl.setText("Connecting")

                    elif self.mask1_2[i] == 2:
                        self.done_s2_lbl.setText("Stopping")
                        
                    elif self.mask1_2[i] == 3:
                        self.done_s2_lbl.setText("Stopped")
                        self.mask1_2[i]=0
                        self.mask2_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)
                    elif self.mask1_2[i] == 7:
                        self.done_s2_lbl.setText("Can't Stop")
                
                #Check the values of sensor 3        
                elif i == 2:
                    if self.mask2_2[i] == 0:
                        self.measure_s3_lbl.setText("Idle")
                        
                    elif self.mask2_2[i] == 1:
                        self.measure_s3_lbl.setText("Connecting")
                        
                    elif self.mask2_2[i] == 2:
                        self.measure_s3_lbl.setText("Measuring")

                    elif self.mask2_2[i] == 3:
                        self.measure_s3_lbl.setText("Measured")
                        self.mask2_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)

                    elif self.mask2_2[i] == 7:
                        self.measure_s3_lbl.setText("No Water")
                        self.done_s1_btn.setEnabled(True)

                    if self.mask1_2[i] == 0:
                        self.done_s3_lbl.setText("Idle")
                        
                    elif self.mask1_2[i] == 1:
                        self.done_s3_lbl.setText("Connecting")

                    elif self.mask1_2[i] == 2:
                        self.done_s3_lbl.setText("Stopping")
                        
                    elif self.mask1_2[i] == 3:
                        self.done_s3_lbl.setText("Stopped")
                        self.mask1_2[i]=0
                        writemask=self.mask1_1[i]*256+self.mask1_2[i]*10+self.mask2_2[i]
                        c.write_single_register(i,writemask)
                    elif self.mask1_2[i] == 7:
                        self.done_s3_lbl.setText("Can't Stop")

                
                elif i == 3:
                    if self.mask1[i] == 0:
                        self.warning_s1_lbl.setText("OK")
                        
                    elif self.mask1[i] > 0:
                        self.warning_s1_lbl.setText(str(self.mask1[i]))

                    if self.mask2[i] == 0:
                        self.error_s1_lbl.setText("OK") 
                        self.reset_s1_btn.setEnabled(False) 
                    elif self.mask2[i] > 0:
                        self.error_s1_lbl.setText(str(self.mask2[i]))
                        self.reset_s1_btn.setEnabled(True)

                elif i == 4:
                    if self.mask1[i] == 0:
                        self.warning_s2_lbl.setText("OK")
                        
                    elif self.mask1[i] > 0:
                        self.warning_s2_lbl.setText(str(self.mask1[i]))

                    if self.mask2[i] == 0:
                        self.error_s2_lbl.setText("OK")  
                        self.reset_s2_btn.setEnabled(False)
                    elif self.mask2[i] > 0:
                        self.error_s2_lbl.setText(str(self.mask2[i]))
                        self.reset_s2_btn.setEnabled(True)

                elif i == 5:
                    if self.mask1[i] == 0:
                        self.warning_s3_lbl.setText("OK")
                        
                    elif self.mask1[i] > 0:
                        self.warning_s3_lbl.setText(str(self.mask1[i]))

                    if self.mask2[i] == 0:
                        self.error_s3_lbl.setText("OK") 
                        self.reset_s3_btn.setEnabled(False) 
                    elif self.mask2[i] > 0:
                        self.error_s3_lbl.setText(str(self.mask2[i]))
                        self.reset_s3_btn.setEnabled(True)


                elif i == 6:
                    self.time_s1_lbl.setText(str(self.regs_old[i]))

                elif i == 7:
                    self.time_s2_lbl.setText(str(self.regs_old[i]))

                elif i == 8:
                    self.time_s3_lbl.setText(str(self.regs_old[i]))

                #Check if cookie is connected(1) or not(0)
                elif i == 9:
                    if regs[i] == 1:
                        self.connect_cookie.setText("Connected")
                        c.write_single_register(i,0)
                    else:
                        self.connect_cookie.setText("Not Connected")




                    if regs:
                        print("reg ad #0 to 9: "+str(regs))
                    else:
                        print("Not Connected")
                    c.close()
                else:
                    self.connect_server.setText("Not Connected")
                    print("Not Connected")

    #Change the ip where the gui is connected
    def connectServer(self):

        print("Connecting Server!")
        print(self.ip_txt.text())
        self.serverip = self.ip_txt.text()
        c.host(self.serverip)
        c.open()
        if c.is_open() == 1:
            print("Connected")
            self.connect_server.setText("Connected")
            regs = c.read_holding_registers(0, 10)

            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            self.connect_server.setText("Not Connected")
            print("Not Connected")

    #Measuring button function
    def seek_table(data):
        if data==1:
            a="Initializing"
        elif data==2:
            a="Init_failed"
        elif data==3:
            a="Uninitialized"
        elif data==4:
            a="Wait_trigger"
        elif data==5:
            a="Initialized"
        elif data==6:
            a="Paused"
        elif data==7:
            a="Running"
        elif data==8:
            a="Init_failed"
        elif data==9:
            a="Stopped"
        elif data==10:
            a="Completed"
        elif data==11:
            a="Idle"
        elif data==12:
            a="Finalizing"

        return a


    def measureS1(self):
        print("Measuring!")
        c.open()
        if c.is_open() == 1:
            self.mask2[0]=1
            writemask=self.mask1[0]*10+self.mask2[0]
            print(writemask)
            if c.write_single_register(0,writemask):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            self.connect_s1_lbl.setText("Not Connected")
            print("Not Connected")        
        
    #Stopping button function
    def doneS1(self):
        self.done_s1_lbl.setText("Connecting!!")
        c.open()
        regs = c.read_holding_registers(0, 10)
        if c.is_open() == 1:
            self.done_s1_lbl.setText("Stopping!")
            self.mask1[0]=1
            self.mask2[0]=0
            writemask=self.mask1[0]*10+self.mask2[0]
            print(writemask)
            if c.write_single_register(0,writemask):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
            self.done_s1_btn.setEnabled(False)
            self.reset_s1_btn.setEnabled(True)
        else:
            print("Not Connected")        
    
    #Reseting button functions
    def resetS1(self):
        c.open()
        regs = c.read_holding_registers(0, 10)
        if c.is_open() == 1:
            self.done_s1_lbl.setText("Reseting!")

            self.mask2[3]=0
            writemask=self.mask1[3]*256+self.mask2[3]
            c.write_single_register(3,writemask)
            self.mask1_1[0]=0
            self.mask1_2[0]=0
            self.mask2_2[0]=0
            writemask=self.mask1_1[0]*256+self.mask1_2[0]*10+self.mask2_2[0]
            
            if c.write_single_register(0,writemask):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
            self.done_s1_btn.setEnabled(True)
            self.reset_s1_btn.setEnabled(False)
        else:
            print("Not Connected")   


if __name__ == "__main__":
    c = ModbusClient()
    print("Creating ModbusClient")
    socket.gethostname()
    c.host(socket.gethostname())
    print("Establishing host")
    c.port(60000)
    print("Establishing port")
    print("Starting")
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())





