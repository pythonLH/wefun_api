import requests
import json
from common.Read_Config import Read_Config


class Http_Request:

    def __init__(self,method,url,data,header,cookie=None):
        config = Read_Config().get("V6API","url")
        url = config + url

        if method == 'post':
            self.resp = requests.post(url=url,data=data,headers=header,cookies=cookie)

        elif method == 'get':
            self.resp = requests.get(url=url,params=data,headers=header,cookies=cookie)

        elif method == 'put':
            self.resp = requests.put(url=url,data=data,headers=header,cookies=cookie)

        elif method == 'delete':
            self.resp = requests.delete(url=url,data=data,headers=header,cookies=cookie)

    def get_stutas_code(self):
        # 获取响应状态码
        return self.resp.status_code

    def get_json(self):
        # 获取响应的json报文
        return self.resp.json()

    def get_text(self):
        # 获取响应的详细信息
        return self.resp.text
    def get_cookie(self):
        # 获取响应的cookies
        return  self.resp.cookies
    def elapsed(self):
        # 获取接口响应总耗时数，单位是"秒"
        return self.resp.elapsed.total_seconds()

    def get_header(self):
        # 获取接口响应头部信息
        return self.resp.headers

    def get_history(self):
        return self.resp.history

if __name__ == '__main__':
    url = "https://test-api.wefunapps.com/v1/channels/message-post"
    data = {"channel_id":"1211989264531718144","content":"海关监管","nonce":"1582788718501"}
    header = {"Content-Type":"application/x-www-form-urlencoded","Auth-Token":"MTIxMjM1MzM4MTU3MDQ0NTMxMg.MQ.tE8i5bvMGDPsxJkTGQG3PiYg8LUUnt3MWF5WmdCUuY0"}

    res = Http_Request('post',url=url,data=json.dumps(data),header=header,cookie=None)
    result = res.get_stutas_code()
    print(result)