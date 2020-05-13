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


# 生成社区邀请码--->根据邀请码加入社区
@ddt
class code_community(unittest.TestCase):
    header = json.loads(Read_Config().get("Headers", "header"))
    global invite_code
    invite_code = None

    case_list = [
        {"case_title": "生成社区邀请码", "method": "post", "url": "/v1/servers/join-with-invite",
            "data": {"invite_code":None}, "expected": "0"},
        {"case_title": "生成社区邀请码", "method": "post", "url": "/v1/servers/join-with-invite",
            "data": {"invite_code":None}, "expected": "0"}
    ]

    @classmethod
    def setUpClass(cls):
        pass
        # 提前查数据库
        '''invite_result = Mysql_()
        sql = ""
        invite_result.fetchaone(sql)'''

        data = {"case_title": "生成社区邀请码", "method": "post", "url": "/v1/servers/invite-code",
            "data": {"server_id":"1192098200014553088", "expire_hour":"8","limit_count":"100","channel_id":"1192098200060690433"}, "expected": "0"}

        res = Http_Request(data['method'], data['url'], data['data'], header=cls.header, cookie=None)
        result = res.get_json()
        My_Logger().debug("接口响应:{}".format(result))
        if "invite_code" in result.keys():  # 如果字典中有，则为True，修改全局变量
            cls.invite_code = res.get_json()['invite_code']

        else:
            cls.invite_code = None


    @data(*case_list)
    def test_001(self,case):

        if case['data']['invite_code'] == None:
            case['data']['invite_code'] = self.invite_code

        else:
            case['data']['invite_code'] = case['data']['invite_code']

        res = Http_Request(case['method'],case['url'],case['data'],header=self.header,cookie=None)
        result = res.get_json()
        My_Logger().debug("接口响应:{}".format(result))
        try:
            self.assertEqual(result['code'],case['expected'])
        except AssertionError as e:
            My_Logger().info("用例失败,失败原因{0},\n接口实际code:{1}".format(e, res.get_json()['code']))
            My_Logger().debug(e)

    @classmethod
    def tearDownClass(cls):
        pass
        # 关闭数据库链接
        #Mysql_().close_mysql()

if __name__ == '__main__':
    unittest.main()