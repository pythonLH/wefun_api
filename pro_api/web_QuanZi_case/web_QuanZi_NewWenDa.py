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
class quanzi_new_wenda(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('新增问答')


    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle_vote_questions where id != '' order by id desc limit 1;"
        global max_id
        max_id = mysql.fetch_one(sql)['id'] # 事先取出数据库中，未新增问答前的最大id，因为后面接口新增成功，数据库中id会+1


    @data(*quanzi_case)
    def test_01(self,case):
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))


        if data['title'] != None: # 对测试用例中的问答名字，做一个拼接处理
            data['title'] = data['title'] + str(random.randint(1,876))
        else:
            data['title'] = data['title'] # 如果测试用例中，title参数值为None 就保持不变

        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求时报错:%s"%e)
            raise e
        # 断言
        result = res.get_json()
        print("请求结果:%s"%result)

        self.assertEqual(case.expected,result['success'])

        # 如果接口请求成功，数据库中数据产生变化，做数据库校验
        if result['message'] == '成功':
            expected = max_id + 1

            actual_id = mysql.fetch_one("select * from message.message_circle_vote_questions where id != '' order by id desc limit 1;")['id']

            self.assertEqual(expected,actual_id)
        # 如果接口请求false,数据库中数据不变化，做数据库校验
        else:
            self.assertEqual(max_id,mysql.fetch_one("select * from message.message_circle_vote_questions where id != '' order by id desc limit 1;")['id'])

    def tearDown(self):
        mysql.close()

if __name__ == '__main__':
    unittest.main()
