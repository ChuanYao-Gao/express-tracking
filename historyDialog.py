
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from history import Ui_Dialog
import json
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from datetime import datetime
from sqlLib import SQLLib
from PyQt5.QtCore import pyqtSignal

class HistoryDialog(QDialog):
    signal1 = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.sqlLib = SQLLib()
        self.items = self.sqlLib.queryHistory()
        self.table_model = QStandardItemModel(len(self.items), 6)
        self.table_model.setHorizontalHeaderLabels(['序号', '物流公司编号', '物流公司名称', '物流单号', '手机号', '创建时间'])

        a = 0
        for item in self.items:
            b = 0
            for j in range(len(item)):
                self.table_model.setItem(a, b, QStandardItem(str(item[j])))
                b+=1
            a+=1
        self.ui.tableView.setModel(self.table_model)

        self.ui.tableView.clicked.connect(self.on_table_clicked)

    def on_table_clicked(self, index):
        row = index.row()
        self.signal1.emit(self.items[row])
