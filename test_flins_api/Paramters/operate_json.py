# -*- coding:utf-8 -*-
import json

class operateJSON():

    # def __init__(self,json_file):
    #
    #     self.json_data = json_file
    #     self.data = self.read_data()

    #读取json文件
    def read_data(self,json_data):
        with open(json_data,'r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    # #根据关键字获取数据
    # def get_data(self,key):
    #     return data[key]



if __name__ == '__main__':

    s = operateJSON()
    d = s.read_data('./breast/female.json')
    print(type(d))

