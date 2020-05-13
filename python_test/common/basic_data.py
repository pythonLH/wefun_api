import re

class doregex:
    @staticmethod
    def replace(target):
        pattern = '\$\{(.*?)\}'
        while re.search(pattern, target):  # 找到一个就返回match
            m = re.search(pattern, target)
            key = m.group(1)  # invest_user
            user = getattr(Context, key)
            target = re.sub(pattern, user, target, count=1)  # 替换excel中的数据
        return target  # 替换后excel中的数据



class Context:
    join_id = 1188157983847088128




if __name__ == '__main__':
    # setattr(Context,'server_id','1188485874103353344')
    t = getattr(Context,'channel')
    print(t)












