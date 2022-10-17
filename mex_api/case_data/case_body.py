# 用户提交借款时，需要传递的参数json
app_list = {
    # appList -->手机上已安装app列表
    "appList": [
        {
            "appName": "生活钱包",  # -->app名称
            "appVersion": "1.0.3",  # -->app版本
            "firstInstallTime": "2022-09-19 16:18:28",  # -->安装时间
            "lastUpdateTime": "2022-09-19 16:18:28",  # -->安装更新时间
            "packageName": "com.life.wallet"  # -->包名
        },
        {
            "appName": "蚂蚁盒子",
            "appVersion": "1.1.0",
            "firstInstallTime": "2022-07-12 16:43:14",
            "lastUpdateTime": "2022-07-12 16:43:14",
            "packageName": "com.vn.antbox"
        },
        {
            "appName": "WPS Office",
            "appVersion": "12.3.1",
            "firstInstallTime": "2020-11-20 19:18:28",
            "lastUpdateTime": "2020-11-20 19:18:28",
            "packageName": "cn.wps.moffice_eng"
        },
        {
            "appName": "Dodo Cash",
            "appVersion": "1.0.0",
            "firstInstallTime": "2022-07-19 16:57:16",
            "lastUpdateTime": "2022-07-19 16:57:16",
            "packageName": "com.dodocash.android"
        }
    ],
    "applyLoanAmount": "1000.00",  # 申请时产品的金额，用于判断用户提交申请后，产品调整额度的情况
    # 附件列表
    "attach": [
        {
            "attachName": "/upload/image/20220919",  # -->附件用户上传的名称
            "channel": "app",  # -->附件上传渠道，app，web
            "md5": "57203D354D9EB3B27F37AB7E42AD9643",
            "newName": "202209192147244175027.jpeg",  # -->附件名称
            "newPathName": "/upload/image/20220919/202209192147244175027.jpeg",  # -->附件访问全路径
            "originalAttachName": "/upload/image/20220919",  # -->附件用户上传的名称
            "originalName": "1663642042276529.jpeg",
            "path": "/upload/image/20220919",  # --附件路径
            "purpose": "sfzzm",
            "size": 14533,  # -->附件大小
            "uploadType": "image"  # --附件格式
        },
        {
            "attachName": "/upload/file/20220919",
            "channel": "app",
            "md5": "7ED63139996F6D07BFEDEC710BBE44B6",
            "newName": "202209192148144366688.jpg",
            "newPathName": "/upload/file/20220919/202209192148144366688.jpg",
            "originalAttachName": "/upload/file/20220919",
            "originalName": "1663642092068advance.jpg",
            "path": "/upload/file/20220919",
            "purpose": "liveness",
            "size": 228014,
            "uploadType": "file"
        }
    ],
    # 传身份证号码
    "bank": {
        "idCard": "D2644544G574676687"  # -->身份证号
    },
    # 借款用户基本信息
    "base": {
        "birthday": "1991-01-01",  # -->出生日期
        "childNum": "0",  # -->子女个数
        "education": "2",  # -->最高学历
        "email": "gfhcbjg@qq.com",
        "familyName": "fhh",  # -->姓
        "givenName": "fch",  # -->名
        "idCardNum": "D2644544G574676687",  # -->身份证号码
        # 紧急联系人集合
        "instancyContacts": [{
            "contactName": "13wei01",
            "contactPhone": "522187858625",
            "contactRelation": "0",  # -->与紧急联系人的关系
            "lastTime": 0
        }, {
            "contactName": "13wei02",
            "contactPhone": "522190858525",
            "contactRelation": "2",  # -->与紧急联系人的关系
            "lastTime": 0
        }],
        "maritalStatus": "1",  # -->婚姻状况
        "middleName": "chb",  # -->第二姓氏
        "placeAddress": "ghhu",  # -->城市社区（居住详细地址）
        "placeCity": "002003",  # -->居住地城市
        "placeProvince": "002",  # -->州、联邦区(居住省)
        "placeTime": "",  # -->居住时长
        "postalCode": "",  # -->邮编
        "rfc": "",  # -->纳税号
        "sex": "1",  # -->性别
        "sysPlaceAddress": "",  # -->系统居住地详细地，由用户选择的州、联邦区+输入城市社区
        "uname": "",  # -->姓名
        "whatsApp": "2806593596"  # -->社交账号WhatsApp
    },
    "configPayout": "true",  # -->是否配置放款方式
    "customerSource": "com.mx.hinance",  # -->客户来源
    "firstExpectAmount": "1000.00",  # -->首次期望借款金额
    "firstExpectDay": "8",  # -->首次期望天数
    "livenessId": "bf496efd-0819-404e-8772-22df69d5a168",  # -->活体验证编号，后台可通过该编号获取活体检测分数
    "merchantNo": "01",  # -->商户编号,贷超传
    "orgNo": "MEX",  # -->机构编号，贷超传
    # AppPayoutPaymentConfigDto对象
    "payoutPaymentConfig": {
        "bankConfig": {
            # SystemCodeField对象
            "accountType": {
                "label": "银行",  # 码表对应的code_value，根据不同语言设置不同码表国际化字段,如：1个月，3-6个月，6-12个月，12个月以上
                "value": "0"  # 码表的对应的code_key，通常是一些码表固定的状态，如0,1,2,3
            },
            "bankCard": "132509588658565963",  # -->银行卡号
            "bankType": {
                "label": "BANCOMEXT",  # 码表对应的code_value，根据不同语言设置不同码表国际化字段,如：1个月，3-6个月，6-12个月，12个月以上
                "value": "37006"  # 码表的对应的code_key，通常是一些码表固定的状态，如0,1,2,3
            },
            "name": "fhh fch chb"  # 户主姓名
        },
        "paymentChildKey": {
            "label": "Bank",  # 码表对应的code_value，根据不同语言设置不同码表国际化字段,如：1个月，3-6个月，6-12个月，12个月以上
            "value": "bank"  # 码表的对应的code_key，通常是一些码表固定的状态，如0,1,2,3
        },
        "paymentTypeKey": {
            "label": "Bank transfer",  # 码表对应的code_value，根据不同语言设置不同码表国际化字段,如：1个月，3-6个月，6-12个月，12个月以上
            "value": "bank"  # 码表的对应的code_key，通常是一些码表固定的状态，如0,1,2,3
        }
    },
    "productNo": "MEX_01_1_20220617173142",  # 所选产品编号
    "promotionChannels": "googlePlay",  # 推广渠道
    # 借款用户使用的手机信息
    "sign": {
        "adbEnabled": 0,  # 是否usb调试已打开
        "androidId": "1f87332bd0b96267",  # android编号
        "availableStorage": " 9.0537GB",  # 设备可用存储
        "battery": "100",  # 电量百分比
        "codeName": "REL",  # 设备当前的系统开发代号，一般使用REL代替
        "cpu": "armeabi-v7a",  # 获取设备指令集名称
        "cpuInfo": " MT6762G",  # cpu的信息
        "cpuSpeed": "1218000KHz",  # cpuSpeed主频
        "currentWifi": "\"HAI-IT\"",  # 所连接的WIFI的名称
        "detailAddress": "",  # 定位的详细地址
        "deviceLanguage": "zh",  # 语言
        "deviceMac": "94:17:00:7F:C7:F7",  # 注册时设备mac地址
        "deviceModel": "Xiaomi#M2006C3LG",
        "deviceSerial": "",  # 序列号
        "deviceSoftwareVersion": "78",  # 设备的软件版本号：返回移动终端的软件版本
        "deviceVersionType": "user",  # 版本类型user,eng
        "displayMetrics": "720,1449",  # 屏幕解析率
        "fingerPrint": "Redmi/dandelion_global/dandelion:10/QP1A.190711.020/V12.0.20.0.QCDMIXM:user/release-keys",
        # 出厂签名
        "gaid": "0c6b61b6-4604-422b-b264-121365738fea",  # google Ad ID
        "hardware": "mt6762",  # 设备硬件名称,一般和基板名称一样
        "imei": "",  # 安卓imei
        "imsi": "",  # 安装imsi
        "inDoor": -1,  # 是否在室内
        "lag": "",  # 纬度
        "lng": "",  # 经度
        "locationAddress": "",  # 定位的地理位置信息
        "locationCity": "",  # 定位的城市
        "mobileName": "Redmi 9A",  # 手机名称.蓝牙名称
        "model": "Xiaomi#M2006C3LG",  # 设备型号
        "networkOperator": "",  # 运营商，可能获取不到
        "networkOperatorName": "",  # 运营商名称，可能获取不到
        "networkType": "wifi",  # 网络类型
        "operatorName": "无服务,只能拨打紧急呼救电话",
        "os": "10",  # 操作系统
        "phoneAvailableRam": " 0.6012GB",  # 手机可用内存
        "phoneCardNum": "",
        "phoneOs": "Android",  # Android/IOS
        "phoneTotalRam": "MemTotal:        1819908 kB",  # 总内存大小
        "phonecardCount": 2,
        "product": "dandelion_global",  # 整个产品的名称
        "radioVersion": "MOLY.LR12A.R3.MP.V107.5.P125,MOLY.LR12A.R3.MP.V107.5.P125",  # 无线电固件版本号
        "resolutionHeight": "1449",  # 分辨率高度
        "resolutionWidth": "720",  # 分辨率宽度
        "rooted": 0,  # 是否被root
        "routerMac": "f4:a4:d6:56:f9:90",  # 路由器mac地址
        "runtimeAvailableMemory": " 0.2306GB",  # apk 可用内存大小
        "runtimeMaxMemory": " 0.2500GB",  # apk可分配的最大内存
        "simState": 1,  # 1代表未插卡
        "simulator": 0,  # 是否模拟器
        "timeZone": "GMT+08:00",  # 时区
        "totalStorage": " 22.6777GB",  # 设备总存储
        "turnOnTime": "2022-09-18 20:40:20",
        "uuid": "fa8e6c6474520d515b29198bb083a8014c47c44e15efd159358a4ce824c27573",  # 设备id，可能获取不到
        "uuidOriginal": "[-6, -114, 108, 100, 116, 82, 13, 81, 91, 41, 25, -117, -80, -125, -88, 1, 76, 71, -60, 78, "
                        "21, -17, -47, 89, 53, -118, 76, -24, 36, -62, 117, 115] "  # 设备id原始字符串
    },
    # 借款用户工作信息借款用户工作信息
    "work": {
        "income": "2",  # 工作收入
        "payDay": "8",  # 发薪日
        "post": "0",  # 公司职位
        "salaryType": "3",  # 薪水类型
        "secondPayDay": "",  # 第二发薪日
        "sourceIncome": "0",  # 收入来源
        "tel": "",
        "workTime": "1"  # 工作时长
    }
}
print(id(app_list))
x = 10  # 直接引用
list_ = ["a", "b", x]  # 间接引用
x = 5
print(list_[2])
print(x)

b = 10
del (b) # 解除引用
print(b)
