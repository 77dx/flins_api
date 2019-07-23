# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#文献标签保存
class know_label_save(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/label/save'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "name": "你好",
            "fileId": 1
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