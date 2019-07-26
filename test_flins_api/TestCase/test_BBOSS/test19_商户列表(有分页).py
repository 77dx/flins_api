# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json


class pfipadd(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/mer/pagelist'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "page": {
                    "currentPage":1,
                    "pageSize":10
            }
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print(self.url)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()