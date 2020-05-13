import requests


class Http:
    def __init__(self,method,url,data,header,cookie):

        if method == 'get':
            self.res = requests.get(url=url,data=data,headers=header,cookies=cookie)

        elif method == 'post':
            self.res = requests.post(url=url,data=data,headers=header,cookies=cookie)

    def get_code(self):
        return  self.res.status_code

    def gte_json(self):
        return self.res.json()



if __name__ == '__main__':
    url = "https://test-api.wefunapps.com/v1/channels/message-post"
    data = {"channel_id":"1211989264531718144","content":"海关监管","nonce":"1582788718501"}
    header = {"Content-Type":"application/x-www-form-urlencoded","Auth-Token":"MTIxMTk4NzE0ODQ0NjYyOTg4OA.MQ.Mz8vrn0XRxmE3ifKiQAEx6pe6Yu9OeJPGstxpAbmzuM"}
    r = Http('post',url=url,data=data,header=header,cookie=None)
    print(r.get_code())
    print(r.gte_json())