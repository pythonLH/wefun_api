import unittest
import requests
import json
import random
from common.excel import DoExcel
from common.readconfig import ConfigLoader
from common.request import Http_Request
from common.os_path import QuanZi_case_dir
from ddt import ddt,data,unpack
from common.mysql_uitl import MysqlUtil



@ddt
class new_quanzi(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("新增圈子")


    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle where id != '' order by id  desc limit 1; "

        global max_uuid
        max_uuid = mysql.fetch_one(sql)['id']  # 事先查出来圈子表中最新的id,也就是最新的那个圈子


    @data(*quanzi_case)
    def test_01(self,case):
        # 必要数据的处理
        header = json.loads(ConfigLoader().get('header', 'header_value'))
        data = json.loads(case.data)

        # 接口参数的值随机选
        data['title'] = data['title'] + str(random.randint(0,550)) # 圈子名字拼接，降低名字重复的几率
        data['base_join_num'] = str(random.randint(100,1500))  # 圈子加入人数初始值，取个随机数


        print(("用例id:{0},用例标题:{1}".format(case.case_id,case.title)))
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求时报错:%s"%e)
            raise e
        # 断言
        result = res.get_json()
        print("请求结果:%s"%result)

        if result['success'] == 'True':  #如果接口返回True
            # 接口成功,对应的数据库圈子表中id要+1
            expected = max_uuid+1 # 期望结果
            self.assertEqual(expected,mysql.fetch_one("select * from message.message_circle where id != '' order by id  desc limit 1; ")['id'])

    def test_02(self):
        pass

    @classmethod
    def tearDownClass(cls):
        mysql.close()

if __name__ == '__main__':
    unittest.main()