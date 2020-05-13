import unittest
import os
import sys
import HTMLTestRunnerNew
from common import os_path

# dir = os.path.dirname(sys.executable)  找出python 安装路径
 print(reslut_html)

discover = unittest.defaultTestLoader.discover(os_path.quanzi_test_dir,pattern="web_*.py",top_level_dir=None)

with open(os_path.reslut_html,'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,title='pro_API',description="见识接口测试报告",tester="test_liu")


    runner.run(discover)

