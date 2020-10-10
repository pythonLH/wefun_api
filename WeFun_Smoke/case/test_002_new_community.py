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


# 新增社区--->删除社区

@ddt
class new(unittest.TestCase):
    global server_id
    server_id =None

    new_case = [
        {"title": "社区创建", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/create",
                 "data": {"server_name": "测试", "server_icon": ""}, "expected": "0"}
    ]   #-------->新增社区得测试用例

    header = {}
    header['Content-Type'] = read_config().get('header', 'type')
    header['Auth-Token'] = read_config().get('header', 'token')
    # header['Cookie'] = open(r'D:\WeFun Smoke\configs\cookie.txt','r+').read()
    def setUp(self):
        # 去掉ResourceWarning
        warnings.simplefilter("ignore", ResourceWarning)

    # 新增社区
    @data(*new_case)
    def test_001(self,case):
        try:
            res = Request(method=case["method"], url=case['url'], data=json.dumps(case['data']), header=self.header)
            result = res.get_json()
            if result['code'] == 0:
                print("创建社区-->成功 %s"%result)
            else:
                print("创建社区-->失败")
            # 如果创建社区成功，就把创建成功得社区id存起来
            if result['server_id']:
                setattr(Context,'new_sercer',result['server_id'])
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%case['title']%e)
            raise e
    # 社区下面创建分类
    def test_002(self):
        header = {}
        header['Content-Type'] = "application/x-www-form-urlencoded"  # 创建社区下面的  分类  频道  需要用到另一个Content-Type
        header['Auth-Token'] = read_config().get('header', 'token')

        case = {"title": "创建分类","method": "post", "url": "https://test-api.wefunapp.cn/v1/channels/create", #---->创建分类
         "data": {"server_id": getattr(Context, 'new_sercer'),"channel_type": "1","channel_name": "test"},"expected": "0"}
        try:
            re =Request(case['method'],case['url'],json.dumps(case["data"]),header=header)
            result = re.get_json()
            if result["code"] == 0:
                print("创建社区中的分类-->成功 %s"%result)
            else:
                print("创建社区中的分类-->失败 %s"%result)
                # 失败的写到日志里面去
                My_Logger().info("创建社区中的分类-->失败 %s"%result)
            self.assertEqual(int(case['expected']),result['code'])
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%case['title']%e)
            raise e

    # 删除社区测试
    def test_003(self):
        case = {"case_id": "2", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/delete", #---->删除社区用例
         "data": {"server_id": getattr(Context,'new_sercer')}, "expected": "success"}
        try:
            re = Request(method=case["method"], url=case['url'], data=json.dumps(case['data']), header=self.header)
            result = re.get_json()
            if result['code'] == 0:
                print("删除社区-->成功 %s"%result)
            else:
                print("删除社区-->失败 %s"%result)
        except Exception as e:
            My_Logger().error("错误接口：删除社区 -->%s"%e)
            raise e



if __name__ == '__main__':
    unittest.main()