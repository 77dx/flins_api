# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json



class Test_statistical6(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/ev/list'
        self.header = {'content-type': 'application/json', 'token': gloVal.BOSS_TOKEN}


    def test01(self):
        data = {
            "serialNumber": "PFC20190715000080",
            "bzId":"m7dKiS0c0q",
            "merId": 1,
            "startSubmitTime":"2019-07-01",
            "endSubmitTime":"2019-07-31",
            "page": {
                "currentPage":1,
                "pageSize":10
            }
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