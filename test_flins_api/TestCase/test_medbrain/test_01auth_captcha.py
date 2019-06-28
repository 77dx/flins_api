# -*- coding:utf-8 -*-

import requests
import unittest
from TestCase.gloVal import gloVal
import json

#登录知识库，获取验证码
class auth_captcha(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL
        self.header = gloVal.HEADER


    #获取验证码token
    def test01(self):
        url = self.url + '/auth/captcha'
        data = {"token":"7c77edad75904a2f81c413dd702e4209"}
        r = requests.post(url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        #提取出来验证码token
        captchaToken = response["data"]["captchaToken"]
        gloVal.captchaToken = captchaToken
        self.assertEqual("0000", response["code"], msg=response['desc'])

    # 正确的用户名和密码，需要验证码
    def test02(self):
        url = self.url + '/auth/login'
        data = {
            "account": "cathy",
            "pwd": "0c8abdb962f042d1857c66dd26b0c87b",
            "captchaToken": gloVal.captchaToken,
            "captcha": "gny8"
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
