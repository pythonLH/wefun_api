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
class quanzi_issue(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('模拟用户发布内容到圈子')


    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global max_id
        sql = "select * from  message.message_circle_link where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' order by id desc limit 1;"
        max_id = mysql.fetch_one(sql)['id'] # 事先查出"第四个圈子"下最新的发布id，因为后面调用发布接口，成功后数据库id会加1

    @data(*quanzi_case)
    def test_01(self,case):
        # 接口需要的参数处理
            data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        print(("用例id:{0},用例标题:{1}".format(case.case_id, case.title)))
        # 发起接口请求
        try:
            res = Http_Request(case.method, case.url, data, headers=header)
            print(res.get_url())
        except Exception as e :
            print("请求报错%s"%e)
            raise e
        print("请求结果:{}".format(res.get_json()))


        # 接口断言
        result = res.get_json()
        self.assertEqual(result['success'], case.expected)



        # 调用发布接口成功，数据库校验
        if result['success'] == True and result['message'] == '成功':
            expected_id = mysql.fetch_one("select * from  message.message_circle_link where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' order by id desc limit 1;")
            self.assertEqual(max_id+1,expected_id['id'])



    def tearDown(self):

        mysql.close()


if __name__ == '__main__':
    unittest.main()
