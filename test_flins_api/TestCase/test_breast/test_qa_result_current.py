#coding:utf-8
import unittest
import json
import requests
from TestCase.gloVal import gloVal
from TestCase.test_breast.StartEnd import unittest_StartEnd

#查询最新测评结果
class qa_result_current(unittest_StartEnd):

    '''正确参数-乳腺'''
    def test01(self):
        url = gloVal.BASE_URL+'/qa/result/current'
        data={"type":"mammaryGland"}
        r = requests.post(url,headers = gloVal.C_HEADER,data=json.dumps(data))
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000",response["code"],msg=response["desc"])

    '''正确参数-甲状腺'''
    def test02(self):
        url = gloVal.BASE_URL+'/qa/result/current'
        data={"type":"1"}
        r = requests.post(url,headers = gloVal.C_HEADER,data=json.dumps(data))
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000",response["code"],msg=response["desc"])

    '''参数为空'''
    def test03(self):
        url = gloVal.BASE_URL + '/qa/result/current'
        data = {"type":1}
        r = requests.post(url, headers=gloVal.C_HEADER, data=json.dumps(data))
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000", response["code"], msg=response["desc"])

    '''错误参数'''
    def test04(self):
        url = gloVal.BASE_URL + '/qa/result/current'
        data = {"type": "abc"}
        r = requests.post(url, headers=gloVal.C_HEADER, data=json.dumps(data))
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("1003", response["code"], msg=response["desc"])



if __name__ == '__main__':
    unittest.main()