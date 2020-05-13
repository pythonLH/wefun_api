import os
import sys


item_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0] # 项目路径
case_dir =os.path.join(item_dir,r'datas\pro_case.xlsx') # 测试用例的路径
web_case_dir = os.path.join(item_dir,r'datas\web_pro_case.xlsx') # web端接口测试用例路径
QuanZi_case_dir = os.path.join(item_dir,r'datas\web_QuanZi_case.xlsx') # 圈子测试用例路径
conf_dir = os.path.join(item_dir,r'conf\oline.conf') # 配置文件的路径




logs_dir = os.path.join(item_dir,'logs') # logs 文件路径
logs_file = os.path.join(logs_dir,'logger_info.txt')
logs_file_error = os.path.join(logs_dir,'logger_error.txt')


testcase_dir = os.path.join(item_dir,r'testcase') # 测试脚本路径

web_test_dir = os.path.join(item_dir,r'web_test_case') # web端测试脚本路径

quanzi_test_dir = os.path.join(item_dir,'web_QuanZi_case') # 圈子测试脚本路径



reslut_dir = os.path.join(item_dir,'repots')
reslut_html = os.path.join(reslut_dir,'test_reslut.html')
Quanzi_html = os.path.join(reslut_dir,'quan_zi.html')
web_test_html = os.path.join(reslut_dir,'web_test_reslut.html')

web_reslut_html = os.path.join(reslut_dir,'web_test_reslut.html')

if __name__ == '__main__':
    pass
    print("项目路径:",item_dir)
    # # print("测试用例路径:",case_dir)
    # print("配置文件的路径:",conf_dir)
    # print("logs输出路径:",logs_file)
    # print("case路径:{}".format(testcase_dir))
    # print(web_case_dir)
    # print(sys.path)
    print(quanzi_test_dir) # 圈子接口脚本路径