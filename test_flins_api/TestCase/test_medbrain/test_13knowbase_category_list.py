# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#文献类目
class knowbase_category_list(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/category/list'
        self.header = gloVal.HEADER


    def test01(self):
        data = {
            "id": 12
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