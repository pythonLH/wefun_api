import unittest
import time
import requests
import json
import random
from common.excel import DoExcel
from common.readconfig import ConfigLoader
from common.request import Http_Request
from common.os_path import QuanZi_case_dir
from ddt import ddt,data,unpack
from common.mysql_uitl import MysqlUtil
from common.random_number import PhoneNOGenerator # 随机名字之类的封装

@ddt
class new_domain(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("添加领域")


    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global newest_id
        newest_id = mysql.fetch_one("select * from message.message_circle_field where id != '' order by id  desc limit 1;") #事先查出最新的领域
        # print(newest_id['id'])
        # print(type(newest_id))


    @data(*quanzi_case)
    def test_01(self,case):
        header = json.loads(ConfigLoader().get("header","header_value"))
        data = json.loads(case.data)

        # 避免名字重复，尽量避开(但不能100%确保名字不重复)
        if data['fieldName'] == '':
            data['fieldName'] = PhoneNOGenerator().stochastict_name() # 随机生成名字
            data['weight'] = random.randint(1,50) # 去个随机数作为  权重

        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e :
            print("请求报错:%s"%e)
            raise e

        result = res.get_json()
        self.assertEqual(case.expected,result['success'])
        if result['success'] == 'Ttrue': # 如果接口返回True，数据库会增加数据，id会加1
            self.assertNotEqual(newest_id['id'],MysqlUtil().fetch_one("select * from message.message_circle_field where id != '' order by id  desc limit 1;")['id'])

        else: # 如果接口返回False，数据库id不会增加
            self.assertNotEqual(newest_id['id'] , MysqlUtil().fetch_one("select * from message.message_circle_field where id != '' order by id  desc limit 1;")['id'])


    def tearDown(self):

        '''time.sleep(20) # 在这个脚本还没执行完之前，数据库能查询到  新增的领域

        # 新增领域后，20秒后删除刚才新增的数据
        sql = "delete from message.message_circle_field order by id desc limit 1;" # 删除新增的领域
        mysql.delete_one(sql)'''

        mysql.close()

if __name__ == '__main__':
    unittest.main()


