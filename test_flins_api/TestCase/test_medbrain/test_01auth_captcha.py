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


    #参数是token
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


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
