import time
import random
class Random:
    def __init__(self):
        self.xs =  ["yexin_",
                    "Tom_",
                    "Mary_",
                    "Crazy_",
                    "Python_",
                    "Java_",
                    "C++_",
                    "Database_",
                    "HUST_",
                    "Nehru_",
                    "Walter_",
                    "Keynv_",
                    "Calista_",
                    "Rebecca_",
                    "Xiongsongshu_",
                    "Wuhan_",
                    "Sahnghai_",
                    "Beijing_"]
        self.mz = ["默然",
                   "旅人",
                   "多余",
                   "云中",
                   "残雪",
                   "末世",
                   "桑榆",
                   "扉匣",
                   "木槿",
                   "空城",
                   "相爱",
                   "不扰",
                   "温情",
                   "谁忆",
                   "冰心",
                   "岛屿",
                   "非晚",
                   "与桔",
                   "暖夏",
                   "旧梦"]
    # 随机名字
    def create_name(self):
        sj = time.strftime('%S', time.localtime(time.time())) # 获取当前时间秒
        name = random.choice(self.xs) + random.choice(self.mz) + sj
        return name
    # 随机号码
    def create_phone(self):
        # 第二位数字
        second = [3, 4, 5, 7, 8][random.randint(0, 4)]
        # 第三位数字
        third = {
            3: random.randint(0, 9),
            4: [5, 7, 9][random.randint(0, 2)],
            5: [i for i in range(10) if i != 4][random.randint(0, 8)],
            7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
            8: random.randint(0, 9),
        }[second]
        # 最后八位数字
        suffix = random.randint(9999999, 100000000)
        # 拼接手机号
        return "1{}{}{}".format(second, third, suffix)

if __name__ == '__main__':
    t = Random().create_name()
    b = Random().create_phone()
    print(b)
