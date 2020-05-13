import logging
from common.os_path import logs_file,logs_file_error

my_logger = logging.getLogger('测试日志收集')
my_logger.setLevel('DEBUG')

formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(lineno)s-%(message)s')

# 输出到控制台
console = logging.StreamHandler()
console.setLevel('DEBUG')
console.setFormatter(formatter)

# 输出到指定文件
file = logging.FileHandler(filename=logs_file,encoding='utf-8')
file.setLevel('INFO')
file.setFormatter(formatter)

# error信息输出至文件
error = logging.FileHandler(filename=logs_file_error,encoding='utf-8')
error.setLevel('ERROR')
error.setFormatter(formatter)

# 添加输出渠道到日志收集器里
my_logger.addHandler(console)
my_logger.addHandler(file)
my_logger.addHandler(error)


if __name__ == '__main__':
    my_logger.debug('你是个debug信息')
    my_logger.info('你是info信息')
    my_logger.error('你是error信息')