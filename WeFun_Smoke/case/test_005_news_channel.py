import unittest
import json
import configparser
import warnings
from common.Request import Request
from common.Configs import read_config
from common.Logger import My_Logger
from ddt import ddt,data,unpack
from common import Pash
from common.Base import Context
from common.random_name import Random


# 新增文本频道-->文本频道中发送消息-->清除新频道
@ddt
class send_message(unittest.TestCase):
    global channel_id
    channel_id = None

    # 请求头
    header = {}
    header['Content-Type'] = "application/x-www-form-urlencoded" # 这个创建社区频道/分类的接口，header中的type2 = application/x-www-form-urlencoded,只能用这个先处理下
    header['Auth-Token'] = read_config().get('header', 'token')


    case_list = [
        {"title": "发送文本内容消息", "method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/message-post",
            "data": {"channel_id": None, "content": "测试频道消息正常发布"}, "expected": "0"},

        {"title": "发送表情内容消息", "method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/message-post",
            "data": {"channel_id": None, "content": "[斜眼笑]"}, "expected": "0"},

        {"title": "发送图片内容消息", "method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/message-post",
            "data": {"channel_id": None, "content": "http://g.hiphotos.baidu.com/zhidao/pic/item/c83d70cf3bc79f3d6e7bf85db8a1cd11738b29c0.jpg"}, "expected": "0"}

        ]

    @classmethod
    def setUpClass(cls):
        warnings.simplefilter("ignore", ResourceWarning)# 去掉ResourceWarning

    # 1-->新增文本频道
        data = {"title": "新增文本频道",
                "method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/create",
                "data": {"server_id": "1277254596447698944",
                         "channel_name": Random().create_name(),
                         "channel_desc":"新增文本频道",
                         "channel_type":"1",
                         "parent_id":"",
                         "channel_pwd":""}
                }
        try:
            re = Request(method=data['method'],
                             url=data['url'],
                             data=data['data'],
                             header=cls.header)
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%data['title']%e)
            raise e

        result = re.get_json()
        if result['code'] == 0:
            print(data['title'] +"-->成功 %s" % result)
        else:
            print(data['title'] +"-->失败 %s" % result)
            My_Logger().info(data['title'] +"-->失败 %s"%result)

        # 处理数据依赖
        if result['code'] == 0:
            cls.channel_id = result['channel_id']
        else:
            pass
    # 2-->测试频道中发布各种消息
    @data(*case_list)
    def test_001(self,case):
        if case['data']['channel_id'] == None:
            case['data']['channel_id'] = self.channel_id
        try:
            re = Request(method=case['method'],
                             url=case['url'],
                             data=case['data'],
                             header=self.header)
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%case['title']%e)
            raise e
        # 接口结果写入报告
        result = re.get_json()
        if result['code'] == 0:
            print(case['title'] +"-->成功 %s" %result)
        else:
            print(case['title'] +"-->失败 %s" % result)
            My_Logger().info(case['title'] +"-->失败 %s"%result)
        # 接口断言
        try:
            self.assertEqual(int(case['expected']), result['code'])
        except AssertionError as e:
            My_Logger().info(case['title'] +"断言错误: %s"%e)

    # 3-->删除这个频道(包括发布的消息)
    @classmethod
    def tearDownClass(cls):
        data = {"case_title": "删除新增得频道", "method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/delete",
                "data": {"channel_id": cls.channel_id}, "expected": "0"}
        try:
            res = Request(method=data['method'],
                          url=data['url'],
                          data=data['data'],
                          header=cls.header,)
            print('删除频道接口: %s'%res.get_json())
        except Exception as e:
            My_Logger().error("删除失败,失败原因: %s"%e)
            raise e


if __name__ == '__main__':
    unittest.main()