#coding:utf-8
class gloVal():

    #c端访问路径
    BASE_URL = "http://192.168.5.111/customer"

    #boss访问路径
    BOSS_URL = "http://192.168.5.111/knowledge"

    #通用header，token有效
    HEADER = {'content-type': 'application/json', "token": "7cfae0fbba37474aa2695601654963d8"}

    # 通用header，token失效
    HEADER_INVALID = {'content-type': 'application/json', "token": "18f1e5de8a2b4bdeabc26e6d36d14f52"}

    #登录验证码token
    captchaToken = ""


