# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_server.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pyModbusTCP.client import ModbusClient
import sys

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(837, 559)
        Form.setStyleSheet("background{color:black}")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 10, 201, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(190, 170, 451, 361))
        self.groupBox_2.setObjectName("groupBox_2")
        self.connect_cookie = QtWidgets.QLabel(self.groupBox_2)
        self.connect_cookie.setGeometry(QtCore.QRect(80, 20, 91, 20))
        self.connect_cookie.setObjectName("connect_cookie")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 391, 91))
        self.groupBox.setObjectName("groupBox")
        self.measure_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.measure_s1_btn.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.measure_s1_btn.setObjectName("measure_s1_btn")
        self.done_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.done_s1_btn.setGeometry(QtCore.QRect(150, 20, 51, 28))
        self.done_s1_btn.setObjectName("done_s1_btn")
        self.measure_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.measure_s1_lbl.setGeometry(QtCore.QRect(30, 56, 91, 20))
        self.measure_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s1_lbl.setObjectName("measure_s1_lbl")
        self.done_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.done_s1_lbl.setGeometry(QtCore.QRect(170, 60, 61, 16))
        self.done_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s1_lbl.setObjectName("done_s1_lbl")
        self.state_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.state_s1_lbl.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.state_s1_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.state_s1_lbl.setObjectName("state_s1_lbl")
        self.reset_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.reset_s1_btn.setEnabled(False)
        self.reset_s1_btn.setGeometry(QtCore.QRect(200, 20, 51, 28))
        self.reset_s1_btn.setObjectName("reset_s1_btn")
        self.connect_cookie_2 = QtWidgets.QLabel(self.groupBox_2)
        self.connect_cookie_2.setGeometry(QtCore.QRect(30, 20, 41, 20))
        self.connect_cookie_2.setObjectName("connect_cookie_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 150, 391, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.measure_s2_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.measure_s2_btn.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.measure_s2_btn.setObjectName("measure_s2_btn")
        self.done_s2_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.done_s2_btn.setGeometry(QtCore.QRect(150, 20, 51, 28))
        self.done_s2_btn.setObjectName("done_s2_btn")
        self.measure_s2_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.measure_s2_lbl.setGeometry(QtCore.QRect(30, 56, 91, 20))
        self.measure_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s2_lbl.setObjectName("measure_s2_lbl")
        self.done_s2_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.done_s2_lbl.setGeometry(QtCore.QRect(170, 60, 61, 16))
        self.done_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s2_lbl.setObjectName("done_s2_lbl")
        self.state_s2_lbl = QtWidgets.QLabel(self.groupBox_5)
        self.state_s2_lbl.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.state_s2_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.state_s2_lbl.setObjectName("state_s2_lbl")
        self.reset_s2_btn = QtWidgets.QPushButton(self.groupBox_5)
        self.reset_s2_btn.setEnabled(False)
        self.reset_s2_btn.setGeometry(QtCore.QRect(200, 20, 51, 28))
        self.reset_s2_btn.setObjectName("reset_s2_btn")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 250, 391, 91))
        self.groupBox_6.setObjectName("groupBox_6")
        self.measure_s3_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.measure_s3_btn.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.measure_s3_btn.setObjectName("measure_s3_btn")
        self.done_s3_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.done_s3_btn.setGeometry(QtCore.QRect(150, 20, 51, 28))
        self.done_s3_btn.setObjectName("done_s3_btn")
        self.measure_s3_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.measure_s3_lbl.setGeometry(QtCore.QRect(30, 56, 91, 20))
        self.measure_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.measure_s3_lbl.setObjectName("measure_s3_lbl")
        self.done_s3_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.done_s3_lbl.setGeometry(QtCore.QRect(170, 60, 61, 16))
        self.done_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.done_s3_lbl.setObjectName("done_s3_lbl")
        self.state_s3_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.state_s3_lbl.setGeometry(QtCore.QRect(270, 20, 111, 31))
        self.state_s3_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.state_s3_lbl.setObjectName("state_s3_lbl")
        self.reset_s3_btn = QtWidgets.QPushButton(self.groupBox_6)
        self.reset_s3_btn.setEnabled(False)
        self.reset_s3_btn.setGeometry(QtCore.QRect(200, 20, 51, 28))
        self.reset_s3_btn.setObjectName("reset_s3_btn")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(190, 80, 451, 81))
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
        self.regs_old = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.serverip=""


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "Cookie GUI"))
        self.groupBox_2.setTitle(_translate("Form", "Cookie"))
        self.connect_cookie.setText(_translate("Form", "Not Connected"))
        self.groupBox.setTitle(_translate("Form", "CDU"))
        self.measure_s1_btn.setText(_translate("Form", "Measuring"))
        self.done_s1_btn.setText(_translate("Form", "Stop"))
        self.measure_s1_lbl.setText(_translate("Form", "Idle"))
        self.done_s1_lbl.setText(_translate("Form", "Idle"))
        self.state_s1_lbl.setText(_translate("Form", "OK"))
        self.reset_s1_btn.setText(_translate("Form", "Reset"))
        self.connect_cookie_2.setText(_translate("Form", "Cookie:"))
        self.groupBox_5.setTitle(_translate("Form", "PDU"))
        self.measure_s2_btn.setText(_translate("Form", "Measuring"))
        self.done_s2_btn.setText(_translate("Form", "Stop"))
        self.measure_s2_lbl.setText(_translate("Form", "Idle"))
        self.done_s2_lbl.setText(_translate("Form", "Idle"))
        self.state_s2_lbl.setText(_translate("Form", "OK"))
        self.reset_s2_btn.setText(_translate("Form", "Reset"))
        self.groupBox_6.setTitle(_translate("Form", "ADU"))
        self.measure_s3_btn.setText(_translate("Form", "Measuring"))
        self.done_s3_btn.setText(_translate("Form", "Stop"))
        self.measure_s3_lbl.setText(_translate("Form", "Idle"))
        self.done_s3_lbl.setText(_translate("Form", "Idle"))
        self.state_s3_lbl.setText(_translate("Form", "OK"))
        self.reset_s3_btn.setText(_translate("Form", "Reset"))
        self.groupBox_3.setTitle(_translate("Form", "Server"))
        self.connect_server.setText(_translate("Form", "Server Not Connected"))
        self.ip_btn.setText(_translate("Form", "Update IP"))
        self.ip_txt.setText(_translate("Form", "127.0.000.198"))
        self.label.setText(_translate("Form", "Server IP"))

        self.ip_btn.clicked.connect(self.connectServer)
        self.measure_s1_btn.clicked.connect(self.measureS1)
        self.done_s1_btn.clicked.connect(self.doneS1)
        #Updating the GUI
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(5000) #trigger every second.


    def update(self):
            print("Updating!")
            c.host(self.serverip)
            c.open()
            if c.is_open() == 1:
                print("Connected")
                self.connect_server.setText("Server Connected")
                regs = c.read_holding_registers(0, 10)

                for i in range(0, 10):
                    if self.regs_old[i] != regs[i]:
                        self.regs_old[i]= regs[i]
                        
                        if i == 0:
                            if self.regs_old[i] == 0:
                                self.measure_s1_lbl.setText("Idle")
                                
                            elif self.regs_old[i] == 1:
                                self.measure_s1_lbl.setText("Connecting")
                                
                            elif self.regs_old[i] == 2:
                                self.measure_s1_lbl.setText("Measuring")

                            elif self.regs_old[i] == 3:
                                self.measure_s1_lbl.setText("Measured")
                                c.write_single_register(i,0)

                            elif self.regs_old[i] == 7:
                                self.measure_s1_lbl.setText("No Water")
                                self.done_s1_btn.setEnabled(True)
                            
                        elif i == 1:
                            if self.regs_old[i] == 0:
                                self.done_s1_lbl.setText("Idle")
                                
                            elif self.regs_old[i] == 1:
                                self.done_s1_lbl.setText("Stopping")
                                
                            elif self.regs_old[i] == 2:
                                self.done_s1_lbl.setText("Stopped")
                                c.write_single_register(i,0)
                            
                        elif i == 2:
                            if self.regs_old[i] == 2:
                                self.done_s1_lbl.setText("Completed! "+str(regs[i]))
                                c.write_single_register(i,0)

                        elif i == 9:
                            if self.regs_old[i] == 1:
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

            
    def measureS1(self):
        print("Measuring!")
        self.measure_s1_lbl.setText("Measuring!!")
        c.open()
        if c.is_open() == 1:
            if c.write_single_register(0,1):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            self.connect_s1_lbl.setText("Not Connected")
            print("Not Connected")        
        

    def doneS1(self):
        self.done_s1_lbl.setText("Connecting!!")
        c.open()
        regs = c.read_holding_registers(0, 10)
        if c.is_open() == 1:
            self.done_s1_lbl.setText("Stopping!")
            if c.write_single_register(1,1):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
            self.done_s1_btn.setEnabled(False)
        else:
            print("Not Connected")        
        


if __name__ == "__main__":
    c = ModbusClient()
    print("Creating ModbusClient")
    c.host("localhost")
    print("Establishing host")
    c.port(60000)
    print("Establishing port")
    print("Connecting")
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

