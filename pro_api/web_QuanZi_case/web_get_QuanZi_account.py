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
class get_short_account(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("圈子内短账号列表")

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql_1 = "select * from message.message_circle_link_account where circle_uuid = '555c54bb67a546569969e8c5d8d0c538' and join_type = 0 and `status` = 1;" #第四个圈子关联账号
        sql_2 = "select * from message.message_circle_link_account where circle_uuid = 'd41b03780174469ba858a3db5ae0f05d' and join_type = 0 and `status` = 1;" #第三个圈子关联账号
        global four_max,three_max # 声明全局变量
        four_max = mysql.fetch_all(sql_1) # 查询出第四个圈子，下属短账号，返回的是list
        three_max = mysql.fetch_all(sql_2)

    @data(*quanzi_case)
    def test_01(self,case):
        # 从excel配置文件读出来的数据处理
        data = json.loads(case.data)
        header = json.loads(ConfigLoader().get('header', 'header_value'))

        # 发起接口请求
        print(("用例id:{0},用例标题:{1}".format(case.case_id, case.title)))
        try:
            res = Http_Request(case.method, case.url, data, headers=header)
        except Exception as e:
            print("请求时报错:%s" % e)
            raise e
        print("请求结果:{}".format(res.get_json()))
        # 接口请求的断言
        result = res.get_json()
        self.assertEqual(result['success'],case.expected)

        # 接口请求结果，与数据库中结果校验
        if result['success'] and result['message']:
            if data['circle_uuid'] == '555c54bb67a546569969e8c5d8d0c538': # 如果用例中uuid = 555c54bb67a546569969e8c5d8d0c538
                self.assertEqual(result['data']['counts'],len(four_max))  # 比对接口获取的值，跟数据库中的条数，一致则PASS

            elif data['circle_uuid'] == 'd41b03780174469ba858a3db5ae0f05d':
                self.assertEqual(result['data']['counts'],len(three_max))
        else:
            pass
            # 如果接口请求不成功，接口断言就会失败，就不会走下面的数据库校验了


if __name__ == '__main__':
    unittest.main()
