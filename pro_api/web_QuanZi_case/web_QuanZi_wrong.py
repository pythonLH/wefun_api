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
class wrong_quanzi(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('搜索非圈子内容加入圈子')

    @data(*quanzi_case)
    def test_01(self,case):
        # 接口需要的参数处理
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        # 发起接口请求
        print(("用例id:{0},用例标题:{1}".format(case.case_id, case.title)))
        try:
            res = Http_Request(case.method, case.url, data, headers=header)
        except Exception as e:
            print("请求时报错:%s" % e)
            raise e
        print("请求结果:{}".format(res.get_json()))

        # 接口断言
        result = res.get_json()
        self.assertEqual(result['success'], case.expected)


if __name__ == '__main__':
    unittest.main()

