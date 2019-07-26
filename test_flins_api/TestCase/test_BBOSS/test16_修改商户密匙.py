# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json


class pfkeyupdate(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/mer/key/update'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "id":"1",
            "expireTime":"2019-08-21",
            "status":"1"
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()