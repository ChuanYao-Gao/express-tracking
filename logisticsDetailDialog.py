
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from logisticsDetail import Ui_Dialog
import json
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from datetime import datetime

class DetailDialog(QDialog):
    def __init__(self,logisticsDetail):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.logisticsDetail = logisticsDetail
        self.ui.label_mailNo.setText("物流单号："+self.logisticsDetail["logisticsTrace"]["mailNo"])
        self.ui.label_lastMessage.setText("最新消息：" + self.logisticsDetail["logisticsTrace"]["theLastMessage"])
        self.ui.label_cpMobile.setText("物流公司联系方式：" + self.logisticsDetail["logisticsTrace"]["cpMobile"])
        self.ui.label_lastMessage.setText("最新消息：" + self.logisticsDetail["logisticsTrace"]["theLastMessage"])
        self.ui.label_logisticsCompanyName.setText("物流公司名称：" + self.logisticsDetail["logisticsTrace"]["logisticsCompanyName"])
        self.ui.label_logisticsStatus.setText("物流状态：" + self.logisticsDetail["logisticsTrace"]["logisticsStatus"])
        self.ui.label_takeTime.setText("耗时：" + self.logisticsDetail["logisticsTrace"]["takeTime"])
        self.ui.label_lastTime.setText("最新时间：" + self.logisticsDetail["logisticsTrace"]["theLastTime"])

        self.aList = self.logisticsDetail["logisticsTrace"]["logisticsTraceDetailList"]
        # 创建一个 QStandardItemModel
        table_model = QStandardItemModel(len(self.aList), 6)  # 3行2列
        table_model.setHorizontalHeaderLabels(['地区编号', '地区名称', '物流子状态', '时间', '物流状态', '描述'])

        # 填充数据
        a = 0
        for i in self.aList:
            b = 0
            for j in i:
                if j == "time":
                    dt_object = datetime.fromtimestamp(self.aList[a][j]/1000)
                    formatted_time = dt_object.strftime('%Y-%m-%d %H:%M:%S')
                    table_model.setItem(a, b, QStandardItem(formatted_time))
                else:
                    table_model.setItem(a, b, QStandardItem(self.aList[a][j]))
                b+=1
            a+=1
        self.ui.tableView.setModel(table_model)