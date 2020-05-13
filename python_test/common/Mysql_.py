import pymysql
from common.Read_Config import Read_Config
from common.My_Logger import My_Logger

class Mysql_:

    def __init__(self):
        # 链接数据库
        try:
            self.db = pymysql.connect(
                host=Read_Config().get('mysql','host'),
                port=int(Read_Config().get('mysql','port')),
                user=Read_Config().get('mysql','user'),
                password=Read_Config().get('mysql','password'),
                database=Read_Config().get('mysql','database') ,
                # 查询结果以字典形式返回
                cursorclass=pymysql.cursors.DictCursor
            )
        except Exception as e:
            My_Logger().error('数据库连接出错,错误信息: %s'%e)
            raise e


    def fetchaone(self,sql):
        # 获取游标
        cursor = self.db.cursor()
        # 执行sql查询
        cursor.execute(sql)
        return cursor.fetchone()


    def fetchall(self,sql):
        # 获取游标
        cursor = self.db.cursor()
        # 执行sql查询
        cursor.execute(sql)
        return cursor.fetchall()


    def fetchmany(self,sql):
        # 获取游标
        cursor = self.db.cursor()
        # 执行sql查询
        cursor.execute(sql)
        return cursor.fetchmany()

    def close_mysql(self):
        return self.db.close()


if __name__ == '__main__':
    sql = "select * from `t_game`"
    res = Mysql_().fetchall(sql)
    print(res)







