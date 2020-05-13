import logging
from common import Os_Path

class My_Logger:

    def __init__(self):
        # 定义自己的日志收集器
        self.my_logger = logging.getLogger('test_logger')
        self.my_logger.setLevel('DEBUG')
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')


    def console(self,level,message):

        # 输出到控制台
        consle = logging.StreamHandler()
        consle.setLevel('DEBUG')
        consle.setFormatter(self.formatter)
        self.my_logger.addHandler(consle)


        # info信息输出到指定文件
        info_logger = logging.FileHandler(filename='D:\python_test\logger\info_log\info.txt',encoding='utf-8')
        info_logger.setLevel('INFO')
        info_logger.setFormatter(self.formatter)
        self.my_logger.addHandler(info_logger)

        # error信息输出到指定文件
        error_logger = logging.FileHandler(filename='D:\python_test\logger\error_log\error.txt',encoding='utf-8')
        error_logger.setLevel('ERROR')
        error_logger.setFormatter(self.formatter)
        self.my_logger.addHandler(error_logger)


        if level == 'DEBUG':
            self.my_logger.debug(message)

        elif level == 'INFO':
            self.my_logger.info(message)

        elif level == 'WARNING':
            self.my_logger.warning(message)

        elif level == 'ERROR':
            self.my_logger.error(message)

        # 去重
        self.my_logger.removeHandler(consle)
        self.my_logger.removeHandler(error_logger)
        self.my_logger.removeHandler(info_logger)


    def debug(self,message):
        self.console('DEBUG',message)

    def info(self,message):
        self.console('INFO',message)

    def warning(self,message):
        self.console('WARNING',message)

    def error(self,message):
        self.console('ERROR',message)

if __name__ == '__main__':
    t = My_Logger()
    t.error('出错啦')
    t.info('搓出啦')
    t.debug('lall')

