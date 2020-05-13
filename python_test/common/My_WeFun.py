import pymysql
from common.Read_Config import Read_Config
from common.My_Logger import My_Logger
class MysqlUtil:

    def __init__(self):
        config = Read_Config()
        host = config.get('mysql', 'host')
        port = config.get_int('mysql', 'port')
        user = config.get('mysql', 'user')
        password = config.get('mysql', 'password')
        database = config.get('mysql','database')
        try:
            self.mysql = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=database,
                                         port=port,
                                         cursorclass=pymysql.cursors.DictCursor)

        except Exception as e :
            print("数据库连接错误:{}".format(e))
            raise e

    def fetch_one(self,sql):
        cursor = self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchone()


    def fetch_all(self,sql):
        cursor = self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql = r"select * from `t_game` order by _id desc;"

    mysql_util = MysqlUtil()
    results = mysql_util.fetch_all(sql)
    print(len(results))