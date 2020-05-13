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
class alter_wenda(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('修改问答')

    def setUp(self):
        global mysql
        mysql = MysqlUtil()
        global alter_ago
        sql = "select * from message.message_circle_vote_questions where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' and activity_type = 2 order by id desc limit 1;"
        alter_ago = mysql.fetch_one(sql)  # 事先查出第四个圈子下最新的一个问答

    @data(*quanzi_case)
    def test_01(self,case):
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get("header", "quanzi_value"))

        # 请求参数补全
        if data['uuid'] == '':  # 如果case中读取出来的uuid为空，就从数据库中查出最新的uuid赋上去
            data['uuid'] = alter_ago['uuid']
        else:
            data['uuid'] = data['uuid']
        data['background_img'] = ConfigLoader().get('picture', 'img_url_one')
        data['images'] = ConfigLoader().get('picture', 'img_url_two')

        try:
            res = Http_Request(case.method, case.url, data, headers=header)
        except Exception as e:
            print("请求报错: %s" % e)
            raise e
        result = res.get_json()
        print("请求结果: %s" % result)
        self.assertEqual(case.expected, result['success'])  # 接口断言

        sql_2 = "select * from message.message_circle_vote_questions where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' and activity_type = 1 order by id desc limit 1;"
        if result['success'] == 'True' and result['message'] == '成功':
            result_img = mysql.fetch_one(sql_2)['images']
            self.assertNotEqual(alter_ago['images'], result_img)  # 修改前的图片，跟调接口修改后的接口，不等则PASS


    def tearDown(self):
        mysql.close()
        # 目前数据库不能轻易删除测试数据，如果后续新了数据，要做数据清除就在tearDown写删除的sql就行


if __name__ == '__main__':
    unittest.main()