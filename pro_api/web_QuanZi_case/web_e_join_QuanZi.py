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
class join_quanzi(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("用户移除或者加入圈子")



    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        sql_1 = "select * from message.message_circle_link_account " \
                "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
                "and account_uuid = 'eab0303b2db04247add02ad2f0d13682'"
        global join_status
        join_status = mysql.fetch_one(sql_1)['status'] # 提前查出：第一条用例时"开心就好"在第四个圈子中的状态,应该是为0
                                                                  #第二条用例时"开心就好"在第四个圈子中的状态,应该是为1

    @data(*quanzi_case)
    def test_001(self,case):
        # 从excel配置文件读出来的数据处理
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
        result =res.get_json()
        self.assertEqual(result['success'],case.expected)

        if result['success'] == True and result['message'] == '成功':
            # 接口请求成功后，查出"开心就好"在第四个圈子的状态
            mysql_expected = mysql.fetch_one("select * from message.message_circle_link_account where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' and account_uuid = 'eab0303b2db04247add02ad2f0d13682'")
            # 第一条用例调用后status是1；第二条用例调用后然后变成0
            self.assertNotEqual(join_status,mysql_expected['status']) # 接口调用前的状态，跟接口调用后的状态，bu一致PASS

    def tearDown(self):
        mysql.close()


if __name__ == '__main__':
    unittest.main()

