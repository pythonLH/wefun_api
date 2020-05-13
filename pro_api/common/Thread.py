import requests
import datetime
import threading


class http_post():


    def Requests(self,url,data,header=None):
        rsp = requests.post(url=url,params=data,headers= header)
        return rsp


    def login_get(self,url,data,header):
        print("开始:{0}".format(datetime.datetime.now()))
        result = http_post().Requests(url,data,header)
        print("结束:{0}响应时间: {1}".format(result.status_code, datetime.datetime.now()))



if __name__ == '__main__':

    k = 0
    while True:
        url = "https://www.jianshipro.cn/api/v1/message/messages/comment"
        data = {
    "activity_uuid":"e9801c92e4814bdc9548189fff409266",
    "parent_uuid":"caa75977928648f086e5c8388942f30f",
    "master_uuid":"0c7e6113331d45b79671b4bcc2780fee",
    "content":"通过接口发布带图评论",
    "sync_type":"0",
    "status":"",
    "url":"http://img95.699pic.com/photo/50062/8783.jpg_wh860.jpg"
}
        header = {"Authorization":"eb976932dab440aaa9aa82024451ecfb"}
        threads = []

        i = 0
        number = 10
        print("程序开始{}".format(datetime.datetime.now()))
        for i in range(0,number):
            t  = threading.Thread(target=http_post().login_get,args=(url,data,header))
            t.setDaemon(True)
            t.start()
            threads.append(t)

        # 等待线程运行完毕
        for t in threads:
            t.join()
        k+=1

        if k == 1:
            break