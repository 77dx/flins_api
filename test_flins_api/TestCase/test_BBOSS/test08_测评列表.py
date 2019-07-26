# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json



class statistical(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/ev/list'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "serialNumber": "ER20181123000053",
            "bzId":"IrAmYuqvEZ",
            "merId": 1,
            "startSubmitTime":"",
            "endSubmitTime":"",
            "page": {
                "currentPage":1,
                "pageSize":10
            }
        }
        r = requests.post(self.url, headers=self.header,data=data)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()