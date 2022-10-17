import os

item_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# if not os.path.exists(item_dir + r'\config'):
#     os.mkdir(item_dir + r'\config')
#     if os.path.exists(item_dir + r'\config'):
#         print("创建路径成功")
#         conf_ = item_dir + r'\config'
#         file_name = conf_ + r'\BasicConfigUration.ini'
#         with open(file_name, 'w') as f:
#             print("创建完配置文件，需要写配置信息，没空做！")
# else:
#     pass


# 根路径路径
_dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# 测试文件
case_dir = _dir + r'\case'
# 测试报告路径:
report_dir = _dir + r'\repos'
report_html = report_dir + r'Into_an_interface.html'
# 配置文件路径
Basfig_path = item_dir + r'\config\BasicConfigUration.ini'
print(Basfig_path)