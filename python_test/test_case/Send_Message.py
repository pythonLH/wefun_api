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
from common.PhoneNOGenerator import Random

# 新增频道-->新频道发消息-->清除新频道
@ddt
class send_message(unittest.TestCase):
    global channel_id
    channel_id = None
    header = json.loads(Read_Config().get("Headers", "header"))# header读出来
    case_list = [
        {"case_title": "发布文本消息", "method": "post", "url": "/v1/channels/message-post",
            "data": {"channel_id": None, "content": "测试频道消息正常发布"}, "expected": "0"},

        {"case_title": "通过接口发空消息", "method": "post", "url": "/v1/channels/message-post",
            "data": {"channel_id": None, "content": ""}, "expected": "0"},

        {"case_title": "发送链接消息", "method": "post", "url": "/v1/channels/message-post",
            "data": {"channel_id": None, "content": "http://g.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d6e7bf85db8a1cd11738b29c0.jpg"}, "expected": "0"}

        ]

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)# 去掉ResourceWarning

        # 1-->新增频道
        data = {"case_title": "新增文本频道", "method": "post", "url": "/v1/channels/create",
                  "data": {"server_id": "1192098200014553088", "channel_name": Random().create_name(),"channel_desc":"新增文本频道","channel_type":"1","parent_id":"","channel_pwd":""}}
        result = Http_Request(method=data['method'],url=data['url'],data=data['data'],header=cls.header,cookie=None)
        res_data = result.get_json()
        My_Logger().debug("新增频道返回: %s"%res_data)
        if res_data['code'] == 0:
            cls.channel_id = res_data['channel_id']

        else:
            pass

        # 2-->测试频道中发布各种消息
    @data(*case_list)
    def test_001(self,case):
        if case['data']['channel_id'] == None:
            case['data']['channel_id'] = self.channel_id

        result = Http_Request(method=case['method'], url=case['url'], data=case['data'], header=self.header, cookie=None)
        My_Logger().debug("接口返回%s"%result.get_json())

        try:
            self.assertEqual(int(case['expected']),result.get_json()['code'])
        except AssertionError as e:
            My_Logger().info("用例失败,失败原因{0},\n接口实际code:{1}".format(e, res.get_json()['code']))
            My_Logger().debug(e)

        # 3-->删除这个频道(包括发布的消息)
    @classmethod
    def tearDownClass(cls):
        data = {"case_title": "删除新增得频道", "method": "post", "url": "/v1/channels/delete",
                "data": {"channel_id": cls.channel_id}, "expected": "0"}
        try:
            res = Http_Request(method=data['method'], url=data['url'], data=data['data'], header=cls.header,
                               cookie=None)
            My_Logger().debug('删除返回: %s'%res.get_json())
        except Exception as e:
            My_Logger().info("删除失败,失败原因: {}".format(e))
            My_Logger.debug(e)


if __name__ == '__main__':
    unittest.main()