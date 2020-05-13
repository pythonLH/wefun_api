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

# 获取最新领域详情，然后修改最新领域的  启用/禁用 状态
@ddt
class get_domain(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("获取领域修改状态")


    def setUp(self):
        print("============================开始测试============================")
        global mysql
        mysql = MysqlUtil()
        global newest
        newest = mysql.fetch_one("SELECT * FROM message.`message_circle_field` where id != '' order by id  desc limit 1;")# 事先查出最新的领域

    @data(*quanzi_case)
    def test_01(self,case):
        # 参数json化
        header = json.loads(ConfigLoader().get("header","header_value"))
        data = json.loads(case.data)

        # 参数补全，因为excel中为空 ,防止id写死就需要最新的field_uuid
        if data['field_uuid'] == '':
            data['field_uuid'] = newest['uuid']
        else:
            data['field_uuid'] = data['field_uuid']

        # 发起请求
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e :
            print("请求报错:%s"%e)
            raise e

        result = res.get_json()
        print("请求结果:%s"%result)
        # 修改领域状态,用例参数补全

        data['status'] = '2'

        # 断言
        self.assertEqual(case.expected,result['success'])

        if result['success'] == 'True' and case.url =="/message/circle/sys/updMessageCircleFieldStatus": # 如果测试跑的是，修改领域状态，则接口请求成功，做数据库校验
            self.assertNotEqual(newest['status'],mysql.fetch_one("SELECT * FROM message.`message_circle_field` where id != '' order by id  desc limit 1;")['status'])


    def tearDown(self):
        print("============================结束测试============================")
        mysql.close()
if __name__ == '__main__':
    unittest.main()

