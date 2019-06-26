# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#我的分组查询
class knowbase_condition_list(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase /conditionalgroup/list'
        self.header = gloVal.HEADER
        self.header_invalid = gloVal.HEADER_INVALID

    #token有效
    def test01(self):
        r = requests.post(self.url, headers=self.header)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    #token失效
    def test02(self):
        r = requests.post(self.url, headers=self.header_invalid)
        body = r.text
        response = json.loads(body)
        print('接口返回：' + body)
        self.assertEqual("1001", response["code"], msg=response['desc'])




    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()