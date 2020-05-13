import configparser

from common.os_path import conf_dir


class ConfigLoader:

    def __init__(self):
        self.conf =configparser.ConfigParser() # 实例化配置文件读取方法
        self.read_conf = self.conf.read(conf_dir,encoding='utf-8') # 加载配置文件

    def get(self,section,option):
        return self.conf.get(section,option)

    def getboolean(self,section,option):
        return self.conf.getboolean(section,option)

    def getfloat(self,section,option):
        return self.conf.getfloat(section,option)

    def getint(self,section,option):
        return self.conf.getint(section,option)
if __name__ == '__main__':
    t = ConfigLoader().get('header','header_value')
    print(t)


