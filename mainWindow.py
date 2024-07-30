
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
        self.logisticsDetail = json.loads('''
                {
                  "traceId" : "3787564475643570990",
                  "trace_id" : "3787564475643570990",
                  "success" : true,
                  "logisticsTrace" : {
                    "theLastTime" : "2024-07-26 18:41:19",
                    "cpCode" : "YTO",
                    "cpUrl" : "http://www.yto.net.cn/",
                    "takeTime" : "1天16小时",
                    "logisticsStatusDesc" : "已签收",
                    "logisticsTraceDetailList" : [ {
                      "areaCode" : "CN130181000000",
                      "areaName" : "河北省,石家庄市,辛集市",
                      "subLogisticsStatus" : "ACCEPT",
                      "time" : 1721732722000,
                      "logisticsStatus" : "ACCEPT",
                      "desc" : "您的快件在【河北省石家庄市辛集市】已揽收，揽收人: 乔祎（15176927958）"
                    }, {
                      "areaCode" : "CN130181000000",
                      "areaName" : "河北省,石家庄市,辛集市",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721733253000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件离开【河北省石家庄市辛集市】，已发往【石家庄转运中心】"
                    }, {
                      "areaCode" : "CN130123000000",
                      "areaName" : "河北省,石家庄市,正定县",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721741758000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件已经到达【石家庄转运中心】"
                    }, {
                      "areaCode" : "CN130123000000",
                      "areaName" : "河北省,石家庄市,正定县",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721741918000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件离开【石家庄转运中心】，已发往【成都转运中心】"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721832950000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件已经到达【成都转运中心】"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721836355000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件离开【成都转运中心】，已发往【四川省成都市高新区三部】"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "TRANSPORT",
                      "time" : 1721858986000,
                      "logisticsStatus" : "TRANSPORT",
                      "desc" : "您的快件已经到达【四川省成都市高新区三部】"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "DELIVERING",
                      "time" : 1721866993000,
                      "logisticsStatus" : "DELIVERING",
                      "desc" : "【四川省成都市高新区三部】的肖春斯（17781615629）正在派件，请耐心等待！如有疑问请联系网点:028-84196896，投诉电话:028-84196896。[95161和185211号段的上海号码为圆通业务员专属号码，请放心接听]"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "STA_INBOUND",
                      "time" : 1721876772000,
                      "logisticsStatus" : "DELIVERING",
                      "desc" : "您好，快件已暂存至成都南城都汇四期31栋店菜鸟驿站，如有疑问请联系17396231602，投诉电话：028-84196896。感谢使用圆通速递，期待再次为您服务！"
                    }, {
                      "areaCode" : "CN510116000000",
                      "areaName" : "四川省,成都市,双流区",
                      "subLogisticsStatus" : "SIGN",
                      "time" : 1721990479000,
                      "logisticsStatus" : "SIGN",
                      "desc" : "已签收，签收人凭取货码签收。如有疑问请联系业务员: 17781615629，网点电话：028-84196896，投诉电话: 028-84196896。感谢使用圆通速递，期待再次为您服务！"
                    } ],
                    "mailNo" : "YT8988680934020",
                    "theLastMessage" : "已签收，签收人凭取货码签收。如有疑问请联系业务员: 17781615629，网点电话：028-84196896，投诉电话: 028-84196896。感谢使用圆通速递，期待再次为您服务！",
                    "cpMobile" : "95554",
                    "logisticsCompanyName" : "圆通快递",
                    "logisticsStatus" : "SIGN"
                  }
                }
                ''')
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

