import unittest
import json
from common.request_ import Request
from common.logger_ import Log
from ddt import ddt, data
from common.login_ import login
from common.redConfig import red_
from common.ptah_object._path import Basfig_path


@ddt
class Login(unittest.TestCase):
    # 请求的参数List
    AddressBook = [
        {
            "title": "上传通讯录:AddressBook",
            "method": "post",
            "url": "/hc/app/userInfo/saveAddressBook",
            "body": [
                {
                    "contactName": "Licenciado",
                    "contactPhone": "+52 449 480 7440",
                    "contactRelation": "",
                    "lastTime": "1661998796390"
                },
                {
                    "contactName": "1422firstcash",
                    "contactPhone": "+52 449 482 0252",
                    "contactRelation": "",
                    "lastTime": "1661998844242"
                },
                {
                    "contactName": "Vicente Ortiz",
                    "contactPhone": "+52 449 496 9413",
                    "contactRelation": "",
                    "lastTime": "1661998880584"
                },
                {
                    "contactName": "Orestamo",
                    "contactPhone": "+52 449 507 7179",
                    "contactRelation": "",
                    "lastTime": "1661999049347"
                },
                {
                    "contactName": "Aquella",
                    "contactPhone": "+52 449 512 8518",
                    "contactRelation": "",
                    "lastTime": "1661999077020"
                },
                {
                    "contactName": "Cash",
                    "contactPhone": "+52 449 514 7208",
                    "contactRelation": "",
                    "lastTime": "1661999122287"
                }]},
        {"title": "查询最大可借天数：queryAvailableProduct",
         "method": "post",
         "url": "/hc/app/loan/queryAvailableProduct",
         "body": {
             "dayRate": "0.77",
             "expectedInstallment": "0",
             "isNew": "1",
             "merchantNo": "01",
             "orgNo": "MEX",
             "prductPayAmountMax": "1300",
             "prductPayAmountMin": "300",
             "productAmount": "0",
             "productFastPayTime": "50",
             "productIntroduce": "testhhh",
             "productLoanTerm": "1",
             "productName": "Préstamos seguros",
             "productNo": "",
             "productPictureUrl": "/upload/image/20220803/2022080301312987180381.png",
             "productTerm": "0",
             "showPeriod": "0",
             "userExpectedAmount": "0",
             "userExpectedTerm": "0"}
         },
        {
            "title": "提交借款申请：submitOneProduct",
            "method": "post",
            "url": "/hc/app/market/submitOneProduct",
            "body": {
                "appList": [{
                    "appName": "MoonVay",
                    "appVersion": "1.0.5",
                    "firstInstallTime": "2022-05-16 10:00:43",
                    "lastUpdateTime": "2022-05-16 10:00:43",
                    "packageName": "app.moon.vay"
                }],
                "attach": [{
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "706A86AC844CA1968434328513F629ED",
                    "newName": "2022100822134953321777.jpeg",
                    "newPathName": "/upload/image/20221008/2022100822134953321777.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "1665285227444595.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "sfzzm",
                    "size": 6758,
                    "uploadType": "image"
                }, {
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "D16BADADB0299041602A2AF74DBD7C52",
                    "newName": "2022100822143953462780.jpeg",
                    "newPathName": "/upload/image/20221008/2022100822143953462780.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "1665285277405318.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "sfzfm",
                    "size": 6749,
                    "uploadType": "image"
                }, {
                    "attachName": "/upload/image/20221008",
                    "channel": "app",
                    "md5": "430A31FCA629E9565AD2A0CACD757733",
                    "newName": "2022100822163053585471.jpeg",
                    "newPathName": "/upload/image/20221008/2022100822163053585471.jpeg",
                    "originalAttachName": "/upload/image/20221008",
                    "originalName": "166528538853127.jpeg",
                    "path": "/upload/image/20221008",
                    "purpose": "scsfz",
                    "size": 6657,
                    "uploadType": "image"
                }],
                "bank": {
                    "idCard": "G28868055658658855"
                },
                "base": {
                    "birthday": "1991-01-01",
                    "childNum": "1",
                    "education": "1",
                    "email": "fhhvhhh@163.com",
                    "familyName": "fifth",
                    "givenName": "gghh",
                    "idCardNum": "G28868055658658855",
                    "instancyContacts": [{
                        "contactName": "13wei(*´I`*)",
                        "contactPhone": "+529212975512",
                        "contactRelation": "0",
                        "contactRealName": "13wei(*´I`*)",
                        "lastTime": 0
                    }, {
                        "contactName": "13wei02(／_＼)大怨种",
                        "contactPhone": "525524064428",
                        "contactRelation": "2",
                        "contactRealName": "13wei02(／_＼)大怨种",
                        "lastTime": 0
                    }],
                    "maritalStatus": "1",
                    "middleName": "gush",
                    "placeAddress": "fghh",
                    "placeCity": "003002",
                    "placeProvince": "003",
                    "placeTime": "",
                    "postalCode": "",
                    "rfc": "",
                    "sex": "1",
                    "sysPlaceAddress": "",
                    "uname": "",
                    "whatsApp": "2158083558"
                },
                "configPayout": "true",
                "customerSource": "com.mx.hinance",
                "firstExpectAmount": "750.00",
                "firstExpectDay": "10",
                "livenessId": "",
                "merchantNo": "01",
                "orgNo": "MEX",
                "payoutPaymentConfig": {
                    "bankConfig": {
                        "accountType": {
                            "label": "银行",
                            "value": "0"
                        },
                        "bankCard": "128095486658866556",
                        "bankType": {
                            "label": "BANCOMEXT",
                            "value": "37006"
                        },
                        "name": "fifth gghh gush"
                    },
                    "paymentChildKey": {
                        "label": "Bank",
                        "value": "bank"
                    },
                    "paymentTypeKey": {
                        "label": "Bank transfer",
                        "value": "bank"
                    }
                },
                "productNo": "MEX_01_1_20220927173142",
                "promotionChannels": "googlePlay",
                "applyLoanAmount": "750.00",
                "sign": {
                    "adbEnabled": 1,
                    "androidId": "4535c1db08e9d00f",
                    "availableStorage": " 16.0653GB",
                    "battery": "71",
                    "codeName": "REL",
                    "cpu": "armeabi-v7a",
                    "cpuInfo": "",
                    "cpuSpeed": "1144000KHz",
                    "currentWifi": "\"HCLOUD-Risk\"",
                    "detailAddress": "",
                    "deviceLanguage": "zh",
                    "deviceMac": "BC:76:5E:8A:0F:91",
                    "deviceModel": "samsung#SM-G610F",
                    "deviceSerial": "3300fbcb8a7783cb",
                    "deviceSoftwareVersion": "01",
                    "deviceVersionType": "user",
                    "displayMetrics": "1080,1920",
                    "fingerPrint": "samsung/on7xeltedd/on7xelte:8.1.0/M1AJQ/G610FDXS1CTE1:user/release-keys",
                    "gaid": "null",
                    "hardware": "samsungexynos7870",
                    "imei": "353415087834233",
                    "imsi": "",
                    "inDoor": -1,
                    "lag": "",
                    "lng": "",
                    "locationAddress": "",
                    "locationCity": "",
                    "mobileName": "Galaxy J7 Prime",
                    "model": "samsung#SM-G610F",
                    "networkOperator": "46000",
                    "networkOperatorName": "",
                    "networkType": "wifi",
                    "operatorName": "",
                    "os": "8.1.0",
                    "phoneAvailableRam": " 0.8086GB",
                    "phoneCardNum": "",
                    "phoneOs": "Android",
                    "phoneTotalRam": "MemTotal:        2882568 kB",
                    "phonecardCount": 0,
                    "product": "on7xeltedd",
                    "radioVersion": "G610FDDS1CTE2",
                    "resolutionHeight": "1920",
                    "resolutionWidth": "1080",
                    "rooted": 0,
                    "routerMac": "3c:cd:5d:11:42:30",
                    "runtimeAvailableMemory": " 0.1715GB",
                    "runtimeMaxMemory": " 0.1875GB",
                    "simState": 0,
                    "simulator": 1,
                    "timeZone": "GMT+08:00",
                    "totalStorage": " 25.3557GB",
                    "turnOnTime": "2022-09-28 10:10:51",
                    "uuid": "53454350484f4e455f3030303030303030303030303030303030313632313535",
                    "uuidOriginal": "[83, 69, 67, 80, 72, 79, 78, 69, 95, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, 48, "
                                    "48, 48, 48, 48, 48, 48, 49, 54, 50, 49, 53, 53] "
                },
                "work": {
                    "income": "3",
                    "payDay": "8",
                    "post": "0",
                    "salaryType": "3",
                    "secondPayDay": "",
                    "sourceIncome": "0",
                    "tel": "",
                    "workTime": "1"
                }
            }
        }

    ]

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化一次 注册登录，写个新的token进配置文件
        login().login()

        cls.header = {
            'app-name': 'Hinance',
            'app-version': '1.0.7',
            'channel': 'googlePlay',
            'commercialId': '1',
            'lang': 'zh',
            'organizationId': 'DCMEX',
            'token': red_(Basfig_path).red_get('token', 'token_'),
            'Content-Type': 'application/json'
        }

    def setUp(self) -> None:
        Log().debug('================================开始================================')

    @data(*AddressBook)
    def test_UploadingAddressBook(self, Book):
        try:
            resp = Request(Book['method'], url_=Book['url'],
                           body_=json.dumps(Book['body']),
                           headers_=self.header,
                           cookies=None).get_json()
            if resp['code'] == 0 and resp['msg'] == '成功':
                Log().debug('\n当前请求接口是: {0},\n请求参数: {1},\n请求结果{2}'.format(Book['title'], Book['body'], resp))
            else:
                Log().debug('当前接口：{0},响应结果{1},错误id：{2}'.format(Book['title'], resp['msg'], resp['traceId']))
                Log().info('当前接口：{0},响应结果{1},错误id：{2}'.format(Book['title'], resp['msg'], resp['traceId']))

            # 接口断言
            self.assertEqual('成功', resp['msg'])

        except Exception as e:
            Log().error("当前请求的错误: {}".format(e))
            raise e

    def tearDown(self) -> None:
        Log().debug('================================结束================================\n')


if __name__ == '__main__':
    unittest.main()
