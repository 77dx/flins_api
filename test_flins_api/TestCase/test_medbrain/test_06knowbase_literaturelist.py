# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#文献列表
class knowbase_literaturelist(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase /literaturelist'
        self.header = gloVal.HEADER

    #order=1：上传时间
    def test01(self):
        data = {
            "keyword": "jws154154",
            "orderType":1,
            "childrenlClassification":1,
            "page": {
                    "currentPage":1,
                    "pageSize":10
            }
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    # order=2：修改时间
    def test02(self):
        data = {
            "keyword": "jws154154",
            "orderType": 2,
            "childrenlClassification": 1,
            "page": {
                "currentPage": 1,
                "pageSize": 10
            }
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    # order=3：浏览次数
    def test03(self):
        data = {
            "keyword": "jws154154",
            "orderType": 3,
            "childrenlClassification": 1,
            "page": {
                "currentPage": 1,
                "pageSize": 10
            }
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()