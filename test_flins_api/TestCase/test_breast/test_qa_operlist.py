#coding:utf-8
import unittest
import json
import requests
from TestCase.test_breast.StartEnd import unittest_StartEnd



#获取测试题列表
class qa_operlist(unittest_StartEnd):

    '''正常参数-乳腺，sex=1，男性'''
    def test01(self):
        data = {"type":"mammaryGland","sex":1}
        url = self.url+'/qa/operlist'
        r = requests.post(url,data=json.dumps(data),headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000",response["code"],msg=response["desc"])

    '''错误参数-sex为空'''
    def test05(self):
        data = {"type": "thyroid", "sex":"" }
        url = self.url + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("1002", response["code"], msg=response["desc"])

    '''错误参数-type为空'''
    def test06(self):
        data = {"type": " ", "sex": 1}
        url = self.url + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000", response["code"], msg=response["desc"])

    '''错误参数-都为空'''
    def test07(self):
        data = {"type": " ", "sex": ""}
        url = self.url + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("1002", response["code"], msg=response["desc"])

    '''错误参数-type非法'''
    def test08(self):
        data = {"type": "abc", "sex":1}
        url = self.url + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("0000", response["code"], msg=response["desc"])

    '''错误参数-sex非法'''
    def test09(self):
        data = {"type": "abc", "sex":0}
        url = self.url + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=self.header)
        response = json.loads(r.text)
        print(r.text)
        self.assertEqual("1002", response["code"], msg=response["desc"])

if __name__ == '__main__':
    unittest.main()