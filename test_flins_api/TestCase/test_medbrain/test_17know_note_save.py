# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#保存我的笔记
class know_note_save(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/note/save'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "fileId": 1,
            "title": "我的笔记",
            "urls": ["www.qiniu.com","www.qiniu.cn"],
            "content": "保存我的笔记"
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