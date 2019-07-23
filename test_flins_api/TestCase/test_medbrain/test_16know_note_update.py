# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#修改我的笔记
class know_note_update(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/note/update'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        data = {
            "id": 1,
            "fileId": 1,
            "title": "我的笔记",
            "urls": ["www.qiniu.com","www.qiniu.cn"],
            "content": "cathy的第一个笔记"
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