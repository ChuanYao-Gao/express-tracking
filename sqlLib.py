import sqlite3
from datetime import datetime

class SQLLib(object):



    def connect(self):
        conn = sqlite3.connect("expressInquiry.db")
        return conn

    def initialDBTable(self):
        # 连接到SQLite数据库
        # 数据库文件是my_database.db
        # 如果数据库不存在，它会被自动创建
        conn = self.connect()
        # 创建一个游标对象
        c = conn.cursor()
        # 定义表结构
        table_creation_query = '''
        CREATE TABLE IF NOT EXISTS "history" (
          "id" INTEGER PRIMARY KEY AUTOINCREMENT,
          "cpCode" varchar NOT NULL,
          "cpName" varchar NOT NULL,
          "mailNo" varchar NOT NULL,
          "tel" varchar NOT NULL,
          "create_time" timestamp
        );
        '''
        # 执行创建表的命令
        c.execute(table_creation_query)
        # 提交更改并关闭连接
        conn.commit()
        conn.close()

    def insertHistory(self,contentArray):
        conn = self.connect()
        c = conn.cursor()
        c.execute('INSERT INTO history(cpCode,cpName,mailNo, tel, create_time) VALUES(?, ?, ?, ?, ?)',
                  contentArray)
        conn.commit()
        conn.close()

    def queryHistory(self):
        conn = self.connect()
        c = conn.cursor()
        c.execute("SELECT * FROM history")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
        return rows