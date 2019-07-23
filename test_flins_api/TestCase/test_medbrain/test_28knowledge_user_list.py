# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

class knowledge_user_list(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + "/knowledgebase/user/list"
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        r = requests.post(self.url, headers=gloVal.HEADER)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()