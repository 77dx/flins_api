# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

class know_doc_upload(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/doc/upload'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        data = {
            "title": "fd1",
            "bigClassification": 1,
            "childrenClassification": "5,6",
            "author": "杨林",
            "url": "33334353452345",
            "keyword": "哈哈",
            "publishedJournals": "sss",
            "sourceId": 1,
            "publishedTimeString": "2018"
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