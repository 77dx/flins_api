# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal



class auth_login(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL
        self.header = gloVal.HEADER

    #正确的用户名密码,无须验证码
    def test01(self):
        url = self.url + '/auth/login'
        data = {
            "account": "admin",
            "pwd":"0c8abdb962f042d1857c66dd26b0c87b",
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    #用户名和密码为空
    def test02(self):
        url = self.url + '/auth/login/'
        data = {
            "account": "",
            "pwd":""
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])


    #用户名不为空，密码为空
    def test03(self):
        url = self.url + '/auth/login/'
        data = {
            "account": "admin",
            "pwd":""
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])


    #用户名为空，密码不为空
    def test04(self):
        url = self.url + '/auth/login/'
        data = {
            "account": "",
            "pwd":"0c8abdb962f042d1857c66dd26b0c87b"
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])


    #用户名错误
    def test05(self):
        url = self.url + '/auth/login/'
        data = {
            "account": "xxs",
            "pwd":"0c8abdb962f042d1857c66dd26b0c87b"
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])


    #用户名正确，密码错误
    def test06(self):
        url = self.url + '/auth/login'
        data = {
            "account": "admin",
            "pwd":"0c8abdb962f042d1857c66dd26b0c87b"
        }
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])





    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
