# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

class Test_list3(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/statistical/detail'
        self.header = {'content-type': 'application/json', 'token': gloVal.BOSS_TOKEN}

    def test01(self):
        data = {
            "merId": 12,
            "startSubmitTime": "",   #2019-07-01
            "endSubmitTime": "",     #2019-07-31
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