# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json


class statistical(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/qa/statisticsdetail'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "channelCodeMain":"trussan",
            "startSubmitTime":"2018-05-21",
            "endSubmitTime":"2018-05-28",
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