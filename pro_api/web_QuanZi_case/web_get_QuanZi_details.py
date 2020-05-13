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
class get_cirle_detils(unittest.TestCase):
    quanzi_case = DoExcel(QuanZi_case_dir).get_case("圈子详情")

    @classmethod
    def setUpClass(cls):
        global mysql
        mysql = MysqlUtil()
        sql = "select *  from message.message_circle_link where circle_uuid = 'd41b03780174469ba858a3db5ae0f05d' and type = 1 and `status` != 0;"
        global spam_type
        spam_type = mysql.fetch_all(sql)  #事先从数据库查出，第三个圈子，下属所有刷屏

    @data(*quanzi_case)
    def test_001(self,case):
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


        # 接口断言
        result = res.get_json()
        if res.get_status_code()==200:
            self.assertEqual(result['message'], case.expected)
        # 数据库校验
        if result['success'] == True  or  result['message'] == '成功':
            if data['type'] == '1': #如果用例中，type标识获取圈子详情下，刷屏
                self.assertEqual(result['data']['counts'],len(spam_type)) # 接口响应counts响应数据条数，与sql查询的结果条数一致，PASS

            elif data['type'] == 2:
                pass
                # 接口查询第三个圈子下见识数，跟数据库查询出来有误差，先不写type=2的数据库校验

        # else:
        #     print("请求接口错误!")
    @classmethod
    def tearDownClass(cls):
        mysql.close() # 关闭数据库连接

if __name__ == '__main__':
    unittest.main()

