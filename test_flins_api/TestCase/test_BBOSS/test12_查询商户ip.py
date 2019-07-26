# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json


class pfiplist(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/mer/ip/list'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "merId": 10
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