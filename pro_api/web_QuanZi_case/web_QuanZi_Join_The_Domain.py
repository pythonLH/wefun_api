# 圈子加入领域
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
class quanzi_join_domain(unittest.TestCase):
    circle_case = DoExcel(QuanZi_case_dir).get_case("圈子加入领域")

    def setUp(self):
        global mysql
        mysql = MysqlUtil()# 数据库实例化

        global max_circle_field_link # 把圈子领域信息表中最大值查出来
        max_circle_field_link = mysql.fetch_one("select * from message.message_circle_field_link where id != '' order by id desc;")['id']

        global enabled_circle,enabled_domain # 四个全局变量，参数中要用到：启用的圈子/禁用的圈子 启用的领域/禁用的领域

        # 事先从数据库查出需要的参数
        enabled_circle = mysql.fetch_one("select * from message.message_circle"
                                         " where `status` = 1 and uuid "
                                         "not in(select circle_uuid from message.message_circle_field_link where `status` = 2 ) "
                                         "order by id  desc limit 1;") # 查出可以加入领域的圈子


        enabled_domain = mysql.fetch_one("select * from message.message_circle_field where id != '' and status = 2  order by id desc limit 1 ;") # 启用状态领域


    @data(*circle_case)
    def test_01(self,case):
        header = json.loads(ConfigLoader().get("header","quanzi_value"))
        data = json.loads(case.data)

        # 参数补全
        if data['circle_uuid'] == '': # 圈子加入领域-正常加入，参数补齐
            data['circle_uuid'] = enabled_circle['uuid']
            data['field_uuid'] = enabled_domain['uuid']

        # 发起请求
        try:
            res = Http_Request(case.method,case.url,data,headers=header)
        except Exception as e:
            print("接口请求报错:%s"%e)
            raise e

        # 断言(接口断言/数据库校验)
        result = res.get_json()
        self.assertEqual(case.expected,result['success'])
        if result['message'] == '成功':
            # 圈子成功加入领域，那么圈子领域circle_field_link 表中数据会增加
            self.assertEqual(max_circle_field_link + 1,mysql.fetch_one("select * from message.message_circle_field_link where id != '' order by id desc;")['id'])

    def tearDown(self):
        mysql.close()

if __name__ == '__main__':
    unittest.main()
