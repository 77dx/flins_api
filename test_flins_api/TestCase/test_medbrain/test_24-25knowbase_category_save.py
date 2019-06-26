# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#子类目录新增
class knowbase_category_save(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/category/sava'

    #新增子目录
    def test01(self):
        data = {
            "name": "血液分析",
            "parentId": 1
        }
        r = requests.post(self.url, headers=gloVal.HEADER, data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    #修改子目录
    def test02(self):
        data = {
            "id": 6,
            "name": "血液检查"
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