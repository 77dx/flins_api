# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

class list(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/statistical/detail'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        data = {
            "merId": "1",
            "startSubmitTime": "",
            "endSubmitTime": "",
            "currentPage": 1,
            "pageSize": 10
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




if __name__ == '__main__':
    unittest.main()