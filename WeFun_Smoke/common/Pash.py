# os.path.realpath(__file__) 获取当前操作的文件路径
import os
moke_path =os.path.realpath(__file__)


# 整个项目路径
moke_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]



conf = os.path.join(moke_path + r'\configs\test.conf') # 测试环境不变的数据，配置文件存放路径
token_dir = os.path.join(moke_path + r'\configs\token.conf') # 会变动的token，配置文件存放路径
case_dir = os.path.join(moke_path + r'\case')
reports_dir = os.path.join(moke_path + r'\reports')


reports = os.path.join(moke_path + r'\reports')
result = os.path.join(moke_path , r'D:\WeFun Smoke\reports')
html = os.path.join(result , 'test_runner.html')





if __name__ == '__main__':
    print(moke_path)
    print(moke_path)
    print(token_dir)
    print(case_dir)
    print(reports)
    print(result)
    print(html)