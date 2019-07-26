# -*- coding:utf-8 -*-
import json

class operateJSON():

    def __init__(self):

        self.json_data = "../TestCase/test_BBOSS/JSData.json"
        self.data = self.read_data()

    #读取json文件



    def read_data(self):
        with open(self.json_data) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,key):
        return self.data[key]



if __name__ == '__main__':

    ope = operateJSON()
    print(ope.read_data())
    print(ope.get_data('pflist'))