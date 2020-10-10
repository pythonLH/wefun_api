import unittest
import configparser
import json
import warnings
import pymysql
import random
from common.Request import Request
from common.Configs import read_config
from common.Logger import My_Logger
from ddt import ddt,data,unpack
from common import Pash
from common.Base import Context
from common.random_name import Random
from common.Mysql import MysqlUtil


# 修改个人基本信息

class set(unittest.TestCase):
    header = {}
    header['Content-Type'] = read_config().get('header', 'type')
    header['Auth-Token'] = read_config().get('header', 'token')

    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)
    # 每次调修改名字前，都会先去数据库，将此用户设置为  现在就"修改名字"，不用等时间，因为wefun修改昵称需要等待60天间隔时间
        sql = "update `t_vip` set update_nickname_time = '1577808000' where telephone = '18888888888'"
        self.mysql = MysqlUtil()
        self.mysql.fetch_one(sql)
        self.mysql.commit()


    # 测试数据
    picture_list = ["http://img2.woyaogexing.com/2020/08/26/39a147f5f6bc4e2c94470e4628f7fe5e!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/24/21269c6f21054deebe64cf5dda71f14b!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/03/5439185ffbcf47b6b7b2d43a4b0646d4!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/02/f2c64c6d67334289abab21ab5208621e!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/26/8076a025d99b484a8d5192a224a8d517!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/09/d13d5fbbc2834801bd307149235a15f3!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/21/8bdf8bd0e6704efd825cf56f96512354!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/13/b4a5b74dc68f43bb8df35bee497c2aa5!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/07/4548195c03f64752aaf7e5326b430830!400x400.jpeg",
                    "http://img2.woyaogexing.com/2020/08/01/4e8ecc9a65c44d16aede57ea9389d831!400x400.jpeg"]
    data = {"title": "设置资料", "method": "post", "url": "https://test-api.wefunapp.cn/v1/vip/update-profile",
                "data":{"nickname":Random().create_name(),"avatar":random.choice(picture_list),"sex":"1"}}

    def test_001(self):
        try:
            re = Request(method=self.data["method"], url=self.data['url'], data=json.dumps(self.data['data']), header=self.header)
            result = re.get_json()
            print("设置资料： %s"%result)
        except Exception as e:
            My_Logger().error("错误接口: %s%s"%self.data['title']%e)
            raise e

            # 断言--->如果传入的名字/图片，跟接口调用之后，数据库中的名字一致，测试PASS
            if result['code'] == 0:
                self.assertEqual(data['data']['nickname'],self.mysql.fetch_one("select * from `t_vip` where telephone = '18888888888'")[0]["nickname"])
                self.assertEqual(data['data']['avatar'],self.mysql.fetch_one("select * from `t_vip` where telephone = '18888888888'")[0]["avatar"])


    def tearDown(self):

        # 关闭数据库连接
        self.mysql.close()


if __name__ == '__main__':
    unittest.main()