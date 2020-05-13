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
class get_vote_list(unittest.TestCase): #
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('圈子下问答投票列表')

    @classmethod
    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle_vote_questions where circle_uuid = '555c54bb67a546569969e8c5d8d0c538';"
        global vote_max
        vote_max = mysql.fetch_all(sql) # 事先从数据库中查出来，第四个圈子下的投票（存在一个圈子下，多个投票的情况，所以返回list）

    @data(*quanzi_case)
    def test_01(self,case):
        # 必要数据的处理
        header = json.loads(ConfigLoader().get('header', 'header_value')) # 从配置文件读取请求头
        data = json.loads(case.data) # excel中读取出来的字典，最开始是str类型，请求接口时需要dict，所以要吧str转成dict


        # 发起接口请求
        try:
            res = Http_Request(case.method, case.url, data, headers=header)
        except Exception as e:
            print("接口请求时报错:%s"%e)
            raise e

        # 对接口请求进行断言
        result = res.get_json()
        print("请求结果%s"%result)
        self.assertEqual(case.expected,result['success']) # 期望结果=excel中的True,实际结果=请求结果中success的值；期望结果 = 实际结果，接口断言通过
        # 数据库断言(接口查询出来有个counts)
        if result['success'] and result['message']:
            self.assertEqual(len(vote_max),result['data']['counts']) # 数据库中查出的数据条数 = 接口响应的条数，PASS

    @classmethod
    def tearDown(self):
        mysql.close() # 关闭数据库连接




if __name__ == '__main__':
    unittest.main()