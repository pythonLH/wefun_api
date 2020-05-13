import unittest
import json
import warnings
from common.Read_Config import Read_Config
from common.Http_Request import Http_Request
from common.My_Logger import My_Logger
from common import Os_Path
from common.Mysql_ import Mysql_
from ddt import ddt,data,unpack
from common.basic_data import Context


# 测试 新增社区，和删除社区
@ddt
class new_community(unittest.TestCase):
    global delete_id
    delete_id = None
    case_list = [{"case_id": "1", "method": "post", "url": "/v1/servers/create",
                  "data": {"server_name": "", "server_icon": ""}, "expected": "0"},

                 {"case_id": "1", "method": "post", "url": "/v1/servers/create",
                  "data": {"server_name": "ee", "server_icon": ""}, "expected": "0"}
                 ]

    def setUp(self):
        # 配置文件中读取出来的数据类型是str，要处理
        self.header = json.loads(Read_Config().get("Headers", "header"))
        # 去掉ResourceWarning
        warnings.simplefilter("ignore", ResourceWarning)

    @data(*case_list)
    def test_001(self,case):
        # 新增社区
        res = Http_Request(method=case["method"],url=case['url'],data=case['data'],header=self.header,cookie=None)
        result = res.get_json()
        if result['code'] == 0:
             self.delete_id = result['server_id']
        # 用例断言
        try:
            self.assertEqual(int(case['expected']),res.get_json()['code'])
            print("测试结果:{}".format(res.get_json()))
        except AssertionError as e:
            My_Logger().info("用例失败,失败原因{0},\n接口实际code:{1}".format(e, res.get_json()['code']))
            My_Logger().debug(e)

    def tearDown(self):

        # 新增测试社区后，还要做数据清除，teardown中，删除新增的测试社区
        data = {"case_id": "3", "method": "post", "url": "/v1/servers/delete","data": {"server_id":self.delete_id}, "expected": "success"}

        # 删除社区
        try:
            res = Http_Request(method=data["method"], url=data['url'], data=data['data'], header=self.header, cookie=None)
        except Exception as e:
            My_Logger().info("删除失败,失败原因: {}".format(e))
            My_Logger().debug(e)


if __name__ == '__main__':
    unittest.main()