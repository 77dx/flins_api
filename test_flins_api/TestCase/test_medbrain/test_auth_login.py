# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal
from TestCase.test_medbrain import test_auth_captcha


class auth_login(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL
        self.header = gloVal.HEADER



    def test01(self):
        url = self.url + '/auth/login/'
        data = {
            "account": "andyzhang",
            "pwd":"0c8abdb962f042d1857c66dd26b0c87b",
            "captchaToken":"7c77edad75904a2f81c413dd702e4209",
            "captcha":"gny8"
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




    def tearDown(self):
        print('结果是：'+test_auth_captcha.auth_captcha.captchaToken)


if __name__ == '__main__':
    unittest.main()
