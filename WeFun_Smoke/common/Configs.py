import configparser
from common import Pash


conf_dir =Pash.conf
token_dir = Pash.token_dir


class read_config:

    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(token_dir,encoding='utf-8')


    def get(self,section,option):
        return self.conf.get( section, option)

    def boolen(self,section,option):
        return self.conf.getboolean( section, option)

    def float(self,section,option):
        return self.conf.getfloat( section, option)

    def int(self,section,option):
        return self.conf.getint( section, option)




if __name__ == '__main__':
    # conf = configparser.ConfigParser()
    # conf.read(Pash.conf,encoding='utf-8')
    # re = conf.get("Headers","header")
    #
    #
    # r = read_config().get("Headers","header")
    # print(r)
    pass