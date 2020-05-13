import unittest
import time
import requests
import json
import random
from common.excel import DoExcel
from common.readconfig import ConfigLoader
from common.request import Http_Request
from common.os_path import QuanZi_case_dir
from ddt import ddt,data,unpack
from common.mysql_uitl import MysqlUtil
from common.random_number import PhoneNOGenerator # 随机名字之类的封装

@ddt
class alter_domain(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("修改领域")

    def setUp(self):
        global mysql
        mysql = MysqlUtil()

        global domain
        domain = mysql.fetch_one("SELECT * FROM message.`message_circle_field` where id != '' order by id  desc limit 1;")


    @data(*quanzi_case)
    def test_01(self,case):
        header = json.loads(ConfigLoader().get("header","header_value"))
        data = json.loads(case.data)

        if data['field_uuid'] == '':
            data['field_uuid'] = domain['uuid']
            data['fieldName'] = PhoneNOGenerator().stochastict_name()

        res = Http_Request(case.method,case.url,data,headers=header)
        result = res.get_json()
        self.assertEqual(case.expected,result['success'])

        if result['success'] == 'True':
            self.assertNotEqual(domain,mysql.fetch_one("SELECT * FROM message.`message_circle_field` where id != '' order by id  desc limit 1;"))


if __name__ == '__main__':
    unittest.main()



