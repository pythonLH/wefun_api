import requests
import json



class Request():

    def __init__(self, method, url, data, header, cookie=None,verify=False):

        if method == 'get':
            self.result = requests.get(url=url,params=data,headers=header,cookies=cookie)

        elif method == 'post':
            self.result = requests.post(url=url, data=data, headers=header,cookies=cookie)

        elif method == 'put':
            self.result =requests.put(url=url,data=data,headers=header,cookies=cookie)


    def get_code(self):
        return  self.result.status_code
    def get_text(self):
        return self.result.text
    def get_json(self):
        return self.result.json()
    def get_cookie(self):
        return self.result.cookies
    def get_header(self):
        return self.result.headers

# class Re:
#
#
#     def get(self,url,data,header):
#         self.result = requests.get(url=url,params=data,headers=header)
#         return self.result
#
#     def post(self,url,data,header):
#         result = requests.post(url,data,header)
#         return result


if __name__ == '__main__':
    url = 'https://test-api.wefunapp.cn/verify-code/send'
    he = {"Content-Type":"application/json;charset=UTF-8"}
    data = {
        "telephone":"18888888888",
        "scenario":"login-dynamic-code"}

    # print(type(data))
    # re = requests.post(url=url,json=data,headers=he)
    # print(re.status_code)
    # print(re.json())
    # print("这是头",re.headers)
    #
    # re = Request('post',url=url,data=data,header=he)
    # result = re.get_json()
    # print(result['message'])
    re = Request('post',url=url,data=json.dumps(data),header=he,verify=False)
    print(re.get_json())
    print(re.get_cookie())