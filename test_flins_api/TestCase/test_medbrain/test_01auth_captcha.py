# -*- coding:utf-8 -*-

import requests
import unittest
from TestCase.gloVal import gloVal
import json
import base64
from Util.captcha_word import main

#登录知识库，获取验证码
class auth_captcha(unittest.TestCase):

    def setUp(self):
        self.url = gloVal.BOSS_URL
        self.img = ""

    #获取验证码token
    def atest01(self):
        url = self.url + '/auth/captcha'
        r = requests.post(url, headers={'content-type':'application/json'})
        body = r.text
        response = json.loads(r.text)
        print('接口返回：' + body)
        #提取出来验证码token
        gloVal.CAPTCHA_TOKEN = response["data"]["captchaToken"]
        # self.img = response["data"]["img"] #提取验证码图片base64
        # self.base64_image()#base64转成图片
        self.assertEqual("1051", response["code"], msg=response['desc'])

    # 正确的用户名和密码，需要验证码
    def test02(self):
        # captcha = main("captcha.jpg")  # 识别验证码
        # print(captcha)
        url = self.url + '/auth/login'
        data = {
            "account": "xiaopang",
            "pwd": "e10adc3949ba59abbe56e057f20f883e",
            "captchaToken":"",
            "captcha": ""
        }
        print(json.dumps(data))
        r = requests.post(url, headers={'content-type':'application/json'}, data=json.dumps(data))
        body = r.text
        response = json.loads(body)
        #提取token
        gloVal.TOKEN = response["data"]["token"]
        print('接口返回：' + body)
        self.assertEqual("0000", response["code"], msg=response['desc'])

    # 把验证码base64转换成图片
    def base64_image(self):
        img = base64.b64decode(self.img)
        file = open('captcha.jpg', 'wb')
        file.write(img)
        file.close()

    def tearDown(self):
        pass



if __name__ == '__main__':
    unittest.main()
