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
class test(unittest.TestCase):
    url = "https://test-api.wefunapp.cn/v1/channels/create"
    data = {"server_id": "1192098200014553088", "channel_name": "一清","channel_desc":"新增文本频道","channel_type":"1","parent_id":"","channel_pwd":""}
    header = {"Content-Type":"application/json; charset=UTF-8","Auth-Token":"MTIzNzgwNzM5OTc2NzYzODAxNg.MA.pY_3-EHIHTXSitUubTaQqk0P1hNZvCGbWRsbS4SX1Vo"}


    re = requests.post(url=url,data=json.dumps(data),headers = header)
    print(re.json())


if __name__ == '__main__':
    unittest.main()