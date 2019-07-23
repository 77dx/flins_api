# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#子类目录删除
class know_category_delete(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/category/delete'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}

    def test01(self):
        data = {
            "id":6
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