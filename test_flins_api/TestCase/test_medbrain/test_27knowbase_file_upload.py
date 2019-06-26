# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal

class knowbase_file_upload(unittest.TestCase):
    def setUp(self):
        self.url = gloVal.BOSS_URL + '/knowledgebase/file/upload'

    def test01(self):
        data = {
            "title": "4453例结节性甲状腺肿临床流行病学调查_盖宝东",
            "authors":"张婷/李惠萍/杨娅娟",
            "abstract ":"目的探讨乳腺癌患者个人掌控感现状及其影响因 素,为临床心理护理提供依据。方法在安徽省某2所三甲医院便利抽取288名住院乳腺癌患者为调查对象目的探讨乳腺癌患者个人掌控感现状及其影响因素,为临床心理护理提供依据。方法在安徽省某2所三甲医院便利抽取288名住院乳腺癌患者为调查对象",
            "number":"JZX-01001",
            "publishedJournals": "现代预防医学",
            "publishedTime":"2019-12-5",
            "childrenlClassificationName":"血液检查",
            "keyword": "乳腺癌; 掌控感; 影响因素分析",
            "source": "知网",
            "url": "www.qiniu.com",
            "sourceUrl": "www.baidu.com",
            "diseaseDirection": "甲状腺",
            "fund": "安徽省高校自然科学研究项目(KJ2017A165)",
            "sortNo": 1
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