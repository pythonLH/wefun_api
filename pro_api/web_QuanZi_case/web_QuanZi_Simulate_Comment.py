# 模拟添加问答回答/投票选择
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
class simulate_comment(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("模拟添加问答投票")


    def setUp(self):
        global mysql
        mysql = MysqlUtil()

        global max_id
        sql = "select * from message.message_circle_vote_questions_link where id != '' order by id desc limit 1;"
        max_id = mysql.fetch_one(sql) # 事先查出最新的投票问答，评论

    @data(*quanzi_case)
    def test_01(self,case):
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get("header","quanzi_value"))

        # 此接口以type判断是问答还是投票，要做用例参数分开传递
        if data['type'] == '1': # 用例中type是1表问答，vote_questions_uuid需要传入问答的uuid
            sql_wenda = "select * from message.message_circle_vote_questions " \
                        "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
                        "and activity_type = 2 " \
                        "and status = 1 order by id desc limit 1;"
            data['vote_questions_uuid'] = mysql.fetch_one(sql_wenda)['uuid']

        elif data['type'] == '2': # 用例中type是2表投票，vote_questions_uuid需要传入投票的uuid
            sql_vote = "select * from message.message_circle_vote_questions " \
                       "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
                       "and activity_type = 1 " \
                       "and status = 1 order by id desc limit 1;"

            data['vote_questions_uuid'] = mysql.fetch_one(sql_vote)['uuid']

        # 调接口
        try:
            res = Http_Request(case.method,case.url,data,headers=header)

        except Exception as e :
            print("请求接口报错:%s"%e)
            raise e

        result = res.get_json()
        print("请求结果:%s"%result)
        self.assertEqual(case.expected,result['success'])


        if result['success'] == 'True' and result['message'] == '成功':
            new_id = mysql.fetch_one("select * from message.message_circle_vote_questions_link where id != '' order by id desc limit 1;")
            self.assertEqual(max_id['id'] + 1 , new_id['id'])

    def tearDown(self):
        mysql.close()


if __name__ == '__main__':
    unittest.main()






