# -*- coding:utf-8 -*-
import unittest
import requests
import json
from TestCase.gloVal import gloVal
from TestCase.test_BBOSS.StartEnd import unittest_StartEnd


#select br.* from boss_role br INNER JOIN boss_user_role bur on bur.role_id=br.id where bur.user_id=?

#select id, name, code, app_id, remark, callback_url, status, create_time from pf_merchant_info
#pf_merchant_info  商户表
#查出商户表中的所有商户信息


#商户列表
class Test_list(unittest_StartEnd):

    #该接口无参数，只需有效token
    def test01(self):
        r = requests.post(self.url+ '/pf/list', headers=self.header)
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + json.dumps(response,indent=4))
        self.assertEqual("0000", response["code"], msg=response['desc'])




if __name__ == '__main__':
    unittest.main()