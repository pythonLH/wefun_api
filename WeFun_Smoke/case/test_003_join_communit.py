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

# 搜索社区 --->加入社区--->取消社区

@ddt
class join(unittest.TestCase):
    header = {}
    header['Content-Type']= read_config().get('header','type')
    header['Auth-Token'] = read_config().get('header','token')

    case_data = [
        {"title": "社区搜索", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/search",
         "data": {"server_name": "乐园社区"},"expected": "0"},
        {"title": "社区加入", "method": "post", "url": "https://test-api.wefunapp.cn/v1/servers/join",
         "data": {"server_id": getattr(Context,'server_id')},"expected": "0"},
        {"title":"离开社区","method":"post","url":"https://test-api.wefunapp.cn/v1/servers/exit","data":{"server_id": getattr(Context,'server_id')},"expected": "0"}
    ]

    def setUp(self):

        warnings.simplefilter('ignore', ResourceWarning)

    @data(*case_data)
    def test_serch(self,case):
        try:
            re = Request(case['method'],case['url'],json.dumps(case['data']),header=self.header)
            result = re.get_json()
            print(case['title'],result)
            if result['code'] == 0:
                print(case['title'] + "-->成功 %s"%result)
            else:
                print(case['title'] + "-->失败 %s" % result)
                # 失败的写到日志去
                My_Logger().info(case['title'] + "-->失败 %s"%result)
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%case['title']%e)
            raise e

        # 断言
        try:
            self.assertEqual(int(case['expected']),result['code'])
        except Exception as e:
            My_Logger().error(case['title']+"断言失败: %s"%e)

if __name__ == '__main__':
    unittest.main()
