import unittest
import HTMLTestRunnerNew
from common.ptah_object._path import case_dir,report_html

discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*.py", top_level_dir=None)
with open(report_html, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='进件接口报告')
    runner.run(discover)  # 执行查找到的用例)
