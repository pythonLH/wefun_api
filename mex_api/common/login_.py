import json
import random
from common.request_ import Request
from common.ptah_object._path import Basfig_path
from common.redConfig import red_
from common.logger_ import Log

url = red_(Basfig_path).red_get('register', 'register_url')
register = eval(red_(Basfig_path).red_get('register', 'register_'))
login_url = red_(Basfig_path).red_get('register', 'login_url')
login_ = eval(red_(Basfig_path).red_get('register', 'login_'))
header = eval(red_(Basfig_path).red_get('headers', 'login_header'))


class login(object):

    def __init__(self):
        self.token_ = None
        self.url = url
        self.register = register
        self.header = header

        # 注册,配置文件中手机号，为空就随机
        if self.register['phone'] == '':
            self.register['phone'] = ('0' + ''.join(str(random.choice(range(10))) for _ in range(10)))
            reg_ = Request('post', url_=self.url,
                           body_=json.dumps(self.register),
                           headers_=self.header).get_json()
            if reg_['msg'] == '成功':
                if login_['phone'] == '':
                    login_['phone'] = self.register['phone']
                else:
                    pass
            else:
                Log().error('注册失败,注册调用结果： {}'.format(reg_))
        # 如果不是空就直接登录
        else:
            Request('post', url_=self.url,
                    body_=json.dumps(self.register),
                    headers_=self.header).get_json()

    def login(self):

        login_re = Request('post', url_=login_url,
                           body_=json.dumps(login_),
                           headers_=self.header).get_json()

        if login_re['msg'] == '成功':
            for v in login_re['data'].values():
                self.token_ = v
                red_(Basfig_path).write_data('token', 'token_', self.token_)
        else:
            Log().error('登录失败: %s,token没传入值,当前值为: %s' % (login_re, self.token_))

        return self.token_


if __name__ == '__main__':
    print(login().login())
