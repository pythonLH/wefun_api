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
class get_quanzi_list(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('圈子列表')


    def setUp(self):

        print("==================================开始测试==================================")


    @data(*quanzi_case)
    def test_01(self,case):

        # excel 配置文件读出来的数据，做处理
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        print(("用例id:{0},用例标题:{1}".format(case.case_id,case.title)))
        res = Http_Request(case.method, case.url, data, headers=header)
        result = res.get_json()
        print("请求结果:%s"%result)

        self.assertEqual(case.expected,result['success'])


    def tearDown(self):
        print("==================================开始测试==================================")



if __name__ == '__main__':
    unittest.main()
