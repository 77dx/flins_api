# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json


class Test_pfipadd(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/mer/key/add'
        self.header = {'content-type': 'application/json', 'token': gloVal.BOSS_TOKEN}


    def test01(self):
        data = {
            "merId": 11,
            "secretKey": "secretKeysecretKeysecretKey",
            "expireTime": "2099-01-01",
            "status": 1
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("1007", response["code"], msg=response['desc'])




    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()