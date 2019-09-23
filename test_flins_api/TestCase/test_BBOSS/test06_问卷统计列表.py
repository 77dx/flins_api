# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json

#select ifnull(sum(1),0) from ( select (if(count(1)>0,1,0)) from qa_quest_statistics where statistical_time >= ? and statistical_time <= ? group by channel_code_main ) t

class Test_statistical2(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.B_URL + '/pf/qa/statistics'
        self.header = {'content-type': 'application/json', 'token': gloVal.BOSS_TOKEN}


    def test01(self):

        data = {
            "startSubmitTime":"",
            "endSubmitTime":"",
            "channelCodeMain":"aviva",
            "page": {
                    "currentPage":1,
                    "pageSize":10
            }
        }
        r = requests.post(self.url, headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])




    def tearDown(self):
        pass





if __name__ == '__main__':
    unittest.main()