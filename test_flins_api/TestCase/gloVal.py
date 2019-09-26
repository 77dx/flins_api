#coding:utf-8
class gloVal():

    #c端访问路径
    BASE_URL = "http://192.168.5.111/customer"
    # BASE_URL = "http://api.flins.com.cn/customer"
    # BASE_URL = "http://192.168.5.38"

    #c端TOKEN
    C_TOKEN = "0f529682e96b446589c60239ea67fdba"

    #c端HEADER
    C_HEADER = {'content-type': 'application/json','token':C_TOKEN}

    #知识库访问路径
    BOSS_URL = "http://192.168.5.111/knowledge"

    #BOSS访问路径
    B_URL = "http://192.168.5.111/boss"

    #BOSS_token
    BOSS_TOKEN = "9d16f0949b3c4291bde2a73a301737a8"

    #BOSS_HEADER
    BOSS_HEADER = {'content-type': 'application/json','token':BOSS_TOKEN}




