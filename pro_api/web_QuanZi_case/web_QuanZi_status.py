import unittest
import requests
import json
import random
from common.excel import DoExcel
from common.readconfig import ConfigLoader
from common.request import Http_Request  # 这个接口地址不一样，所以用第二个封装的请求
from common.os_path import QuanZi_case_dir
from ddt import ddt,data,unpack
from common.mysql_uitl import MysqlUtil



@ddt
class quanzi_status(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('问答投票详情禁用启用')

    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global newest_id
        sql = "select * from message.message_circle_vote_questions where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' order by id desc limit 1;"
        newest_id = mysql.fetch_one(sql) # 第四个圈子下，最新的问答信息

    @data(*quanzi_case)
    def test_01(self,case):
        # excel和config 读出来的数据，转换成dict
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        # 接口参数传递
        data['uuid'] = newest_id['uuid'] # 这里避免出错，把uuid的值，直接从数据库中取
        if newest_id['status'] == 2: #这里检查下  数据库中最新问答或圈子的状态，因为新增的问答投票，默认是禁用状态
            data['status'] = '1' # 取出来的状态是禁用，那么调用接口就传 1,启用
        elif newest_id['status'] == 1: # 这里检查下  数据库中问答投票的状态
            data['status'] = '2' # 取出来的状态是启用，那么调用接口就传 2,禁用

        # 发起忌口请求
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("请求时报错:%s"%e)
            raise e

        result = res.get_json()
        print("请求结果:%s"%result)

        # 断言(接口断言/数据库校验)
        self.assertEqual(case.expected,result['success'])

        if result['success'] == 'True' and result['message'] == '成功':
            sql_2 = "select * from message.message_circle_vote_questions where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' order by id desc limit 1;"
            self.assertNotEqual(newest_id['status'],mysql.fetch_one(sql_2)['status'])
    def tearDown(self):
        mysql.close()

if __name__ == '__main__':
    unittest.main()



