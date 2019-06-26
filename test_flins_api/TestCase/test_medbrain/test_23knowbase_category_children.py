# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#查询子类目录
class knowbase_categoty_children(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/category/childrens'

    def test01(self):
        data = {
            "parentId": 12
        }
        r = requests.post(self.url, headers=gloVal.HEADER, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
