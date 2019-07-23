# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

#我的分组查询条件保存
class knowbase_condition_save(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/conditionalgroupsava'
        self.header = {'content-type': 'application/json', 'token': gloVal.TOKEN}


    def test01(self):
        data = {
            "bigClassification": 3,
            "childrenlClassification":"7,8",
            "uploader": 1,
            "title": "甲状腺死亡统计",
            "titleClarity": 1,
            "keyword": "甲状腺",
            "keywordClarity": 1,
            "label": "死亡统计",
            "labelClarity": 1,
            "publishedJournals": "现代预防医学",
            "publishedJournalsClarity": 1,
            "fundName": "现代预防",
            "fundNameClarity": 1,
            "author": "于明娟",
            "source": 1,
            "minPublishedTime": 2018-5-12,
            "maxPublishedTime": 2016-5-12,
            "minUploadTime": 2019-5-12,
            "maxUploadTime": 2016-7-12,
            "notes": 2,
            "orderType":1,
            "page": {
                "currentPage":1,
                "pageSize":10
            }
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