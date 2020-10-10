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

# 生成社区邀请码--->根据邀请码进入社区--->离开社区
@ddt
class new_code(unittest.TestCase):
    # 请求头
    header = {}
    header['Content-Type'] = read_config().get('header', 'type')
    header['Auth-Token'] = read_config().get('header', 'token')
    # 请求数据
    case = [{"title": "生成社区邀请码", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/invite-code",
        "data": {"server_id": 1249029898480123904}, "expected": "0"}]
    case_2 = [{"title": "根据邀请码加入", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/join-with-invite",
        "data": {"invite_code": ""}, "expected": "0"}]


    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)

    # 生成社区邀请码
    @data(*case)
    def test_001(self,case):
        try:
            re = Request(method=case["method"], url=case['url'], data=json.dumps(case['data']), header=self.header)
            result = re.get_json()
            if result['code'] == 0:
                print("生成社区邀请码-->成功 %s"%result)
            else:
                print("生成社区邀请码-->失败 %s"%result)
                # 失败的写道日志里去
                My_Logger().info("生成社区邀请码-->失败 %s"%result)

            # 生成的邀请码存起来
            if re.get_json()['code'] == 0:
                self.case_2[0]["data"]["invite_code"] = re.get_json()['invite_code']
        except Exception as e:
            My_Logger().error("错误接口：生成社区邀请码-->%s"%e)
            raise e

    # 根据社区邀请码加入社区
    @data(*case_2)
    def test_002(self,case):
        try:
            re = Request(method=case["method"], url=case['url'], data=json.dumps(case['data']), header=self.header)
            result = re.get_json()
            if result['code'] == 0:
                print("根据邀请码加入社区-->成功 %s"%result)
            else:
                print("根据邀请码加入社区-->失败 %s"%result)
                My_Logger().info("根据邀请码加入社区-->失败 %s"%result)
        except Exception as e:
            My_Logger().error("错误接口：根据邀请码加入社区-->%s"%e)
            raise e

    # 数据清除，通过邀请码，加入社区成功后，做一个离开社区的操作
    @classmethod
    def tearDownClass(cls):
        cls.header
        data = {"case_id": "离开社区", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/exit",
        "data": {"server_id": 1249029898480123904}, "expected": "0"}
        try:
            re = Request(method=data["method"], url=data['url'], data=json.dumps(data['data']), header=cls.header)
        except Exception as e:
            My_Logger().error("错误接口：离开社区-->%s"%e)
            raise e


if __name__ == '__main__':
    unittest.main()
