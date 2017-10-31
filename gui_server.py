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
        self.ip_txt = QtWidgets.QLineEdit(Form)
        self.ip_txt.setGeometry(QtCore.QRect(330, 80, 113, 22))
        self.ip_txt.setObjectName("ip_txt")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 80, 55, 16))
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(210, 130, 391, 121))
        self.groupBox.setObjectName("groupBox")
        self.measure_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.measure_s1_btn.setGeometry(QtCore.QRect(20, 20, 93, 28))
        self.measure_s1_btn.setObjectName("measure_s1_btn")
        self.done_s1_btn = QtWidgets.QPushButton(self.groupBox)
        self.done_s1_btn.setGeometry(QtCore.QRect(150, 20, 93, 28))
        self.done_s1_btn.setObjectName("done_s1_btn")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(280, 20, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.measure_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.measure_s1_lbl.setGeometry(QtCore.QRect(30, 56, 91, 20))
        self.measure_s1_lbl.setObjectName("measure_s1_lbl")
        self.done_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.done_s1_lbl.setGeometry(QtCore.QRect(170, 60, 61, 16))
        self.done_s1_lbl.setObjectName("done_s1_lbl")
        self.done_s1_lbl_2 = QtWidgets.QLabel(self.groupBox)
        self.done_s1_lbl_2.setGeometry(QtCore.QRect(280, 60, 91, 16))
        self.done_s1_lbl_2.setObjectName("done_s1_lbl_2")
        self.connect_s1_lbl = QtWidgets.QLabel(self.groupBox)
        self.connect_s1_lbl.setGeometry(QtCore.QRect(160, 90, 91, 20))
        self.connect_s1_lbl.setObjectName("connect_s1_lbl")
        self.ip_btn = QtWidgets.QPushButton(Form)
        self.ip_btn.setGeometry(QtCore.QRect(480, 80, 93, 28))
        self.ip_btn.setObjectName("ip_btn")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(360, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.regs_old = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ip_txt.setText(_translate("Form", "localhost"))
        self.label.setText(_translate("Form", "IP"))
        self.groupBox.setTitle(_translate("Form", "Sensor 1"))
        self.measure_s1_btn.setText(_translate("Form", "Measuring"))
        self.done_s1_btn.setText(_translate("Form", "Done"))
        self.pushButton_4.setText(_translate("Form", "Done"))
        self.measure_s1_lbl.setText(_translate("Form", "Not measuring"))
        self.done_s1_lbl.setText(_translate("Form", "Not Done"))
        self.done_s1_lbl_2.setText(_translate("Form", "Not measuring"))
        self.connect_s1_lbl.setText(_translate("Form", "Not measuring"))
        self.ip_btn.setText(_translate("Form", "Update IP"))
        self.label_2.setText(_translate("Form", "SERVER"))

        self.ip_btn.clicked.connect(self.connectServer)
        self.measure_s1_btn.clicked.connect(self.measureS1)
        self.done_s1_btn.clicked.connect(self.doneS1)
        #Updating the GUI
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(100) #trigger every second.



    def update(self):
        print("Updating!")
        c.host(self.ip_txt.text())
        c.open()
        if c.is_open() == 1:
            print("Connected")
            self.connect_s1_lbl.setText("Connected")
            regs = c.read_holding_registers(0, 10)

            for i in range(0, 9):
                if self.regs_old[i] != regs[i]:
                    self.regs_old[i]= regs[i]
                    
                    if i == 0:
                        if self.regs_old[i] == 0:
                            self.measure_s1_lbl.setText("Idle")
                            
                        elif self.regs_old[i] == 1:
                            self.measure_s1_lbl.setText("Measuring")
                            
                        elif self.regs_old[i] == 2:
                            self.measure_s1_lbl.setText("Measured")
                            c.write_single_register(i,0)
                        
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


            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            self.connect_s1_lbl.setText("Not Connected")
            print("Not Connected")

    def connectServer(self):

        print("Connecting Server!")
        print(self.ip_txt.text())
        c.host(self.ip_txt.text())
        c.open()
        if c.is_open() == 1:
            print("Connected")
            self.connect_s1_lbl.setText("Connected")
            regs = c.read_holding_registers(0, 10)

            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            self.connect_s1_lbl.setText("Not Connected")
            print("Not Connected")

            
    def measureS1(self):
        print("Measuring!")
        self.measure_s1_lbl.setText("Measuring!!")
        c.open()
        if c.is_open() == 1:
            self.measure_s1_lbl.setText("Measuring!!")
            self.connect_s1_lbl.setText("Connected")
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
            self.connect_s1_lbl.setText("Connected")
            if c.write_single_register(1,1):
                regs = c.read_holding_registers(0, 10)
            if regs:
                print("reg ad #0 to 9: "+str(regs))
            else:
                print("Not Connected")
            c.close()
        else:
            print("Not Connected")        
          

    def printnum(self):
        print("Ham!")

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

