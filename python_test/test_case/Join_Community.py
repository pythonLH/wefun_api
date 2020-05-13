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


@ddt
class join_community(unittest.TestCase):
    global server_id
    _id = None

    case_list = [{"case_id": "1", "method": "post", "url": "/v1/servers/join",
                  "data": {"server_id": getattr(Context,'join_id')}, "expected": "0"}
                 ]

    def setUp(self):
        # 配置文件中数据处理
        self.header = json.loads(Read_Config().get("Headers", "header"))
        # 去掉ResourceWarning
        warnings.simplefilter("ignore", ResourceWarning)


    @data(*case_list)
    def test_001(self,case):
        # 加入社区
        try:
            res = Http_Request(method=case['method'],url=case['url'],data=case['data'],header=self.header,cookie=None)
        except Exception as e :
            My_Logger.error("请求出错，错误原因:{}".format(e))
            My_Logger.debug(e)
        if res.get_json()['code'] == 0:
            self._id = getattr(Context,'join_id')


        try:
            self.assertEqual(int(case['expected']),res.get_json()['code'])
        except AssertionError as e:
            My_Logger().info("用例失败,失败原因{0},\n接口实际code:{1}".format(e, res.get_json()['code']))
            My_Logger().debug(e)

    def tearDown(self):
        # 取消关注社区
        data = {"case_id": "1", "method": "post", "url": "/v1/servers/exit","data": {"server_id":self._id}, "expected": "0"}
        try:
            res = Http_Request(method=data['method'],url=data['url'],data=data['data'],header=self.header,cookie=None)
        except Exception as e:
            My_Logger.info("删除失败,失败原因: {}".format(e))
            My_Logger.debug(e)



if __name__ == '__main__':
    unittest.main()