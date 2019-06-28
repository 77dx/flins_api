# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#查询笔记列表
class knowbase_note_list(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/note/list'


    def test01(self):
        data = {
            "id": 12,
            "isOwner": True,
            "page": {
                    "currentPage":1,
                    "pageSize":10
            }
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