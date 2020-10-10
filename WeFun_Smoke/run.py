import unittest
import HTMLTestRunnerNew
from common import Pash




discover = unittest.defaultTestLoader.discover(Pash.case_dir, pattern="test*.py", top_level_dir=None)
with open(Pash.html, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='wefun接口测试报告')
    runner.run(discover)   # 执行查找到的用例
