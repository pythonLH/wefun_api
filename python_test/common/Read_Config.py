import os
import configparser
from common import Os_Path

# conf_dir = r'D:\python_test\conf\test.conf'
# con = configparser.ConfigParser()
# con.read(conf_dir,encoding='utf-8')
# print(con.get('mysql','user_mysql'))


swich_dir = Os_Path.control_datas

class Read_Config:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read(swich_dir,encoding='utf-8')

        if self.conf.getboolean('switch','off'): # 如果控制conf中的值是True，读取测试环境的配置文件
            test_conf = Os_Path.test_datas
            self.conf.read(test_conf,encoding='utf-8')

        else: # 读取正式环境的配置文件
            official_conf = Os_Path.official_datas
            self.conf.read(official_conf,encoding='utf-8')




    def get(self,section,option):
        return self.conf.get(section,option)

    def get_boolean(self,section,option):
        return self.conf.getboolean(section,option)

    def get_float(self,section,option):
        return self.conf.getfloat(section,option)

    def get_int(self,section,option):
        return self.conf.getint(section,option)

    def set(self,section,option,value):
        return self.conf.add_section(section,option,value)

if __name__ == '__main__':

    result = Read_Config().get('V6API','url')
    result2 = Read_Config().get('Headers','header')
    # print(result,type(result))
    # print(result2,type(result2))
    # Read_Config().set("Headers","channel_id","211.82.96.1")
    # with open(Os_Path.test_datas, 'w') as fw:
    #     conf.write(fw)
    # res = Read_Config().get('Headers','channel_id')
    # print(res)



    # 读取盛趣账号
    accout_dir = Os_Path.snqu_accout
    con = configparser.ConfigParser()
    con.read(accout_dir,encoding='utf-8')

    for i in con.items('shared_disk'):
        for j in i:
            print((j),'',end='')
