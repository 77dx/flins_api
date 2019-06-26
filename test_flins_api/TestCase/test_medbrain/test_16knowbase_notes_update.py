# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#修改我的笔记
class knowbase_notes_update(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/notes/update'


    def test01(self):
        data = {
            "id": 1,
            "literatureId": 1,
            "title": "我的笔记",
            "urls": ["www.qiniu.com","www.qiniu.cn"],
            "content": "我的笔记.XXXXXXXXX",
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