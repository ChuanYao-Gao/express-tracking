
import sys
from PyQt5.QtWidgets import QApplication,QDialog
import requests
import json
import sqlite3
from datetime import datetime
from expressInquiry import Ui_Form
from logisticsDetailDialog import DetailDialog
from historyDialog import HistoryDialog
from sqlLib import SQLLib

class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # https://open.taobao.com/doc.htm?docId=105085&docType=1
        self.cpCodeDict = {"圆通快递":"YTO","极兔速递":"HTKY","中通快递":"ZTO","优速快递":"UC","国通快递":"GTO",
                           "天天快递":"TTKDEX","全峰快递":"QFKD","申通快递":"STO","韵达快递":"YUNDA","顺丰速运":"SF",
                           "EMS":"EMS","宅急送":"ZJS","菜鸟速递":"CP570969","德邦快递":"DBKD"}
        self.ui.pushButton_inquiry.clicked.connect(self.button_inquiry_clicked)
        self.ui.pushButton_history.clicked.connect(self.button_history_clicked)
        self.ui.pushButton_detail.clicked.connect(self.button_detail_clicked)
        self.ui.comboBox_cpCode.clear()
        self.ui.comboBox_cpCode.addItems(self.cpCodeDict.keys())
        self.logisticsDetail = {}

    def button_detail_clicked(self):
        
        self.logisticsDetailDialog = DetailDialog(self.logisticsDetail)
        self.logisticsDetailDialog.show()
    def button_history_clicked(self):

        self.historyDialog = HistoryDialog()
        self.historyDialog.signal1.connect(self.receiveSignal1)
        self.historyDialog.show()

    def receiveSignal1(self,item):
        self.ui.comboBox_cpCode.setCurrentText(item[2])
        self.ui.lineEdit_mailNo.setText(item[3])
        self.ui.lineEdit_tel.setText(item[4])


    def button_inquiry_clicked(self):
        url = "https://eolink.o.apispace.com/wlgj1/paidtobuy_api/trace_search"
        payload = {"cpCode": self.cpCodeDict[self.ui.comboBox_cpCode.currentText()],
                   "mailNo": self.ui.lineEdit_mailNo.text(),
                   "tel": self.ui.lineEdit_tel.text(),
                   "orderType": "asc"}
        headers = {
            "X-APISpace-Token": "x49bt79rd3c6vr9juzlcpurl8ignakph",
            "Content-Type": "application/json"
        }
        response = requests.request("POST", url, data=json.dumps(payload), headers=headers)
        if response.status_code == 200:
            sqlLib.insertHistory([self.cpCodeDict[self.ui.comboBox_cpCode.currentText()],self.ui.comboBox_cpCode.currentText(), self.ui.lineEdit_mailNo.text(),
                       self.ui.lineEdit_tel.text(), datetime.now()])
            self.logisticsDetail = response.text
        else:
            print("发生错误")




# 创建应用程序对象
app = QApplication(sys.argv)
dialog = MyDialog()
dialog.show()
sqlLib = SQLLib()
sqlLib.initialDBTable()
# 进入应用程序的主循环，等待事件处理
sys.exit(app.exec_())

