#coding:utf-8
import unittest
import json
import requests
from TestCase.test_breast.StartEnd import unittest_StartEnd
from Paramters.operate_yml import operateYaml

#查询测评限制
class ev_restrict(unittest_StartEnd):

    '''正常参数-甲状腺'''
    def test01(self):
        datas = operateYaml().read_data()
        data = datas["restrict"][1]["thyroid"]
        print(data)
        url = self.url+"/ev/restrict"
        r = requests.post(url,headers = self.header,data=json.dumps(data))
        response = json.loads(r.text)
        print('接口返回：'+r.text)
        self.assertEqual("0000",response["code"],msg=response["desc"])

    '''正常参数-乳腺'''
    def test02(self):
        data = {"type": "mammaryGland"}
        url = self.url + "/ev/restrict"
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        response = json.loads(r.text)
        print('接口返回：'+r.text)
        self.assertEqual("0000", response["code"], msg=response["desc"])

    '''参数为空'''
    def test03(self):
        data = {"type": " "}
        url = self.url + "/ev/restrict"
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        response = json.loads(r.text)
        print('接口返回：' + r.text)
        self.assertEqual("9999", response["code"], msg=response["desc"])

    '''错误参数'''
    def test04(self):
        data = {"type": "sss"}
        url = self.url + "/ev/restrict"
        r = requests.post(url, headers=self.header, data=json.dumps(data))
        response = json.loads(r.text)
        print('接口返回：' + r.text)
        self.assertEqual("9999", response["code"], msg=response["desc"])

    '''没有参数'''
    def test05(self):
        url = self.url + "/ev/restrict"
        r = requests.post(url, headers=self.header)
        response = json.loads(r.text)
        print('接口返回：' + r.text)
        self.assertEqual("9999", response["code"], msg=response["desc"])



if __name__ == '__main__':
    unittest.main()