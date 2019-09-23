#coding:utf-8
import unittest
import json
import requests
from TestCase.gloVal import gloVal
import yaml
from mock import mock



#提交测试题
class qa_opersave(unittest.TestCase):

    '''正常参数-乳腺，sex=2，女性'''
    def test01(self):
        data = {"type": "mammaryGland", "sex": 2}
        url = gloVal.BASE_URL + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=gloVal.C_HEADER)
        response = json.loads(r.text)
        print(r.text)
        globals()['id'] = response["data"]["id"]
        self.assertEqual("0000", response["code"], msg=response["desc"])

    #提交乳腺题目-女
    def test02(self):
        female = open("../../Paramters/breast/female.yaml","r",encoding="utf-8")
        data = yaml.load(female)
        data["id"] = id
        print(data)
        r = requests.post(gloVal.BASE_URL+'/qa/opersave',headers=gloVal.C_HEADER,data=json.dumps(data))
        print(r.text)

    def test03(self):
        r = requests.post(gloVal.BASE_URL+'/qa/opersave',headers=gloVal.C_HEADE)



if __name__ == '__main__':
    unittest.main()
