# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#文献属性保存(文献详情页)
class know_doc_update(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/doc/update'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
        "title": "fd",
        "childrenClassification": "3,7,6",
        "author": "杨林;吕斌",
        "fund": None,
        "number": "asa",
        "url": "33334353452345",
        "keyword": None,
        "publishedJournals": None,
        "sourceId": 1,
        "sourceUrl": None,
        "publishedTime": 1561602916000,
        "publishedTimeString":  "2020"
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