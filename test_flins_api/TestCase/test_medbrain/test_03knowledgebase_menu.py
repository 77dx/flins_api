# -*- coding:utf-8 -*-
import requests
import unittest
import json
from TestCase.gloVal import gloVal

#菜单查询
class knowledgebase_menu(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/menu'
        self.header = gloVal.HEADER

    #rootid参数正确
    def test01(self):
        data = {
            "rootId":1
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    #参数为空
    def test02(self):
        data = {
            "rootId":None
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])

    #参数错误
    def test03(self):
        data = {
            "rootId":99
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])


    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()