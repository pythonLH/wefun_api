# 可以加入领域的圈子
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
class may_join_domain(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("获取可以加入领域的圈子")

    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global max_circle
        # 事先从数据库中查出，可以加入领域的 圈子
        max_circle = mysql.fetch_all("select m.title,m.uuid from message.message_circle  m where m.`status`=1 and m.uuid not in (select circle_uuid from message.message_circle_field_link where `status`=2)")
    @data(*quanzi_case)
    def test_001(self,case):
        # 参数json化  请求的参数 和请求的头  都必须是  json格式
        header = json.loads(ConfigLoader().get("header","quanzi_value"))
        data = json.loads(case.data)

        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求报错:%s"%e)
            raise e
        result = res.get_json()
        # print(result)
        self.assertEqual(case.expected,result['success'])

        if data['keyword'] == None and result['message'] == '成功':
            self.assertEqual(len(max_circle),result['data']['counts'])

    def tearDown(self):
        mysql.close()


if __name__ == '__main__':
    unittest.main()