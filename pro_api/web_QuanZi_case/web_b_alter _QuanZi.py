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
class alter_quanzi(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case('修改圈子')

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql = "select * from message.message_circle where id != '' order by id  desc limit 1; "
        global max_uuid
        max_uuid = mysql.fetch_one(sql)  # 事先从数据库中查出最新的圈子信息
        print(max_uuid)

    @data(*quanzi_case)
    def test_001(self,case):
        # 接口需要的参数处理
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        data['base_join_num'] = str(random.randint(25, 85))  # 修改圈子加入基数，随机生成
        if data['uuid'] == '': # 如果用例中，uuid为 '' 控制用那条用例来请求接口
            data['uuid'] = max_uuid['uuid']  # 就从数据库中查出，最新圈子uuid作为修改圈子的uuid
            data['title'] = max_uuid['title']
            # 发起请求
            res = Http_Request(case.method, case.url, data, headers=header)
            result = res.get_json()
            self.assertEqual(result['data'],case.expected)

            # 修改成功，要做数据库校验
            if result['data'] == '1' and result['message'] == '成功': #如果接口请求成功，说明图片修改成功
                alter_image = mysql.fetch_one("select * from message.message_circle where id != '' order by id  desc limit 1; ")
                self.assertNotEqual(max_uuid['image'],alter_image) #执行请求前的图，跟请求后的图，不相等PASS
        else:
            data['uuid'] = data['uuid']
            res = Http_Request(case.method, case.url, data, headers=header)
            result = res.get_json()
            self.assertNotEqual(result['status'],case.expected)

    @classmethod
    def tearDownClass(cls):
        mysql.close()
if __name__ == '__main__':
    unittest.main()

