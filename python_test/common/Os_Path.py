import os


# os.path.realpath(__file__) 获取当前操作的文件路径

test_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]


# 配置文件path
conf_dir = os.path.join(test_path + r'\conf') # 放置配置文件的package
snqu_accout = os.path.join(conf_dir + r'\Test_Accout.conf')
test_datas = os.path.join(conf_dir + r'\test.conf')
official_datas = os.path.join(conf_dir + r'\official.conf')
control_datas = os.path.join(conf_dir + r'\control.conf')

# 日志输出文件path
logger_dir = os.path.join(test_path + r'\logger')
logger_error = os.path.join(logger_dir + r'/erro_log/error.txt')
logger_info = os.path.join(logger_dir + r'/info_log/info.txt')


# 测试用例路径
case_dir = os.path.join(test_path + r'\test_detas')
test_case = os.path.join(conf_dir + r'test_case.xlsx')




if __name__ == '__main__':
    '''
    print("配置文件目录路径是%s "%(conf_dir))
    print("盛趣测试账号存放路径%s "%(snqu_accout))
    print("控制环境切换的配置文件路径%s "%(control_datas))
    print("测试环境API数据路径%s "%(test_datas))
    print("正式环境API数据路径%s "%(official_datas))
    '''

    print(logger_dir)
    print(logger_error)
    print(logger_info)
