#coding:utf-8
import unittest
import json
import requests
from TestCase.gloVal import gloVal
from Paramters.operate_yml import operateYaml
from TestCase.test_breast.StartEnd import unittest_StartEnd



#提交测试题
class qa_opersave(unittest_StartEnd):

    '''
    正常参数-乳腺，sex=2，女性
    '''
    def test01(self):
        data = {"type": "mammaryGland", "sex": 2}
        url = gloVal.BASE_URL + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=gloVal.C_HEADER)
        response = json.loads(r.text)
        globals()['id'] = response["data"]["id"]
        self.assertEqual("0000", response["code"], msg=response["desc"])

    #提交乳腺题目-女
    def test02(self):
        data = operateYaml("E:/git_flins_api/test_flins_api/Paramters/breast/bre_female.yaml").read_data()
        data["id"] = id
        print(data)
        r = requests.post(gloVal.BASE_URL+'/qa/opersave',headers=gloVal.C_HEADER,data=json.dumps(data))
        response = json.loads(r.text)
        self.assertEqual("0000",response["code"],msg=response["desc"])

    '''
        提交甲状腺题目
    '''
    #获取测评id
    def test03(self):
        data = {"type":"thyroid","sex": 2}
        url = gloVal.BASE_URL + '/qa/operlist'
        r = requests.post(url, data=json.dumps(data), headers=gloVal.C_HEADER)
        response = json.loads(r.text)
        global tid
        tid = response["data"]["id"]
        self.assertEqual("0000", response["code"], msg=response["desc"])

    # 提交甲状腺题目-女
    def test04(self):
        data = operateYaml("E:/git_flins_api/test_flins_api/Paramters/thyroid/thy_female.yaml").read_data()
        data["id"] = tid
        print(data)
        r = requests.post(gloVal.BASE_URL + '/qa/opersave', headers=gloVal.C_HEADER, data=json.dumps(data))
        response = json.loads(r.text)
        self.assertEqual("0000", response["code"], msg=response["desc"])


if __name__ == '__main__':
    unittest.main()
