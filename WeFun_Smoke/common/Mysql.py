import pymysql
import configparser
from common.Configs import read_config
from common.Logger import My_Logger





class MysqlUtil:

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(r"D:\WeFun Smoke\configs\test.conf")
        host = conf.get('mysql', 'host')
        port = conf.getint('mysql', 'port')
        user = conf.get('mysql', 'user')
        password = conf.get('mysql', 'password')
        database = conf.get('mysql','database')
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

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql = "select * from `t_vip` where telephone = '18888888888'"

    mysql_util = MysqlUtil()
    results = mysql_util.fetch_all(sql)
    print(results[0]['avatar'])
