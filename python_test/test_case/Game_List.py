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


class gte_game_list(unittest.TestCase):
    header = json.loads(Read_Config().get("Headers", "header"))
    data = {"case_title": "获取游戏列表", "method": "get", "url":"/game/get-game-list",
            "data": {}}



    def setUp(self):
        print("================================开始获取================================")
        warnings.simplefilter("ignore", ResourceWarning)
        # 提前从数据库中查出来，数据库中的游戏个数
        mysql = Mysql_()
        global game
        game_sql = 'SELECT * FROM `t_game` '
        game = len(mysql.fetchall(game_sql))

    def test_get_list(self):
        try:
            res = Http_Request(method=self.data['method'], url=self.data['url'], data=self.data['data'], header=self.header,cookie=None)
            result = res.get_json()
            self.assertEqual(0,int(result['code']))
        except Exception as e:
            My_Logger().error("接口调用报错，检查Auth-Token")
            My_Logger().debug(e)


        list = []
        if result['code'] == 0:
            for i in result['data']:
                list.append(i)
        else:
            My_Logger().error("请求报错%s"%result['code'])

        My_Logger().debug("接口获取到的游戏总数:%d"%len(list))

        for i in result['data']:
            print(i)
        # 接口调用成功，要验证接口查出来的数据 跟数据库中是否相符
        if result['code'] == 0:
            self.assertEqual(len(list),game)
        else:
            passs

    def tearDown(self):
        print("================================结束获取================================")
        Mysql_().close_mysql()


if __name__ == '__main__':
    unittest.main()