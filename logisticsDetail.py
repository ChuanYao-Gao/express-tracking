# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logisticsDetail.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_mailNo = QtWidgets.QLabel(Dialog)
        self.label_mailNo.setObjectName("label_mailNo")
        self.verticalLayout_2.addWidget(self.label_mailNo)
        self.label_lastMessage = QtWidgets.QLabel(Dialog)
        self.label_lastMessage.setObjectName("label_lastMessage")
        self.verticalLayout_2.addWidget(self.label_lastMessage)
        self.label_cpMobile = QtWidgets.QLabel(Dialog)
        self.label_cpMobile.setObjectName("label_cpMobile")
        self.verticalLayout_2.addWidget(self.label_cpMobile)
        self.label_logisticsCompanyName = QtWidgets.QLabel(Dialog)
        self.label_logisticsCompanyName.setObjectName("label_logisticsCompanyName")
        self.verticalLayout_2.addWidget(self.label_logisticsCompanyName)
        self.label_logisticsStatus = QtWidgets.QLabel(Dialog)
        self.label_logisticsStatus.setObjectName("label_logisticsStatus")
        self.verticalLayout_2.addWidget(self.label_logisticsStatus)
        self.label_takeTime = QtWidgets.QLabel(Dialog)
        self.label_takeTime.setObjectName("label_takeTime")
        self.verticalLayout_2.addWidget(self.label_takeTime)
        self.label_lastTime = QtWidgets.QLabel(Dialog)
        self.label_lastTime.setObjectName("label_lastTime")
        self.verticalLayout_2.addWidget(self.label_lastTime)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_mailNo.setText(_translate("Dialog", "物流单号："))
        self.label_lastMessage.setText(_translate("Dialog", "最新消息："))
        self.label_cpMobile.setText(_translate("Dialog", "手机号："))
        self.label_logisticsCompanyName.setText(_translate("Dialog", "物流公司："))
        self.label_logisticsStatus.setText(_translate("Dialog", "物流状态："))
        self.label_takeTime.setText(_translate("Dialog", "耗时："))
        self.label_lastTime.setText(_translate("Dialog", "最新时间："))

