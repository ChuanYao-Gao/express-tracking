# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'expressInquiry.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setEnabled(True)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_cpCode = QtWidgets.QComboBox(Form)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.comboBox_cpCode.setFont(font)
        self.comboBox_cpCode.setObjectName("comboBox_cpCode")
        self.comboBox_cpCode.addItem("")
        self.comboBox_cpCode.addItem("")
        self.comboBox_cpCode.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_cpCode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_mailNo = QtWidgets.QLineEdit(Form)
        self.lineEdit_mailNo.setObjectName("lineEdit_mailNo")
        self.horizontalLayout_2.addWidget(self.lineEdit_mailNo)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_tel = QtWidgets.QLineEdit(Form)
        self.lineEdit_tel.setObjectName("lineEdit_tel")
        self.horizontalLayout_3.addWidget(self.lineEdit_tel)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_inquiry = QtWidgets.QPushButton(Form)
        self.pushButton_inquiry.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_inquiry.setFont(font)
        self.pushButton_inquiry.setObjectName("pushButton_inquiry")
        self.horizontalLayout_5.addWidget(self.pushButton_inquiry)
        self.pushButton_detail = QtWidgets.QPushButton(Form)
        self.pushButton_detail.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_detail.setFont(font)
        self.pushButton_detail.setObjectName("pushButton_detail")
        self.horizontalLayout_5.addWidget(self.pushButton_detail)
        self.pushButton_history = QtWidgets.QPushButton(Form)
        self.pushButton_history.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(13)
        self.pushButton_history.setFont(font)
        self.pushButton_history.setObjectName("pushButton_history")
        self.horizontalLayout_5.addWidget(self.pushButton_history)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "快递查询"))
        self.label_3.setText(_translate("Form", "请选择快递公司："))
        self.comboBox_cpCode.setItemText(0, _translate("Form", "圆通快递-YTO"))
        self.comboBox_cpCode.setItemText(1, _translate("Form", "中通快递"))
        self.comboBox_cpCode.setItemText(2, _translate("Form", "申通快递"))
        self.label_2.setText(_translate("Form", "请输入快递单号："))
        self.label_4.setText(_translate("Form", "请输入取件手机号："))
        self.pushButton_inquiry.setText(_translate("Form", "查询"))
        self.pushButton_detail.setText(_translate("Form", "详细页面"))
        self.pushButton_history.setText(_translate("Form", "历史记录"))

