# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#商户列表
class list(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/list'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    #该接口无参数，只需有效token
    def test01(self):
        r = requests.post(self.url, headers=self.header)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




if __name__ == '__main__':
    unittest.main()