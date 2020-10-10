import unittest
import json
import configparser
import warnings
import requests
from common.Request import Request
from common.Configs import read_config
from common.Logger import My_Logger
from ddt import ddt,data,unpack
from common import Pash
from common.Base import Context

# 获取好友列表--->选择好友创建群聊--->修改群聊信息--->踢出群聊成员--->离开群聊

class hh(unittest.TestCase):
    global _id
    _id = None
    header = {}
    header['Content-Type'] = read_config().get('header', 'type')
    header['Auth-Token'] = read_config().get('header', 'token')

    def setUp(self):
      warnings.simplefilter('ignore', ResourceWarning)
      print("-------------------------------------------------开始-------------------------------------------------")

    def test_001(self):
      url = "https://test-api.wefunapp.cn/v1/friend/index"
      data = {"online_status": "", "page": "", "row": ""}
      try:
        re = requests.post(url=url, data=data, headers=self.header)
        My_Logger().info("获取好友：%s"%re.json())
      except Exception as e:
        My_Logger().error("报错:获取好友接口-> %s"%e)
        raise e

    # 创建群聊
    def test_002(self):
      url = "https://test-api.wefunapp.cn/v1/friend/create-crowd"
      data = {"members": ["1212124358370131968","1190659892201914368","1186674854070321152"]}
      try:
        re = requests.post(url=url, data=json.dumps(data), headers=self.header)
        result = re.json()

        # 如果创建成功，存入id以供后面接口使用
        if result['server_id']:
          self._id = result['server_id']
          setattr(Context,'id',result['server_id'])
        My_Logger().info("创建群聊：%s"%re.json())
      except Exception as e:
        My_Logger().error("错误接口：创建群聊--> %s"%e)
        raise e

    # 修改群聊资料
    def test_003(self):
      url = "https://test-api.wefunapp.cn/v1/friend/update-crowd-info"
      data = {"channel_id":getattr(Context,'id'),"channel_name":"s","icon":"4e8ecc9a65c44d16aede57ea9389d831.jpeg"}
      try:
        re = requests.post(url=url, data=json.dumps(data), headers=self.header)
        My_Logger().info("修改群资料：%s"%re.json())
      except Exception as e:
        My_Logger().error("错误接口：修改群资料--> %s"%e)
        raise e

    # 踢出群聊
    def test_004(self):
      url = "https://test-api.wefunapp.cn/v1/friend/delete-member"
      data = {"server_id":getattr(Context,'id'),"member_id": ["1212124358370131968","1190659892201914368","1186674854070321152"]}
      try:
        re = requests.post(url=url, data=json.dumps(data), headers=self.header)
        My_Logger().info("踢出群聊：%s"%re.json())
      except Exception as e:
        My_Logger().error("错误接口：踢出群聊--> %s"%e)
        raise e
    def tearDown(self):
      print("-------------------------------------------------结束-------------------------------------------------")



if __name__ == '__main__':
    unittest.main()
