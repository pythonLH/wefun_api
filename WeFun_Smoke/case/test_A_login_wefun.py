import unittest
import configparser
import json
import warnings
from common.Request import Request
from common.Configs import read_config
from common.Logger import My_Logger
from ddt import ddt,data,unpack
from common import Pash
from common.Base import Context

# 获取验证码---->使用验证码登录---->登录后的token写入配置文件
@ddt
class login(unittest.TestCase):
    header = {'Content-Type':'application/json; charset=UTF-8'}
    global verify_code
    verify_code = None


    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self):
        login = {"title": "验证码登录",
         "method": "post",
         "url": "https://test-api.wefunapp.cn/login/dynamic-code",
         "data": {"telephone": "18888888888", "verify_code": self.verify_code, "login-type": "0"},
         "expected": "send success"}
        try:
            re = Request(login['method'],login['url'],json.dumps(login['data']),self.header)
            if re.get_json()['code'] == 0:
                print("登录成功")
            else:
                print("登录失败 %s"%re.get_json())
                My_Logger().debug("登录失败")
        except Exception as e:
            My_Logger().error("错误接口：登录接口--> %s"%e)
            raise e
        # 登录成功后的token写入配置文件，便于后面的接口使用
        type = "application/json; charset=UTF-8"
        value = json.loads(re.get_text())['api_token']

        # cookies
        for i in re.get_cookie():
            k = str(i).split(" ")[1]
        with open(r'D:\WeFun Smoke\configs\cookie.txt','w+') as file:
            file.write(k)

        set_conf = configparser.ConfigParser()
        set_conf.add_section('header')
        set_conf.set('header','type',type)
        set_conf.set('header','token',value)
        with open(Pash.token_dir, 'w+') as fw:
            set_conf.write(fw)


    git_code = [{"title":"获取验证码",
                   "method":"post",
                   "url":"https://test-api.wefunapp.cn/verify-code/send",
                   "data":{"telephone":"18888888888","scenario":"login-dynamic-code"},
                   "expected":"send success"
                  }]

    @data(*git_code)
    def test_code(self,case):
        try:
            re = Request(case['method'],case['url'],json.dumps(case['data']),self.header)
            print("获取验证码--> %s"%re.get_json())
        except Exception as e:
            My_Logger().error("错误接口：获取验证码--> %s"%e)
            raise e

        # 获取验证码成功，就把获取到的验证码，传入全局变量以供登录时调用
        self.assertEqual(case['expected'],re.get_json()['msg'])
        if re.get_json()['msg'] == "send success":
            self.verify_code = re.get_json()['verify_code']

if __name__ == '__main__':
    unittest.main()



