import unittest
import json
import requests
import configparser
import warnings
from common.Request import Request
from common.Configs import read_config
from common.Logger import My_Logger
from ddt import ddt,data,unpack
from common import Pash
from common.Base import Context


# 修改社区备注名    修改好友备注名
class remarks(unittest.TestCase):
    header = {}
    header['Content-Type'] = read_config().get('header', 'type')
    header['Auth-Token'] = read_config().get('header', 'token')



    url = "https://test-api.wefunapp.cn/v1/friend/set-remark"
    data = {
        "friend_id":"",
        "remark":""
    }


    def test_001(self):
        re = requests.post(url=url,data=json.dumps(data),headers = self.header)