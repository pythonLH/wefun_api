import requests
import json
from common.logger_ import Log
from common.ptah_object._path import Basfig_path
from common.redConfig import red_
"""Requests封装类
实现只需调用一个方法，来支持完成多种请求方式（get,post,delete....）的请求"""


class Request:
    def __init__(self, method, url_, body_, cookies=None, headers_=None):

        self.url = red_(Basfig_path).red_get('host_ip', 'url_176')  # 接口前段部分，直接读配置文件

        try:  # 异常处理

            if method == 'get':
                self.resp = requests.get(url=self.url + url_, params=body_, cookies=cookies, headers=headers_)
            elif method == 'post':
                self.resp = requests.post(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)
            elif method == 'put':
                self.resp = requests.put(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)
            elif method == 'head':
                self.resp = requests.head(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)
            elif method == 'delete':
                self.resp = requests.delete(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)
            elif method == 'options':
                self.resp = requests.options(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)
            elif method == 'patch':
                self.resp = requests.patch(url=self.url + url_, data=body_, cookies=cookies, headers=headers_)

        except Exception as e:
            Log().error("请求错误:{}".format(e))
            raise e

    def get_status_code(self):  # 返回响应码
        return self.resp.status_code

    def get_text(self):  # 返回str类型的响应体
        return self.resp.text

    def get_json(self):  # 返回dict类型的响应体
        return self.resp.json()

    def get_cookies(self, key=None):  # 返回cookies
        print(self.resp.cookies)
        if key is not None:
            return self.resp.cookies[key]
        else:  # key=None，返回整个cookies对象
            return self.resp.cookies


if __name__ == '__main__':
    url = "/hc/app/noAuth/logon/doRegister"
    data = {
        "promotionChannels": "googlePlay",
        "password": "",
        "flag": "01",
        "phone": "2221593587",
        "countryCode": "52",
        "shortNo": "9999"
    }

    headers = {
        'app-name': 'Hinance',
        'app-version': '1.0.7',
        'channel': 'googlePlay',
        'commercialId': "1",
        'lang': 'zh',
        'organizationId': 'DCMEX',
        'token': '',
        'Content-Type': 'application/json'
    }
    t = Request('post', url_=url, body_=json.dumps(data), headers_=headers, cookies=None)
    print(t.get_json())
