import pymysql
import configparser
from common.ptah_object import _path
from common.redConfig import red_



# 用来查询sql的

class MysqlUtil:

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read(_path, encoding='utf-8')
        host = conf.get('mysql', 'host')
        port = conf.getint('mysql', 'port')
        user = conf.get('mysql', 'user')
        password = conf.get('mysql', 'password')
        database = conf.get('mysql', 'database')
        try:
            self.mysql = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         database=database,
                                         port=port,
                                         cursorclass=pymysql.cursors.DictCursor)

        except Exception as e:
            print("数据库连接错误:{}".format(e))
            raise e

    def fetch_one(self, sql):
        cursor = self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchone()

    def fetch_all(self, sql):
        cursor = self.mysql.cursor()
        cursor.execute(sql)
        return cursor.fetchall()

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    sql = "SELECT * FROM `mp-asset`.`t_asset`  order by  id desc limit 2;"
    code = []
    mysql_util = MysqlUtil()
    results = mysql_util.fetch_all(sql)
    for co in results:
        code.append(co['code'])
    print(code)
