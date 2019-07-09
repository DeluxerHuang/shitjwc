import pymysql.cursors

'''
1. 需要能够连接上数据库并将抓取的数据存在数据库中
2. 根据指定要求提取出数据
3. 逻辑层不在此处处理
'''

class conn():
    def __init__(self, host, port, user, passwd):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd

    def _connectMysql(self):
        # 连接数据库
        connect = pymysql.Connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.passwd,
            charset='utf8'
        )
        return connect

    def getAll(sql):
        cursor = _connectMysql().cursor
        cursor.excute(sql)
        return cursor.fetchall()