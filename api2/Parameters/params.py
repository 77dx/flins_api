# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午11:32
# @Author  : WangJuan
# @File    : datas.py

"""
定义所有测试数据
"""

import os
from Parameters import LoadYaml
from Common import Log
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = LoadYaml.GetPages().get_page_list()
    param = data[name]
    return param


class Login:
    log.info('解析yaml, Path:' + path_dir + '/Parameters/Parameter/Login.yml')
    params = get_parameter('Login')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])




if __name__ == '__main__':
    print(Login.header)