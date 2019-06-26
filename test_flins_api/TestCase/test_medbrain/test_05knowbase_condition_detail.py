# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal


#根据id查询分组详情
class knowbase_condition_detail(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase /conditionalgroup/detail'
        self.header = gloVal.HEADER


    #参数id正确
    def test01(self):
        data = {
            "id": 1
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    #错误的id
    def test02(self):
        data = {
            "id": 000
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])

    #id为空
    def test03(self):
        data = {
            "id": None
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("9999", response["code"], msg=response['desc'])



    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()