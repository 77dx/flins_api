# -*- coding:utf-8 -*-

import requests
import unittest
from TestCase.gloVal import gloVal
import json
import hashlib
from TestCase.test_BBOSS.StartEnd import unittest_StartEnd


#登录boss，获取token
class Test_login(unittest_StartEnd):

    #获取验证码token,返回1051是不需要验证码
    def test_01(self):
        url = self.url + '/auth/captcha'
        r = requests.post(url, headers=self.header)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        globals()['code'] = response["code"]
        self.assertEqual("1051", response["code"], msg=response['desc'])

    # 正确的用户名和密码
    def test_02(self):
        if code == "1051":
            url = self.url + '/auth/login'

            # 对密码进行MD5加密
            password = '123456'
            m = hashlib.md5(password.encode())

            data = {
                "account": "jane",
                "pwd": m.hexdigest(),
                "captchaToken":"",
                "captcha": ""
            }
            r = requests.post(url, headers=self.header, data=json.dumps(data))
            body = r.text
            response = json.loads(body)
            #提取token
            gloVal.TOKEN = response["data"]["token"]
            print('接口返回：' + body)
            self.assertEqual("0000", response["code"], msg=response['desc'])


if __name__ == '__main__':
    unittest.main()


