# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#文献类目修改
class know_doc_update(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/doc/category/update'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        data = {
            "id": 11,
            "childrenClassification":"5,6"
        }
        r = requests.post(self.url, headers=self.header, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])


    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()