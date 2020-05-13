# 获取领域列表
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
class get_domain_list(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("获取领域列表")

    def setUp(self):
        global mysql
        mysql = MysqlUtil()

        global max_counts
        max_counts = mysql.fetch_all("select * from message.message_circle_field where id != '' order by id desc ") # 事先查出所有的领域


    @data(*quanzi_case)
    def test_01(self,case):
        header = json.loads(ConfigLoader().get("header","quanzi_value")) # 请求头
        data = json.loads(case.data) # excel 中读取的字典，是str类型，需要json化，因为接口只接收json格式参数

        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求报错:%s"%e)
            raise e
        result = res.get_json()

        self.assertEqual(case.expected,result['success'])
        print(result['data']['counts'])

        if result['message'] == '成功' and case.url == '/message/circle/sys/queryMessageCircleField':
            self.assertEqual(result['data']['counts'],len(max_counts))  #获取领域列表的接口，返回的值counts与数据库中查出的数据条数一致，PASS




    def tearDown(self):
        mysql.close()

if __name__ == '__main__':
    unittest.main()



