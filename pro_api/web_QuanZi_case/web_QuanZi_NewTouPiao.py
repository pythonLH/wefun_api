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
class quanzi_wenda(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('新增投票')



    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle_vote_questions where id != '' order by id desc limit 1; "
        global max_id
        max_id = mysql.fetch_one(sql)['id'] # 事先查出最新的圈子投票id

    @data(*quanzi_case)
    def test_001(self,case):
        header = json.loads(ConfigLoader().get('header', 'header_value'))
        data = json.loads(case.data)
        data['title'] = data['title'] + str(random.randint(1,521)) # 从用例中取出来名字，做个拼接

        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            raise e

        result = res.get_json()
        self.assertEqual(case.expected,result['success'])


        if result['success'] == 'True':
            expected = max_id + 1 # 请求接口成功后，id 会+1
            self.assertEqual(expected,mysql.fetch_one("select * from message.message_circle_vote_questions where id != '' order by id desc limit 1;"))

    def tearDown(self):
        mysql.close()

if __name__ == '__main__':
    unittest.main()
