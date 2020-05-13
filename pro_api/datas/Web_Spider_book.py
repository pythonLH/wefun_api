import requests,sys
from bs4 import BeautifulSoup



class downloader:

    def __init__(self):
        self.server = 'http://www.shuhai.com/read/46018/'
        self.target = 'http://www.shuhai.com/read/46018/'
        self.names = [] # 章节名
        self.urls = [] #存放章节链接
        self.nums = 0 #章节数


    def get_download_url(self):
        req = requests.get(url = self.target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html,"html.parser")
        texts = bf.findAll('ul', {'class': 'f_gray3'})
        a_bf = BeautifulSoup(str(texts[3]))
        a = a_bf.find_all('a')
        self.nums = len(a[1:])
        for i in a[1:]:
            self.names.append(i.string)
            self.urls.append(self.server + i.get('href'))

    def get_contents(self,target):
        req = requests.get(url=target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        texts = bf.findAll('div', {'class': 'chapter-item'})
        texts = texts[0].text.replace('\xa0'*1,'\n\n')
        return texts


    def writer(self,name,path,text):
        write_flag = True
        with open(path,'a',encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    # print(dl.names)
    # print(dl.urls)
    print("《天火丹帝》开始下载: ")
    for i in range(dl.nums):
        dl.writer(dl.names[i],'《天火丹帝》.txt',dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / dl.nums) + '\r')
        sys.stdout.flush()
    print('《天火丹帝》下载完成')
