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




@ddt
class new_channels(unittest.TestCase):
    case_list = [{"case_title": "新增文本频道", "method": "post", "url": "/v1/channels/create",
                  "data": {"server_id": "1192098200014553088", "channel_name": Random().create_name(),"channel_desc":"新增文本频道","channel_type":"1","parent_id":"","channel_pwd":""}, "expected": "0"},

                 {"case_title": "新增语音频道", "method": "post", "url": "/v1/channels/create",
                  "data": {"server_id": "1192098200014553088", "channel_name": Random().create_name(),"channel_desc":"新增语音频道","channel_type":"2","parent_id":"","channel_pwd":""}, "expected": "0"},

                 {"case_title": "新增分类", "method": "post", "url": "/v1/channels/create",
                  "data": {"server_id": "1192098200014553088", "channel_name": Random().create_name()[0:3],"channel_desc":"新增一个分类","channel_type":"3","parent_id":"","channel_pwd":""}, "expected": "0"},
                 {"case_title": "异常参数值", "method": "post", "url": "/v1/channels/create",
                  "data": {"server_id": "1192098200014553088", "channel_name": Random().create_name()[0:3],"channel_desc":"新增一个分类","channel_type":"4","parent_id":"","channel_pwd":""}, "expected": "422"}
                 ]

    global channel_id
    channel_id = None

    @classmethod
    def setUpClass(cls):
        # header读出来
        cls.header = json.loads(Read_Config().get("Headers", "header"))
        # 去掉ResourceWarning
        warnings.simplefilter("ignore", ResourceWarning)

        # 提前查出数据库中的数据，做断言用
        # sql = ""
        # cls.mysql = Mysql_().fetchaone(sql)

    @data(*case_list)
    def test_001(self,case):
        res = Http_Request(method=case['method'],url=case['url'],data=case['data'],header=self.header,cookie=None)
        result = res.get_json()
        My_Logger().debug("接口返回%s"%result)
        if result['code'] == 0 :

            self.channel_id = result['channel_id']
        else:
            self.channel_id = None

        try:
            self.assertEqual(int(case['expected']),result['code'])
        except AssertionError as e:
            My_Logger().info("用例失败,失败原因{0},\n接口实际code:{1}".format(e, res.get_json()['code']))
            My_Logger().debug(e)
    def tearDown(self):
        # 删除频道
        '''data = {"case_title": "删除新增得频道", "method": "post", "url": "/v1/channels/delete",
                  "data": {"channel_id":self.channel_id}, "expected": "0"}
        try:
            res = Http_Request(method=data['method'],url=data['url'],data=data['data'],header=self.header,cookie=None)
        except Exception as e:
            My_Logger().info("删除失败,失败原因: {}".format(e))
            My_Logger.debug(e)'''

    # @classmethod
    # def tearDownClass(cls):
    #     pass
    #     # cls.mysql.close()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(new_channels('test_001'))
    runner = unittest.TestRunner()
    runner.run(suit)


