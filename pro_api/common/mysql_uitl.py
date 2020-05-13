import pymysql
from common.readconfig import ConfigLoader

class MysqlUtil:

    def __init__(self):
        config = ConfigLoader()
        host = config.get('mysql', 'host')
        port = config.getint('mysql', 'port')  # port 是一个int数据
        user = config.get('mysql', 'usr')
        password = config.get('mysql', 'pwd')
        try:
            self.mysql = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=None,
                                         port=port,
                                         cursorclass=pymysql.cursors.DictCursor)

        except Exception as e :
            print("数据库连接错误:{}".format(e))
            raise e

    def fetch_one(self,sql):  # 查询一条数据并返回
        cursor = self.mysql.cursor() # 建立数据库连接游标
        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchone()  #


    def fetch_all(self,sql):  # 查询多条数据并返回
        cursor = self.mysql.cursor()
        cursor.execute(sql)  # 根据sql 进行查询
        return cursor.fetchall()  # ((),())

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql_2 = "select *  from message.message_circle_link where circle_uuid = 'd41b03780174469ba858a3db5ae0f05d' and type = 1 "

    mysql_util = MysqlUtil()
    results = mysql_util.fetch_all(sql_2)
    print(len(results))
