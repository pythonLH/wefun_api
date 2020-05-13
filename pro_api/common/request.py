import requests
import json
from common.readconfig import ConfigLoader
class Http_Request():


    def __init__(self, method,url,data=None,cookies=None, headers=None):

        config = ConfigLoader().get('api','test_api')
        url = config + url
        if method == 'get':
            self.resp = requests.get(url=url,params=data,cookies=cookies,headers=headers) # get请求的方式 以params定义参数名
        elif method == 'post':
            self.resp = requests.post(url=url,data=data,cookies=cookies,headers=headers)
        elif method == 'delete':
            self.resp = requests.delete(url=url,data=data,cookies=cookies,headers=headers)

        elif method == 'put':
            self.resp = requests.put(url=url,params=data,cookies=cookies,headers=headers)


    def get_status_code(self):
        return self.resp.status_code

    def get_text(self):
        return self.resp.text

    def get_json(self):
        return self.resp.json()

    def get_cookies(self):
        return self.resp.cookies

    def get_time(self):
        return self.resp.elapsed.microseconds

    def get_url(self):
        return self.resp.url

if __name__ == '__main__':
    url = "/message/stream/procedure/spam"
    header = {"Authorization": "cffc4b45666c4b7f86d75b2bc61eeac7"}
    data = {"pageNumber":1,"pageSize":20,"end_uuid":None,"isWeb":1}
    print(type(data))



    resp = Http_Request('get',url=url,data=data,headers=header)
    reslut_code = resp.get_status_code()
    res = resp.get_json()['data']['landing']
    print(reslut_code,res)
