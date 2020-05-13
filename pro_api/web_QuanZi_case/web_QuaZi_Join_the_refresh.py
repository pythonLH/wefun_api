# 投票问答加入刷屏
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
class join_the_refresh(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('问答投票加入刷屏')


    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global newest_vote
        vote_sql = "select * from message.message_circle_vote_questions" \
                   " where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
                   "and activity_type = 1 " \
                   "and status = 1 " \
                   "order by id desc limit 1;"
        newest_vote = mysql.fetch_one(vote_sql) #提前查询出 第四个圈子下，最新的启用状态投票

        global newest_answers
        ans_sql = "select * from message.message_circle_vote_questions " \
                  "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' " \
                  "and activity_type = 2 " \
                  "and status = 1 " \
                  "order by id desc limit 1;"
        newest_answers = mysql.fetch_one(ans_sql) #提前查询出 第四个圈子下，最新的启用状态问答


    @data(*quanzi_case)
    def test_01(self,case):
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get("header","quanzi_value"))


        # 用例中包含"问答"和"投票"的用例，实际调用时uuid 参数要区分下
        if data['uuid'] == '1': # 用例中uuid 写的1，表示用例为"投票的用例"
            data['uuid'] = newest_vote['uuid'] # 就把最新投票的uuid给到接口参数需要的uuid

        elif data['uuid'] == '2': # 用例中uuid 写的2，表示用例为"问答的用例"
            data['uuid'] = newest_answers['uuid'] # 就把最新问答的uuid给到接口参数需要的uuid

        else:
            data['uuid'] = data['uuid']

        # 调用接口
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e :
            print("请求时报错: %s"%e)
            raise e

        result = res.get_json()
        self.assertEqual(case.expected,result['success']) # 接口断言

        # 分别对投票/问答，是否加入刷屏，做接口请求后的数据库校验
        if result['success'] == 'True' and data['uuid'] == newest_vote['uuid']: # 投票
            # 查出接口调用后，加入刷屏的状态，作为实际结果
            vote_expected = mysql.fetch_one("select * from message.message_circle_vote_questions "
                                            "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' "
                                            "and activity_type = 1 "
                                            "and status = 1 order by id desc limit 1;")['is_join_sp']
            # 调用接口前，与调用接口后，状态不等PASS
            self.assertNotEqual(newest_vote['is_join_sp'],vote_expected)

        elif result['success'] == 'True' and data['uuid'] == newest_answers['uuid']: # 问答
            # 查出接口调用后，加入刷屏的状态，作为实际结果
            ans_expected = mysql.fetch_one("select * from message.message_circle_vote_questions "
                                           "where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' "
                                           "and activity_type = 2 "
                                           "and status = 1 order by id desc limit 1;")['is_join_sp']
            # 调用接口前，与调用接口后，状态不等PASS
            self.assertNotEqual(newest_answers['is_join_sp'],ans_expected)


    def tearDown(self):
        mysql.close() # 用例中涉及到数据操作，记得关闭数据库连接




if __name__ == '__main__':
    unittest.main()
