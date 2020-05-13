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
class login(unittest.TestCase):
    global verify_code
    verify_code = None
    header = json.loads(Read_Config().get("Headers", "header_two"))

    code_data = [
        {"case_title": "正确手机获取验证码", "method": "post", "url": "/verify-code/send",
            "data": {"telephone": "15198034727", "scenario": ""}, "expected": "0"}
        ]


    @classmethod
    def setUpClass(cls):
        pass


    # 获取验证码
    @data(*code_data)
    def test_001(self,case):

        result = Http_Request(method=case['method'], url=case['url'], data=case['data'], header=self.header,cookie=None)
        print("响应结果：%s"%result.get_json())
        if result.get_json()['code'] == 0 :
            self.verify_code = result.get_json()['verify_code']
        else:
            pass

        try:
            self.assertEqual(int(case['expected']),result.get_json()['code'])
        except AssertionError as e :
            My_Logger().info("断言错误:%s"%e)
            My_Logger().debug(e)


    # def tearDown(self):
    #
    #     data = {"case_title": "C端登录", "method": "post", "url": "/login/dynamic-code",
    #             "data": {"telephone": "15198034727", "verify_code": self.verify_code, "login-type": "1"}, "expected": "0"}
    #     res = Http_Request(data['method'], data['url'], data['data'], header=self.header, cookie=None)
    #     print(res.get_header())
    # 使用验证码登录
    @classmethod
    def tearDownClass(cls):
        #pass
        header = json.loads(Read_Config().get("Headers","header_two"))
        data = {"case_title": "C端登录", "method": "post", "url": "/login/dynamic-code",
            "data": {"telephone": "15198034727", "verify_code": verify_code,"login-type":"1"}, "expected": "0"}

        res = Http_Request(data['method'],data['url'],data['data'],header=header,cookie=None)
        print(res.get_header())
        print(res.get_history())



if __name__ == '__main__':
    unittest.main()