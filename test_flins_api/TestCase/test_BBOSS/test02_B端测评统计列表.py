# -*- coding:utf-8 -*-
import unittest
import requests
from TestCase.gloVal import gloVal
import json
from TestCase.test_BBOSS.StartEnd import unittest_StartEnd

#select count(1) from (select mer_id, count(1) from pf_evaluation_statisticals where mer_id = ? group by mer_id ) tem
#select mer_id, sum(count) count from pf_evaluation_statisticals where mer_id = ? group by mer_id limit ?,?
#pf_evaluation_statisticals商户测评统计表，统计测评的次数

class Test_statistical(unittest_StartEnd):

    def test01(self):
        data = {
            "merId": "",
            "startSubmitTime":"",   #2019-07-01
            "endSubmitTime":"",     #2019-07-29
            "page":
                {
                    "currentPage":1,
                    "pageSize":10
                }
        }
        r = requests.post(self.url+ '/pf/ev/statistical', headers=self.header,data=json.dumps(data))
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])


if __name__ == '__main__':
    unittest.main()