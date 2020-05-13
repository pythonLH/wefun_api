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
class app_join_quanzi(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("移动端用户加入圈子")

    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle_link_account" \
              " where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
              "and account_uuid = '7cd855be8df149bc86d816add22ec3d3' ;"
        global super_status
        super_status = mysql.fetch_one(sql)['status'] # 事先查出super 用户，在第四个圈子的  状态

    @data(*quanzi_case)
    def test_01(self,case):
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header','quanzi_value')) # 这里取出来的token，是接口文档给得

        # 发起接口请求
        print(("用例id:{0},用例标题:{1}".format(case.case_id, case.title)))
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求接口报错:%s"%e)
            raise e
        print("请求结果:{}".format(res.get_json()))

        # 接口断言
        result = res.get_json()
        self.assertEqual(result['success'], case.expected)

        if result['success'] == True and result['message'] == '成功':
            mysql_expected = mysql.fetch_one("select * from message.message_circle_link_account "
                                             "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' "
                                             "and account_uuid = '7cd855be8df149bc86d816add22ec3d3' ;")
            self.assertNotEqual(super_status,mysql_expected) # 不相等则PASS


    def tearDown(self):
        mysql.close()


if __name__ == '__main__':
    unittest.main()